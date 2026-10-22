"""
podcastToSpeech.py — turn a two-host podcast transcript into one MP3.

Reads only lines that start with a speaker tag, e.g.
    THEO: Welcome back to Who Holds the Keys...
    JUNE: And I'm June...
Everything else in the file (headings, notes, the ideas list) is ignored.

Usage (from this folder):
    export OPENAI_API_KEY="sk-..."
    python3 podcastToSpeech.py "../../podcast/Episode 01 - The Wedding in Solteres.md"

Optional:
    --out episode01.mp3        output file (default: same name as the transcript, .mp3)
    --model tts-1              cheaper/faster than the default tts-1-hd
    --voice THEO=onyx --voice JUNE=nova   change who sounds like whom

Cost guide: tts-1-hd is about $30 per million characters, so a 45-minute
episode (~50,000 characters) is roughly $1.50.
"""
import argparse
import os
import re
import sys

from openai import OpenAI

# Voice options: alloy, echo, fable, onyx, nova, shimmer
DEFAULT_VOICES = {"THEO": "onyx", "JUNE": "nova"}
MAX_CHARS = 3000  # the API limit is 4,096 characters per request

LINE = re.compile(r"^([A-Z][A-Z ]{1,20}):\s+(.+)$")


def parse_transcript(path):
    """Return a list of (speaker, text) in order."""
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            m = LINE.match(raw.strip())
            if m:
                lines.append((m.group(1).strip(), m.group(2).strip()))
    return lines


def split_long(text, max_chars=MAX_CHARS):
    """Split an over-long line on sentence boundaries."""
    if len(text) <= max_chars:
        return [text]
    parts, current = [], ""
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        if len(current) + len(sentence) + 1 > max_chars and current:
            parts.append(current.strip())
            current = ""
        current += sentence + " "
    if current.strip():
        parts.append(current.strip())
    return parts


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("transcript")
    ap.add_argument("--out")
    ap.add_argument("--model", default="tts-1-hd")
    ap.add_argument("--voice", action="append", default=[], help="SPEAKER=voice, e.g. JUNE=shimmer")
    args = ap.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit('OPENAI_API_KEY is not set.\nRun:  export OPENAI_API_KEY="your-key-here"')
    client = OpenAI(api_key=api_key)

    voices = dict(DEFAULT_VOICES)
    for v in args.voice:
        name, _, voice = v.partition("=")
        voices[name.strip().upper()] = voice.strip()

    lines = parse_transcript(args.transcript)
    if not lines:
        sys.exit("No speaker lines found. Each spoken line must start like 'THEO: ...'.")
    unknown = sorted({s for s, _ in lines} - set(voices))
    if unknown:
        sys.exit(f"No voice set for: {', '.join(unknown)}. Add --voice NAME=voice.")

    out = args.out or os.path.splitext(args.transcript)[0] + ".mp3"
    total_chars = sum(len(t) for _, t in lines)
    print(f"{len(lines)} lines, {total_chars:,} characters. Writing {out}")

    with open(out, "wb") as audio:
        for i, (speaker, text) in enumerate(lines, 1):
            for chunk in split_long(text):
                print(f"  [{i}/{len(lines)}] {speaker}")
                response = client.audio.speech.create(model=args.model, voice=voices[speaker], input=chunk)
                for part in response.iter_bytes():
                    audio.write(part)

    print(f"Done: {out}")


if __name__ == "__main__":
    main()
