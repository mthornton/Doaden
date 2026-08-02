# D&D 5e Game Session Planning — Project Memory

## Role
You help a Dungeon Master plan and run D&D 5th Edition sessions by maintaining a distilled, fast-to-search knowledge base of campaign material, so raw source PDFs never need to be reread just to answer a question.

## Repository & Sync (git)
This project lives in a **git repository** (`git/Doaden`, branch `main`, remote `origin` → github.com/mthornton/Doaden) and is pulled to another computer also used for D&D planning. **After making any change to files here — summaries, session notes, NPCs, players, or this file — stage, commit with a clear message, and push:**

```
git add -A
git commit -m "…"
git push
```

- **`raw_campaigns/` is git-ignored** (NOT synced). The source PDFs are ~11 GB and several exceed GitHub's 100 MB per-file limit, so they live only on the primary machine. The committed `processed_campaigns/_extracted/` text cache stands in for them elsewhere — read that on other machines instead of the PDFs.
- If a `git push` can't reach the network from a given session, still make the commit, and note that it needs pushing from the primary machine.

## Folder Structure & Rules
- `raw_campaigns/` — original source PDFs (published modules, homebrew adventures, session notes, handouts). **Read-only.** Never edit or delete anything here. **Git-ignored** (too large for GitHub) — present only on the primary machine.
- `processed_campaigns/` — condensed summaries you generate, one file per raw source (or per campaign if a campaign spans multiple PDFs). This is the primary place you read from.
- `processed_campaigns/_index.md` — master index of every processed summary, with a one-line description and last-processed date for each. Always keep this current.
- `players/` — player-character sheets & backstories for the active home game (the party begin as **Penitents** of the Church of Azerai). Primary reference for PC questions. Read-mostly; update when a PC changes.
- `world_lore/` — NPCs, deities/factions, myths, timeline, and quest lore for the home campaign's world (**Doaden**). Primary reference for "who/what is X" questions. Mixed `.md` / `.docx` / `.pdf`.
- `sessions/` — chronological notes from sessions already played (one file per chapter). Primary reference for "what happened / what did the party do" questions; append here after each session.

## Lookup Order (always follow this)
1. Check the **Active Campaigns** table below.
2. Check `processed_campaigns/_index.md` for the full list of summaries.
3. Read the relevant `processed_campaigns/{name}.md` file(s).
4. **Only** if the summary doesn't answer the question, is out of date, or the user needs exact original wording (e.g. exact stat block numbers, read-aloud boxed text) — open the corresponding PDF(s) in `raw_campaigns/`.

When you do have to fall back to raw_campaigns/, say so, and offer to update the processed summary with what you found.

For questions about the **home campaign** — this specific party, its NPCs, world lore, or sessions already played — look in `players/`, `world_lore/`, and `sessions/` first (not `processed_campaigns/`, which is the catalog of published/homebrew modules). See **Home Campaign — Doaden** below.

## Active Campaigns (hot cache)
| Campaign | Status | One-line | Summary file |
|---|---|---|---|
| The Man Eaters (saga) | Catalogued | Lvl 5→9; cannibal Man Eaters faction; Man Hunt → Red Dawn (Siege of Guerrin) | Man_Eaters_Saga.md |
| Calden Keep (saga) | Catalogued | Lvl 5→5-10; revenants & the Goliath; Calden Keep → The Undying Lord | Calden_Keep_Saga.md |
| Crisis in the North: Siege of Sturmenburg | Catalogued | Lvl 5-10; Beastmen invasion (Escalation campaign, Ch2-3) | Siege_of_Sturmenburg.md |
| The Eternal Legions Rise | Catalogued | Lvl 5-13; undead legions; Echoes of War → Lord of War (Ch2-3; Ch1=The Dreadlights) | Eternal_Legions.md |
| The Penitent Crusade | Catalogued | Lvl 5-13; zealot trilogy: Indictum Dominus → Purgation → Under Cover of Darkness | Penitent_Crusade.md |

> **Full catalog:** all 35 processed summaries are indexed in `processed_campaigns/_index.md`. Status **Catalogued** = processed but not yet run — change to *In progress* / *Completed* as you play. Raw-text extractions are cached in `processed_campaigns/_extracted/`.

## Home Campaign — Doaden (players / world_lore / sessions)
The user runs a live D&D 5e home game set in **Doaden** using the **Path of Penitence** framework; the party begin as **Penitents** conscripted into the service of the **Church of Azerai**. These three folders are the *living* campaign record — read them first for anything about *this* group's ongoing story (as opposed to the published-module catalog in `processed_campaigns/`).

### players/ — the party (PCs)
| File | Character | Notes |
|------|-----------|-------|
| JonLief.md | JonLief | Exiled noble; secret marriage, banished wife & son he's sworn to find and protect |
| Luthien Veynar.md | Luthien Veynar | Half-elf bard/satirist (human scholar + elven minstrel); turned on the hypocritical Church of the Radiant Flame |
| Wolfram Eisenherz - Todd.pdf | Wolfram Eisenherz | PC played by Todd (PDF character sheet) |

_Players named in session notes: JE, Todd, Channing, Tyler, plus the DM. Match players to PCs as this becomes clear._

### world_lore/ — NPCs, gods & setting
- **Old Gods & mana** — `Old Gods.md`: old gods are near-immortal psychic beings sustained by worshippers' "mana"; most have faded. Core myth: `Myths and Legends of the Old Gods.docx`.
- **The central conflict** — `Saraswati and Adephagia.md`: **Saraswati** (goddess of the arts, now imprisoned in the *Prison Realm*) vs **Adephagia** (`Adephagia.md`, goddess of gluttony, the strongest surviving old god, who captured her). Sara created magic art-items to slowly rebuild her power.
- **Cult of Saraswati** (`Cult of Saraswati.md`) — secret artists' cult trying to free Sara; key members in `Corbin Wainwright and Orla Miller.md`.
- **NPCs** — `Master Thaddeus and Marion.md` (Alchemical Guild; Thaddeus transformed into a giant worm, telepathic mute wife Marion), `Turok.md` (chieftain of the Grey Wolf Tribe of the Mistwood), `Zelryn.md` (half-elf outcast), plus PDFs: `Vozruk the Redeemer.pdf`, `Orryn Cogspinner.pdf`, `Zookbert Nackle.pdf`, `Fid and Zook.pdf`.
- **Reference** — `Timeline.md` (Church history, dated in PA/PC eras: Church of Azerai, the High Bishops, the holy city / Sunlit Citadel), `The Quest for the Sun-Petal.md` (in-world legend / tapestry story).

### sessions/ — play log (one file per chapter, chronological)
| File | Session focus |
|------|---------------|
| Chapter 1 Welcome to Doaden.md | Party wakes as Penitents of the Church of Azerai (Session 1, Oct 20 2025) |
| Chapter 2 Dol Island.md | Dol / Saraswati's Island — where Sara was lured & imprisoned; DM notes on the Adephagia infiltration plot |
| Chapter 3 Alds Star.md | Alds Star, a small southern-coast farming village (pop. ~78) owned by Ald |
| Chapter 4 Sy Pytor.md | Room-by-room delve of St. Pyotr's (Saint Pyotr, "healer of madness") |
| Chapter 5 The Inn.md | Intrigue at the Inn — the plot to assassinate Ulfric using the lovers Corvin & Marguerite |
| Chapter 6 Swine Raid.md | Escorting Lady Ysabel to Solteres; Master Thaddeus's pumpkin/swine infestation at Haleyon |

When asked about the home game, read the relevant file(s) here first. After a real session, offer to add a new `Chapter N ….md` here (or append) and to update the related `world_lore/` NPC and `players/` files.

## Processing Workflow
Run this whenever asked to "process campaigns," "update summaries," or on first setup:
1. List every PDF in `raw_campaigns/`.
2. For each raw file with no matching summary, or whose raw file is newer than its summary, extract and read it in full.
3. Write or update `processed_campaigns/{same-base-name}.md` using the Summary Template below.
4. Update `processed_campaigns/_index.md` and the Active Campaigns table above.
5. Don't reprocess unchanged files — check modification dates first.

### Reading the source PDFs
Most 5e adventure PDFs are text-heavy with occasional maps/handouts/illustrations:
- Run `pdfinfo` and `pdffonts` first to confirm the PDF has a real text layer (not a scan).
- Use `pdftotext -layout` or pdfplumber for the primary text extraction — this is where stat blocks, boxed read-aloud text, and narrative live.
- Only rasterize/view pages visually for battle maps, player handouts, or illustrations where the image itself matters (e.g. you need to describe a map layout). Don't rasterize the whole PDF — it's expensive and usually unnecessary for text content.
- If a stat block or table extracts garbled, rasterize just that page and read it visually instead of guessing at numbers.

## Summary Template
Use this structure for every file in `processed_campaigns/`:

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

## Session Log / Timeline
Chronological recap of what's happened so far, including party decisions and consequences (if session notes exist).

## Treasure & Rewards
- Item — where found / who has it — notable properties

## Secrets & Twists
- ...

## Open Threads / Things to Remember
- ...
```

## Answering Questions
- Default to `processed_campaigns/` first — don't open raw PDFs unless needed.
- Say which campaign/summary an answer came from.
- If the processed summary can't answer it, say so explicitly before checking `raw_campaigns/`.
- If a raw-file lookup turns up info missing from the summary (new NPC, changed stat block, plot detail), mention it and offer to fold it into the summary.
- For quick session prep ("what do I need for tonight"), pull directly from the relevant summary's Session Log, Encounters, and Open Threads sections rather than re-summarizing from scratch.

## Maintenance
- If `raw_campaigns/` has new or changed PDFs, flag it and offer to (re)process before answering questions — don't let summaries go stale silently.
- After each real game session, offer to append to that campaign's Session Log and update Open Threads based on what happened.
- For small updates, patch just the relevant section of a summary rather than regenerating the whole file.
- Keep summaries scannable: tables and bullets over prose.

## Preferences
- System: D&D 5e
_(add more as needed — session cadence, party composition/level, house rules, DM style)_