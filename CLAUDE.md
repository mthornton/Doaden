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
- **Cloud/remote sessions cannot delete files** on the local disk. Anything that needs deleting gets moved into `_to_delete/` instead — that folder is disposable junk (stale git lock files from interrupted commits), and Michael can remove it by hand at any time. Don't treat it as content.

## Folder Structure & Rules
- `raw_campaigns/` — original source PDFs (published modules, homebrew adventures, session notes, handouts). **Read-only.** Never edit or delete anything here. **Git-ignored** (too large for GitHub) — present only on the primary machine.
- `processed_campaigns/` — condensed summaries you generate, one file per raw source (or per campaign if a campaign spans multiple PDFs). This is the primary place you read from.
- `processed_campaigns/_index.md` — master index of every processed summary, with a one-line description and last-processed date for each. Always keep this current.
- `players/` — player-character sheets & backstories for the active home game (the party begin as **Penitents** of the Church of Azerai). Primary reference for PC questions. Read-mostly; update when a PC changes.
- `world_lore/` — NPCs, deities/factions, myths, timeline, and quest lore for the home campaign's world (**Doaden**). Primary reference for "who/what is X" questions. Mixed `.md` / `.docx` / `.pdf`.
- `sessions/` — notes for the home campaign, in chronological order (one file per chapter). Holds **both played chapters and unplayed prep** — see the sessions table below before describing anything as history.
- **Known junk, safe to ignore or delete:** `_to_delete/` (stale git locks), `sessions/.fuse_hidden0000000a00000001`, `processed_campaigns/_writetest.txt`.

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

### Published modules being mined for the home game
The home campaign reskins published Bestiarum material rather than running it straight. Track the mapping so a question about a Bramblefen mechanic can be answered from the source summary:

| Home-game element | Source | Notes |
|---|---|---|
| **Bramblefen** (Session 7) | `Prison_Breakdown_5E.md` | Location and mechanic reskin: Cell Block B → **Deep Cages**, Warden's Office → **Chainmaster's Hall**, Secret Tunnel → **The Drain**, Grolo → **Denrick**, Grolo's Stinky Sack → Denrick's "lucky" sack, the 1d20 armory-loot table and the 500 gp tunnel stash carry over verbatim. **"The Ghost"** (assassin-convict in Cell Block B who, if freed, kills six of the boss's men and vanishes) is the un-statted chassis behind **Prisoner X**. |
| **Old Cobb** | Warden Ingfar (`Prison_Breakdown_5E.md`, also in `Prisoner_X_Iron_Juggernaut.md`) | Inverted: the captive being tortured is now the party's emotional payload rather than a quest-giver. |
| **The Juggernaut / Mott** | `Prisoner_X_Iron_Juggernaut.md` (name only) | The home-game Mott is **original** — a Rage Clock barbarian, not the CR 10 Iron Juggernaut. Don't confuse the two stat blocks. |
| **Path of Penitence** framework | `Path_of_Penitence_System.md` | Campaign rules + Doaden setting; the Penitent/Redeemer structure the party sits inside. |
| **The Jailer / Brudda Death** arc | `Rise_of_the_Jailer.md`, `Return_of_the_Jailer.md` | The cosmic plot's endgame material, not yet used in play. |

## Home Campaign — Doaden (players / world_lore / sessions)
The user runs a live D&D 5e home game set in **Doaden** using the **Path of Penitence** framework; the party begin as **Penitents** conscripted into the service of the **Church of Azerai**. These three folders are the *living* campaign record — read them first for anything about *this* group's ongoing story (as opposed to the published-module catalog in `processed_campaigns/`).

### The Penitent premise (established in Chapter 1)
Four strangers wake as prisoners in a Church of Azerai camp, branded on the shoulder with the **Mark of Atonement** (a stylized sun with a single tear), and are assigned as a unit to **Vozruk the Redeemer**. Each owes **500 years of service**, reduced per successful mission. Camp guards wear the same Mark, faded — former Penitents, so release is at least nominally possible. **No reporting or check-in mechanic has ever been established**, and since Chapter 3 the party has been months of travel from camp with no orders and no contact. That vacuum is a live plot lever, not an oversight to paper over.

### players/ — the party (PCs)
| File | Character | Established in play |
|------|-----------|---------------------|
| JonLief.md | **JonLief** | **Elf** (confirmed by NPCs). Bow/sword/light armor, bear-fur cloak that "fits perfectly." Meditates instead of sleeping. The party's de-escalator and diplomat. Exiled noble; secret marriage; wife **Maren** and son **Rowan** banished and (he now learns) sold, not killed. |
| Luthien Veynar.md | **Luthien Veynar** | Half-elf bard/satirist (human scholar + elven minstrel); turned on the hypocritical Church of the Radiant Flame. Surfer/stoner voice ("dude," "like"). Carries a stolen **bone guitar** and Fid's **Ball of Undeath**. Banned from the camp armory for life. |
| Wolfram Eisenherz - Todd.pdf | **Wolfram Eisenherz** | Paladin-coded human warrior from **Westfield, Western Diocese**; son of Konrad Eisenherz. Senses extraplanar presences. Killed Bishop Thurstan; the Citadel's version of that story is a lie the folk don't believe. Carries **two** of Fid's knitting spiders (he may not know about the second). |
| *(no file)* | **Virgil** | **Gap — no character file exists.** Established in play: former **Alchemical Order** member, body covered in engineered edible symbiotic fungus, cones of plant matter where his eyes were; shapeshifts into a spider; staff empowered by exploding fungus. Left the Order over "core principals." Offer to create `players/Virgil.md`. |

**Players → PCs:** Session 1 (Oct 20 2025) lists **JE, Todd, Channing** present and **Tyler** absent, with the DM running Luthien. So **Tyler = Luthien** and **Todd = Wolfram** (per the filename). JE and Channing map to JonLief and Virgil in some order — not yet confirmed. **Dave** is a prospective fifth player: the Session 7 notes hold **Prisoner X** unwritten specifically so he can become Dave's PC.

### world_lore/ — NPCs, gods & setting
- **Old Gods & mana** — `Old Gods.md`: old gods are near-immortal psychic beings sustained by worshippers' "mana"; most have faded. Core myth: `Myths and Legends of the Old Gods.docx`.
- **The central conflict** — `Saraswati and Adephagia.md`: **Saraswati** (goddess of the arts, now imprisoned in the *Prison Realm*) vs **Adephagia** (`Adephagia.md`, goddess of gluttony, the strongest surviving old god, who captured her). Sara created magic art-items to slowly rebuild her power.
- **Cult of Saraswati** (`Cult of Saraswati.md`) — secret artists' cult trying to free Sara; key members in `Corbin Wainwright and Orla Miller.md`.
- **The city** — `Solteres.md`: capital of the Southern Diocese, merchant-run, syndicate-riddled, open slave markets. **This file is also the only home for two major NPCs** — **Lord Leofard Ironwake** (controls transport tax + the slave trade) and **Lady Ysabel Rochefort** (textile merchant he ruined and framed for her niece's murder; facing trial by combat). Consider splitting them into their own files.
- **NPCs** — `Master Thaddeus and Marion.md` (Alchemical Guild; Thaddeus transformed into a giant worm, telepathic mute wife Marion), `Turok.md` (chieftain of the Grey Wolf Tribe of the Mistwood), `Zelryn.md` (half-elf outcast; both Turok and Zelryn are NPCs with unusually full backstories, not PCs, and are not in play yet), plus PDFs: `Vozruk the Redeemer.pdf` (the party's Redeemer/master), `Orryn Cogspinner.pdf` + `Zookbert Nackle.pdf` + `Fid and Zook.pdf` (Fid the mad artificer and his assistant — only **Fid** has appeared in play so far).
- **The slaver arc (Session 7 cast)** — full NPC write-ups with stat blocks, all tied to **Lord Leofard Ironwake** of Solteres:
  - `Vaskar the Brand.md` — Chainmaster of Bramblefen; Session 7 boss. Cold, transactional, cannot model selflessness (*Blind to Love*).
  - `Old Cobb.md` — enslaved slaver's clerk; wrote down every sale, incl. JonLief's family. Kept a hidden **second ledger** of evidence against Ironwake.
  - `Anselm Vogt.md` — enslaved Westfield sheriff, leader of the Bramblefen revolt; served under Wolfram's father Konrad. The honest counterweight to Denrick.
  - `Denrick.md` — treacherous "trusty"; sells the party a trapped tunnel.
  - `The Juggernaut.md` — "Mott," Ironwake's giant pit-fighter; a *Rage Clock* boss you survive rather than out-damage.
  - `Durgan Half-Ear.md` — enslaved dwarf handler, Mott's only off-switch and the heart of the pair.
- **Reference** — `Timeline.md` (Church history in PA/PC eras: Church of Azerai, the High Bishops, the Sunlit Citadel; **modern day = 1126**), `The Quest for the Sun-Petal.md` (in-world legend / tapestry story).

### sessions/ — the play log and the prep pile
| File | Played? | Focus |
|------|---------|-------|
| Chapter 1 Welcome to Doaden.md | **Played** (Session 1, Oct 20 2025) | Waking as Penitents; the Mark; Vozruk; Finnian's armory; Fid's gadgets; voyage on *The Hreowan*; shipwreck on Dol. |
| Chapter 2 Dol Island.md | **Played** (mostly prep in file) | Saraswati's Island. Cultists harvest Sara's blood and ship it out; the party recovers the **amulet of transportation** (2 charges) and the St. Pyotr map. |
| Chapter 3 Alds Star.md | **Played** (has a "Story (Session Notes)" log) | Ald's Star, a village of green-skinned halflings. Cage-hound hunt; Alice and Red die. |
| Chapter 4 Sy Pytor.md | **Prep — appears unplayed** | Room-key delve of St. Pyotr's sanitorium (A1–A12 / B1–B7). Father Ignatius, the black-fog ritual, the herald, "Brudda Death." |
| Chapter 5 The Inn.md | **Played** | Four interlocking plots at the Inn; Ysabel's champion **Ulfric** assassinated via the Corvin/Marguerite ruse, arranged by Emeric for Ironwake. |
| Chapter 6 Swine Raid.md | **Played** | Escorting Lady Ysabel toward Solteres; Porcine beastmen raid; Thaddeus's magical-pumpkin problem and the plea to help **Haleyon**. |
| Session 7 DM Notes.md | **NOT YET PLAYED — prep** | The Chained Coast: raid on the slaver holdfast **Bramblefen**. Living working file; the older `Chapter 7 The Chained Coast.md` was deleted and replaced by it. |
| Session 7 Run Sheet.md | **NOT YET PLAYED — prep** | At-table companion to the DM Notes: sundown clock, guard head-count, DC list, three entry branches, encounter math for 4 PCs at level 3, read-aloud per scene, NPC voice cards, revolt table, end-of-night checklist. The DM Notes are the *why*; the Run Sheet is the *at the table*. |

**Note:** file naming is inconsistent by design history — `Chapter N …` for the first six, `Session 7 …` for the current prep. Chapter number and session number are **not** one-to-one (Chapter 4 was prepped but never run). Anything named `Session N …` is a working file for a session that hasn't happened yet — never describe it as something the party has done.

After a real session, offer to add a new `Chapter N ….md` (or append) and to update the related `world_lore/` NPC and `players/` files.

### Where the story stands (as of Session 7 prep, Aug 2026)
Three plots run in parallel, plus a standing institutional problem:

1. **The cosmic plot (cold since Ch4).** Adephagia's cultists harvested Saraswati's blood on Dol Island (Ch2) and shipped it away in barrels to fuel a ritual bringing **the Jailer / Prison Master — Brudda Death**, ruler of the Prison Realm — into Doaden. St. Pyotr's (Ch4 prep) is the next node and was never run. The Session 7 ledger seeds it back in: women sold to unnamed buyers who "paid well."
2. **The slaver plot (active — this is Session 7).** JonLief's wife **Maren** and son **Rowan** were sold, not killed. The trail runs Bramblefen → **Old Cobb's ledger** → a chimney sweep named **Barney Soot** in Solteres → **Lord Ironwake**, who is also rigging Lady Ysabel's trial by combat using the Juggernaut as his champion. Ysabel's trial lands in Session 8.
3. **The Haleyon / Alchemical Order plot (warm, deferred).** Master Thaddeus asked the party to help Haleyon with a spreading magical-pumpkin infestation, in exchange for restoring Virgil's standing with the Order. The seeds are parasitic and lethal; a **coven of witches** grows them somewhere inland. Untouched since Ch6.
4. **The Church problem (standing).** The party has been out of contact with Vozruk for weeks, has no way back to camp, and is about to sack a nobleman's holding. Slavery is illegal by Church ruling, which is a defense — but a defense somebody has to accept. Nothing has been decided about consequences.

**Unresolved debts and loose ends worth remembering:** the first Penitent team lost on Dol was never found; the *Hreowan*'s crew is unaccounted for; the amulet of transportation has 2 charges and points one-way into Saraswati's crypt; Fid gave Luthien the Ball of Undeath against Vozruk's explicit order; Wolfram's second knitting spider is a secret; Wolfram promised Ald there were no more beasts nearby; the party took six jars of pickled cabbage from a dead man's house without telling anyone.

### Naming conventions to hold to
The session files are written fast and unedited, so **treat any proper noun in `sessions/` as approximate.** Canonical spellings:

| Use | Not |
|---|---|
| **Solteres** | Solaries, Soleres, Solares |
| **Lady Ysabel Rochefort** | Rockfort |
| **Lord Leofard Ironwake** | — |
| **JonLief** (one word) | Jon Lief, Jon Leif, Joneric |
| **Virgil** | Virgl |
| **Vozruk** | Volzruk |
| **Wolfram Eisenherz**, of **Westfield, Western Diocese** | — |
| **St. Pyotr** | St. Pytor, Sy Pytor (the Ch4 filename is wrong; leave the filename, fix the prose) |
| **Ald's Star** | Alds Star (filename only) |
| **Alchemical Order** | Alchemetic Order |
| **Adephagia** | Aldephiaga |
| **Finnian Quickstep** | Finnan |
| **Church of Azerai**; the **Mark of Atonement**; the **Sunlit Citadel** | — |
| **Brudda Death**, also called the Jailer and the Prison Master | — |
| **Maren** (JonLief's wife), **Rowan** (his son) | — |

### Known continuity conflicts (flag before using, don't silently pick one)
- **Who remembers Maren and Rowan.** `Old Cobb.md` says Cobb recalls "a half-elf woman and a small boy, brought in **years apart**." `Session 7 DM Notes.md` (item 4) says they arrived **together, about a month ago**, and Maren died of fever shortly after. The Session 7 version is the current one; the Cobb file needs updating.
- **Durgan duplicates Cobb.** `Durgan Half-Ear.md` carries an "optional connective hook" letting Durgan be the one who knows Maren and Rowan's fate. That is now Cobb's job. Keep it optional or cut it — running both makes the ledger redundant.
- **Chapter 3 was retconned mid-file.** The `# Overview` section has Ald as a middle-aged human and the village farming rye, wheat, apples and goats. The `Story (Session Notes)` section has green-skinned halflings whose entire economy is heirloom cabbage. **The Story section is what happened.**
- **Real player names in prose.** Chapter 1 narrates the branding of *"Tyler"* rather than Luthien. Chapter 3 has a slur-adjacent NPC descriptor. Session 7 item 2 describes Mott as "mildly retarted" — `The Juggernaut.md` handles the same idea as "his mind never grew with his body," which is the phrasing to prefer.
- **Ysabel's charge.** Chapter 5 says she's accused of poisoning her niece; `Solteres.md` says Ironwake had the niece murdered and framed her. These are compatible — the second is the truth behind the first — but say so explicitly if it comes up.

### House rules & file conventions (so edits match the DM's style)
- **Tiered result ladders** rather than single DCs for information delivery: `0-10: / 11-15: / 16-19: / 20: / Nat 20+:`. Plain DCs are used for physical checks.
- **A sanity stat** exists (Ch4 calls for a sanity-loss check). Not a standard 5e rule.
- **Parentheses are the DM-only aside marker** — item stats and rules notes are written inline in parentheses, mid-prose.
- **Branch logic is written as `IF the party…` lines**, including a branch for inaction.
- Encounters are listed as bare rosters ("1 demagogue / 2 cultists / 1 bruiser"); stat blocks live in `world_lore/` or the processed summaries, not in the session files.
- Read-aloud text is second-person present tense and is **not** visually marked in Chapters 1–6; the Session 7 files upgrade this to `> **Read-aloud —**` blockquotes. Prefer the newer convention going forward.

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
- **Encounter math is the DM's most common ask.** The party is small and low level; when suggesting a fight, state the adjusted XP against the 4-PC level-3 thresholds (Easy 300 / Medium 600 / Hard 900 / Deadly 1600) rather than eyeballing CR.

## Maintenance
- If `raw_campaigns/` has new or changed PDFs, flag it and offer to (re)process before answering questions — don't let summaries go stale silently.
- After each real game session, offer to append to that campaign's Session Log and update Open Threads based on what happened.
- For small updates, patch just the relevant section of a summary rather than regenerating the whole file.
- Keep summaries scannable: tables and bullets over prose.
- When a fact changes in one place, check the other files that repeat it — the slaver-arc NPC files, the Session 7 notes, and the Run Sheet all restate the same details and drift apart easily.

## Preferences
- System: D&D 5e
- **Party:** 4 PCs — JonLief, Luthien Veynar, Wolfram Eisenherz, Virgil. **Level 3** as of Session 7 prep (Aug 2026). Update this when they level.
- **Possible 5th player:** Dave. Prisoner X is being held blank as his entry point — don't write stats or backstory for that character.
- The DM writes prep in two layers: a discursive **DM Notes** file (why things are true) and a terse **Run Sheet** (what to say and roll at the table). Match that split when generating new prep.
_(add more as needed — session cadence, house rules, DM style)_
