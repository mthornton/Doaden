# processed_campaigns/ — the published-module library

> **Not canon.** These are condensed summaries of published and homebrew adventures Michael owns. He pulls from them for inspiration, mechanics and stat blocks. **Most will never be used.** Nothing in here is true in Doaden unless a file in `sessions/`, `world_lore/` or `players/` has adopted it. See the "Published modules are not canon" rule in `CLAUDE.md`.
>
> **Moved here from `CLAUDE.md` (Oct 2026)** so it only loads when someone is actually working with the library.

## When to open this folder

- Michael asks about a specific module, or asks for ideas / encounters / stat blocks from the library.
- You need mechanics or a stat block from a module the home game is **reskinning** — the "Published modules being mined" table in `CLAUDE.md` lists them.
- Michael asks you to process new PDFs.

Otherwise, leave it out of searches and reviews.

## Files

- `_index.md` — master index of every summary, with a one-line description and last-processed date. Keep it current when you add or reprocess a summary.
- `{name}.md` — one summary per raw source (or per campaign if it spans several PDFs).
- `_extracted/` — cached raw-text extractions of the PDFs. **`raw_campaigns/` is git-ignored and only exists on Michael's primary machine**, so on any other machine read `_extracted/` instead of the PDFs.
- `_writetest.txt` — junk, ignore.

## Looking something up in a module

1. Find it in `_index.md`.
2. Read the summary.
3. **Only** if the summary doesn't answer the question, or Michael needs exact original wording (stat block numbers, read-aloud boxed text), open the source — `raw_campaigns/` on the primary machine, `_extracted/` elsewhere. Say that you did, and offer to fold what you found into the summary.

Say which summary an answer came from. When borrowing from a module for the home game, say that it's a borrowing, not canon.

## Processing Workflow

Run this **only when Michael asks** to "process campaigns" or "update summaries":

1. List every PDF in `raw_campaigns/`.
2. For each raw file with no matching summary, or whose raw file is newer than its summary, extract and read it in full.
3. Write or update `processed_campaigns/{same-base-name}.md` using the template below.
4. Update `_index.md`.
5. Don't reprocess unchanged files — check modification dates first.

### Reading the source PDFs

- Run `pdfinfo` and `pdffonts` first to confirm the PDF has a real text layer.
- Use `pdftotext -layout` or pdfplumber for the primary extraction — stat blocks, boxed text and narrative live there.
- Only rasterize pages where the image matters (battle maps, handouts). Don't rasterize the whole PDF.
- If a stat block or table extracts garbled, rasterize just that page and read it visually instead of guessing.

## Summary Template

```markdown
# [Campaign / Adventure Name]
**Source:** raw_campaigns/[filename]
**Last processed:** [date]
**Level range:** [e.g. 1–5]

## Overview
1–3 sentence premise and setting.

## Key NPCs
| Name | Role | Motivation | Location | Stat block ref |
|------|------|------------|----------|----------------|

## Key Locations
- Name — short description, notable features

## Encounters / Combat
| Encounter | Location | Monsters (CR) | Notes / tactics |
|-----------|----------|----------------|------------------|

## Plot / Quest Threads
| Thread | Status | Notes |
|--------|--------|-------|

## Treasure & Rewards
- Item — where found / who has it — notable properties

## Secrets & Twists
- ...

## Open Threads / Things to Remember
- ...
```

- For small updates, patch the relevant section rather than regenerating the whole file.
- Keep summaries scannable: tables and bullets over prose.

## Former "Active Campaigns" table *(removed from CLAUDE.md, Oct 2026)*

These five sagas were listed as a "hot cache." **None has been run; all are only catalogued.**

| Campaign | Level | One-line | File |
|---|---|---|---|
| The Man Eaters (saga) | 5→9 | Cannibal Man Eaters faction; Man Hunt → Red Dawn (Siege of Guerrin) | Man_Eaters_Saga.md |
| Calden Keep (saga) | 5→10 | Revenants & the Goliath; Calden Keep → The Undying Lord | Calden_Keep_Saga.md |
| Crisis in the North: Siege of Sturmenburg | 5–10 | Beastmen invasion (Escalation campaign, Ch2–3) | Siege_of_Sturmenburg.md |
| The Eternal Legions Rise | 5–13 | Undead legions; Echoes of War → Lord of War | Eternal_Legions.md |
| The Penitent Crusade | 5–13 | Zealot trilogy: Indictum Dominus → Purgation → Under Cover of Darkness | Penitent_Crusade.md |
