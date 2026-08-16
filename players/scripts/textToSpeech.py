import os
from openai import OpenAI

# Initialize client from the OPENAI_API_KEY environment variable.
# Never hardcode the key here — this file is committed to git.
#   export OPENAI_API_KEY="sk-..."        (add to ~/.zshrc to make it permanent)
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(
        "OPENAI_API_KEY is not set.\n"
        'Run:  export OPENAI_API_KEY="your-key-here"\n'
        "or add that line to ~/.zshrc and open a new terminal."
    )
client = OpenAI(api_key=api_key)

# 1. Configuration - Set your file inputs and voice preferences
input_text_file = "ThePenitentsChronicle.txt"  # Name of your input text file
output_audio_file = "ThePenitentsChronicle.mp3"  # Name of the generated audiobook
chosen_voice = "onyx"  # Voice options: alloy, echo, fable, onyx, nova, shimmer
chosen_model = "tts-1-hd"  # Use 'tts-1-hd' for high quality, 'tts-1' for cheaper

# 2. Split text safely into chunks well below the 4,096-character limit
def split_text_by_paragraphs(text, max_chars=3000):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) + 2 < max_chars:
            current_chunk += para + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# 3. Read the file, process text chunks, and stream to a single output file
try:
    with open(input_text_file, "r", encoding="utf-8") as f:
        story_text = f.read()

    text_chunks = split_text_by_paragraphs(story_text)
    print(f"Loaded '{input_text_file}'. Split into {len(text_chunks)} parts.")

    with open(output_audio_file, "wb") as master_audio_file:
        for i, chunk in enumerate(text_chunks):
            print(f"Generating audio for part {i+1}/{len(text_chunks)}...")

            response = client.audio.speech.create(
                model=chosen_model,
                voice=chosen_voice,
                input=chunk
            )

            for audio_chunk in response.iter_bytes():
                master_audio_file.write(audio_chunk)

    print(f"Success! Complete audiobook saved as: {output_audio_file}")

except FileNotFoundError:
    print(f"Error: Could not find the file '{input_text_file}'. Make sure it is in the same folder as this script.")
except Exception as e:
    print(f"An error occurred: {e}")
