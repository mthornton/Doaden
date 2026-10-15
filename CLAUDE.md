# D&D 5e Game Session Planning — Project Memory

## Role
You help Michael, the Dungeon Master, plan and run his **D&D 5e home campaign, Doaden** — prep, NPCs, lore, continuity, and the record of what happened at the table. **The home-campaign files (`sessions/`, `world_lore/`, `players/`) are the canon and your primary source.** He also keeps a library of published modules (`processed_campaigns/`) that he mines for ideas; that library is **not canon** and is mostly noise — see the rule under Lookup Order.

**This file is the operating manual, not the lore.** The present is in `sessions/Campaign State.md`, the undecided is in `sessions/Decisions.md`, and the world is in `world_lore/` (see its `_index.md`). Don't copy lore into this file — link to it.

## Repository & Sync (git)

> ## ⛔ NEVER RUN GIT COMMANDS THAT WRITE
> **Do not `git add`, `git commit`, `git push`, `git stash`, `git checkout`, `git reset`, or anything else that writes to the repository or to `.git/`. Michael manages version control himself, entirely.**
>
> Agent sessions run against a mounted filesystem that cannot properly delete git's lock files, so every agent-run commit leaves behind stale `.git/*.lock` and `.git/objects/*/tmp_obj_*` files that break his next commit. This is not a preference — it actively breaks the repo.
>
> **Just edit the files and stop.** Then tell him plainly what you changed and that it's ready for him to review and commit. Never offer to commit. Never say "I'll commit this for you." If a task seems to require a commit, do the file edits and hand it back.
>
> Read-only git (`git status`, `git log`, `git diff`) is fine when he asks a question about repo state.

This project lives in a **git repository** (`git/Doaden`, branch `main`, remote `origin` → github.com/mthornton/Doaden) and is pulled to another computer also used for D&D planning.

- **`raw_campaigns/` is git-ignored** (NOT synced). The source PDFs are ~11 GB and several exceed GitHub's 100 MB per-file limit, so they live only on the primary machine. The committed `processed_campaigns/_extracted/` text cache stands in for them elsewhere — read that on other machines instead of the PDFs.
- **Cloud/remote sessions cannot delete files** on the local disk. Anything that needs deleting gets moved into `_to_delete/` instead — that folder is disposable junk (stale git lock files from earlier agent commits, from before the rule above), and Michael can remove it by hand at any time. Don't treat it as content.

## Folder Structure & Rules
- `sessions/` — notes for the home campaign, in chronological order. From Chapter 7 on, each played chapter has a **`Chapter N - Record.md`** (what actually happened — the canon); Chapters 1–6 are single chapter files mixing prep and session notes; unplayed chapters are **prep**; see the sessions table below before describing anything as history. Also holds **`Campaign State.md`** (the present), **`Decisions.md`** (every open DM decision), and the player-facing handouts (Timeline, Chronicle, Player Open Questions).
- `world_lore/` — NPCs, deities/factions, myths, timeline, and quest lore for the home campaign's world (**Doaden**). Primary reference for "who/what is X" questions; **`_index.md`** lists every file with its status. Mixed `.md` / `.docx` / `.pdf`.
- `players/` — player-character sheets & backstories for the active home game. Primary reference for PC questions. Read-mostly; update when a PC changes.
- `processed_campaigns/` — **the published-module library. Not canon.** Summaries of purchased/homebrew adventures Michael pulls ideas and stat blocks from; most will never be used. **Ignore it unless the task is about a module — see the rule under Lookup Order.** How to use, search and maintain it is in `processed_campaigns/README.md`.
- `raw_campaigns/` — the source PDFs behind that library. **Read-only, git-ignored**, primary machine only.
- **Known junk, safe to ignore or delete:** `_to_delete/` (stale git locks), `sessions/.fuse_hidden0000000a00000001`, `processed_campaigns/_writetest.txt`.
- `_archive/` — superseded files kept for the DM's reference only (old prep, per-session logs, retired handouts and NPCs). **Ignore it — see the Archived Files rule under Lookup Order.** Contents listed in `_archive/README.md`.

## Lookup Order (always follow this)

> ### 🗄️ Archived files — ignore them
> **Everything under `_archive/` (and the junk in `_to_delete/`) is superseded. It is not canon and it is often wrong** — it holds prep for scenes that never happened, NPCs who never appeared, and older versions of facts that have since changed.
> - **Exclude `_archive/` and `_to_delete/` from every search** (grep, find, glob) and from every review of "the material."
> - **Never use an archived file as a source** for an answer, a summary, a handout, or new prep — even if it is the only place a detail appears. If something only exists in the archive, tell Michael and ask whether to restore it; don't quietly re-use it.
> - **Never link to or cite archived files** from live files, and don't edit them.
> - **The only exceptions:** Michael explicitly asks about an archived file, or asks why something was designed the way it was (the old prep holds the reasoning). Even then, say that the file is archived and may be out of date.
> - When you archive something, add it to `_archive/README.md` with what replaced it, and repoint any links to it.

> ### 📚 Published modules are not canon
> **`processed_campaigns/` and `raw_campaigns/` are a library of published adventures, not part of Doaden.** Nothing in them is true in the home campaign unless a file in `sessions/`, `world_lore/` or `players/` has adopted it.
> - **Leave both folders out of general searches and reviews of "the material."** They are 38 files of other people's campaigns and they will drown the real ones.
> - **Never mix a module's NPCs, places, factions or plot into an answer about the home game.** If you suggest borrowing something, say it is a borrowing.
> - **Open the library only when** Michael asks about a module, asks for ideas / encounters / stat blocks from it, asks you to process PDFs, or you need mechanics from a module the home game is **reskinning** (the table below). When you do, read `processed_campaigns/README.md` first, and say which module you are quoting.
> - **Never reprocess or "update summaries" unless he asks.**

**For anything about the home campaign, look in this order:**
1. **`sessions/Campaign State.md`** — where everything stands right now. Then the sessions table below — which chapters are played, which are prep.
2. **The most recent `sessions/Chapter N - Record.md`** (or, for Chapters 1–6, the chapter file's session notes) for what happened, and the current chapter's planning/prep file for what's coming. The Record wins over any prep.
3. **`world_lore/`** for who/what/why — start from **`world_lore/_index.md`**, which says what each file covers and how far to trust it — and **`world_lore/Campaign Arc Plan.md`** for where the campaign is going (proposals, not canon, unless echoed elsewhere).
4. **`players/`** for the PCs.
5. **Player-facing handouts** (`sessions/Timeline.md`, `The Penitents Chronicle.md`, `Player Open Questions.md`) only for what the *players* know.

6. **`sessions/Decisions.md`** for anything still undecided. Don't treat an open item's recommendation as canon.

Say which file an answer came from.

### Published modules being mined for the home game
The only modules with a live connection to Doaden. The home campaign reskins them rather than running them straight; open these summaries for mechanics and stat blocks. **Everything else in the library is inspiration only.**

| Home-game element | Source | Notes |
|---|---|---|
| **Bramblefen** (Chapter 7) | `Prison_Breakdown_5E.md` | Location and mechanic reskin: Cell Block B → **Deep Cages**, Warden's Office → **Chainmaster's Hall**, Secret Tunnel → **The Drain**, Grolo → **Denrick**, Grolo's Stinky Sack → Denrick's "lucky" sack, the 1d20 armory-loot table and the 500 gp tunnel stash carry over verbatim. **"The Ghost"** (assassin-convict in Cell Block B who, if freed, kills six of the boss's men and vanishes) was the chassis behind the old **Prisoner X** slot — **now replaced by Gimble Beren, Dave's PC** (see below). ⚠️ **As played (Oct 2026): the Drain and Denrick never came into play and were cut.** |
| **Old Cobb** | Warden Ingfar (`Prison_Breakdown_5E.md`, also in `Prisoner_X_Iron_Juggernaut.md`) | Inverted: the captive being tortured is now the party's emotional payload rather than a quest-giver. |
| **The Juggernaut / Mott** | `Prisoner_X_Iron_Juggernaut.md` (name only) | The home-game Mott is **original** — a Rage Clock barbarian, not the CR 10 Iron Juggernaut. Don't confuse the two stat blocks. |
| **Path of Penitence** framework | `Path_of_Penitence_System.md` | Campaign rules + Doaden setting; the Penitent/Redeemer structure the party sits inside. |
| **The Jailer / Brudda Death** arc | `Rise_of_the_Jailer.md`, `Return_of_the_Jailer.md` | The cosmic plot's endgame material, not yet used in play. |

## The home campaign in one paragraph
A live D&D 5e game set in **Doaden**, using the **Path of Penitence** framework (`processed_campaigns/Path_of_Penitence_System.md`). The party woke as prisoners in a Church of Azerai camp, branded with the **Mark of Atonement** (a sun with a single tear), and were made a unit under **Vozruk the Redeemer**, each owing **500 years** of service, reduced per completed mission. They were sent to Dol Island and have been out of contact ever since. **No reporting mechanic has ever been established** — that vacuum is a plot lever, not an oversight. Everything in the campaign is about imprisonment and who holds the keys *(Arc Plan §1)*.

### The party
| PC | Player | File | Notes |
|---|---|---|---|
| **JonLief** | JE or Channing *(unconfirmed)* | `players/JonLief.md` | Elf; exiled noble; wife **Elizabeth** (dead), son **Rowan** (sold). |
| **Luthien Veynar** | Tyler | `players/Luthien Veynar.md` | Half-elf bard; stolen bone guitar (a Saraswati vessel — he doesn't know). |
| **Wolfram Eisenherz** | Todd | `players/Wolfram Eisenherz.md` (+ original PDF) | Human paladin, Oath of Devotion, of **Westfield, Western Diocese**; killed Bishop Thurstan. |
| **Gimble Beren** | Dave | `players/Gimble Beren.md` | Gnome ranger; Penitent; sole survivor of the first Dol team. **Dave writes Gimble's personal backstory; the Dol events are the DM's.** Don't write stats. |
| **Baltus's apprentice** | Virgil's former player | `players/Baltus's Apprentice.md` | Unbranded Shepherd's apprentice. **Name and backstory TBD.** |
| *Virgil* | — | `world_lore/Virgil.md` | **NPC since end of Ch7**, with Thaddeus at Underwood. |

**Level 4** as of the end of Chapter 7. Update `Campaign State.md` when they level.

### sessions/ — what's in it
| File | What it is |
|---|---|
| `Campaign State.md` | **The present.** Read first; update after every session. |
| `Decisions.md` | **Every open DM decision**, with recommendations, plus a log of settled ones. |
| `Chapter 1 …` – `Chapter 6 …` | **Played.** Each file mixes prep and session notes; where they disagree, the session notes are what happened. |
| `Chapter 7 - Record.md` | **Played** (3 sessions). The canonical record of what happened. |
| `Chapter 8 DM Notes - Planning.md` | **Prep — not yet played.** |
| `Timeline.md` | Player handout. Part Two is **the factual base for all player-facing files** — correct it first, then propagate. |
| `The Penitents Chronicle.md` | Player-facing prose of Chs 1–7. Flavor is not canon. |
| `Player Open Questions.md` | Player handout: what the party knows they don't know. |
| `The Unit Before Us.md` | Player handout given to Gimble: the first team's story. |

Chapter number ≠ session count — one chapter can take several sessions. **From Chapter 8 on, each played chapter gets a `Chapter N - Record.md`.**

**Campaign chronology — SETTLED (Aug 2026, per the DM).** In-world dates now run: **branding 22 July 1126** → sails 23 July → three weeks at sea → **wreck 13 Aug, Dol 14 Aug** → **Ald's Star 15–16 Aug** (preserves the "mid-August" anchor in the Ch3 overview) → **St. Pyotr's 18 Aug** → **a month on the road, 19 Aug – 19 Sept** → **the Calf and Ass, 20 Sept** → depart 21 Sept, Thaddeus's confession 23 Sept, **swine raid 24 Sept** → two quiet weeks → **early October 1126, two days from Solteres.** Total elapsed ≈ **two and a half months**, which is what makes "out of contact with Vozruk for months" and Luthien's "two months? Three?" true. The month of aimless walking between Ch4 and Ch5 is the stretch that makes the arithmetic work — the map ended at St. Pyotr's, the party had no lead, and nobody came looking for them. It is written into `sessions/Timeline.md` and the Chronicle. **Chapter 7 runs 8–10 Oct 1126.** If you compress that leg later, the "months" language in three files has to come down with it.

### 🔒 Never put these in a player-facing file
The Timeline, Chronicle and Player Open Questions hold **only what the party witnessed or was told**. Keep out, among others:
- **Elizabeth's bargain with Brudda Death** and **Rowan's immunity** (`Elizabeth and the Green.md`).
- **That the guitar is a Saraswati vessel**, the vessel roster, and the bone (`The Art-Items.md`).
- **Who the Patient became** (`The Patient.md`) and **who the old man at the Inn is** (the Emperor).
- **That the party ended the harvest**, and the cask count (`The Barrel Trail.md`).
- **What Vaskar is hiding from Ironwake** (Ch8 plan §2–3a), and Corbin's crimes and bargain.
- Anything marked DM ONLY. When in doubt, check the Record for whether the party actually saw it.

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
| **St. Pyotr** | St. Pytor, Sy Pytor |
| **Ald's Star** | Alds Star |
| **Alchemical Order** | Alchemetic Order, Alchemic Order |
| **Adephagia** | Aldephiaga |
| **Finnian Quickstep** | Finnan |
| **Church of Azerai**; the **Mark of Atonement**; the **Sunlit Citadel** | — |
| **Brudda Death**, also called the Jailer and Brudda Death | — |
| **Elizabeth** (JonLief's wife), **Rowan** (his son) | — |

### Known continuity traps
- **Chapter 3 was retconned mid-file.** The `# Overview` has Ald as a human grain farmer; the `Story (Session Notes)` section has green-skinned halflings and heirloom cabbage. **The Story section is what happened.**
- **Ysabel's charge.** Ch5 says she's accused of poisoning her niece; `Solteres.md` says Ironwake had the niece murdered and framed her. Compatible — the second is the truth behind the first.
- **Virgil's Ch3 line** that he and the Order "no longer agree" is him saving face; `world_lore/Virgil.md` is canon (he was sentenced).
- **Real player names in prose.** Ch1 narrates the branding of *"Tyler"* rather than Luthien. Ch3 has a slur-adjacent NPC descriptor. For Mott, use `The Juggernaut.md`'s phrasing: "his mind never grew with his body."
- **Era labels.** `world_lore/Timeline.md` mixes "PA" and "PC"; use **PA**.

### House rules & file conventions (so edits match the DM's style)
- **Tiered result ladders** rather than single DCs for information delivery: `0-10: / 11-15: / 16-19: / 20: / Nat 20+:`. Plain DCs are used for physical checks.
- **A sanity stat** exists (Ch4 calls for a sanity-loss check). Not a standard 5e rule.
- **Parentheses are the DM-only aside marker** — item stats and rules notes are written inline in parentheses, mid-prose.
- **Branch logic is written as `IF the party…` lines**, including a branch for inaction.
- Encounters are listed as bare rosters ("1 demagogue / 2 cultists / 1 bruiser"); stat blocks live in `world_lore/` or the processed summaries, not in the session files.
- Read-aloud text is second-person present tense and is **not** visually marked in Chapters 1–6; the Chapter 7 files upgrade this to `> **Read-aloud —**` blockquotes. Prefer the newer convention going forward.
- **Prep comes in two layers:** a discursive **DM Notes** / planning file (why things are true) and a terse **Run Sheet** (what to say and roll at the table). Match that split.
- **When something is decided, rewrite the section cleanly** rather than stacking a "SETTLED" note on top, and log it in `Decisions.md`.

## Answering Questions
- Default to the home-campaign files (see Lookup Order). Say which file an answer came from.
- For quick session prep ("what do I need for tonight"), pull from the current chapter's planning file and the latest Record rather than re-summarizing from scratch.
- **Encounter math is the DM's most common ask.** When suggesting a fight, state the adjusted XP against the 5-PC level-4 thresholds (Easy 625 / Medium 1,250 / Hard 1,875 / Deadly 2,500) rather than eyeballing CR. **The DM deliberately runs encounters out of balance** so the players look for better solutions than a fair fight — report the math, don't rebalance it.
- **Published modules:** see `processed_campaigns/README.md`. Only when asked.

## Maintenance
- **After each real game session**, offer to: write or extend that chapter's `Chapter N - Record.md`; update `Campaign State.md`; move anything settled or overtaken in `Decisions.md`; update the affected `world_lore/` and `players/` files; then the player handouts (Timeline Part Two first, then the Chronicle and Player Open Questions).
- For small updates, patch the relevant section rather than regenerating the whole file.
- **After any edit, just report what you changed.** Do not commit or push — see the git rule at the top of this file.
- When a fact changes in one place, check the other files that repeat it — the NPC files, the chapter Record, the current chapter plan, `Campaign State.md` and the player handouts all restate the same details and drift apart easily.
- **Keep this file short.** New lore goes in `world_lore/` with a line in its `_index.md`; new decisions go in `Decisions.md`; the present goes in `Campaign State.md`.

## Preferences
- System: D&D 5e.
- Michael manages git himself (see top).
- _(add more as needed — session cadence, house rules, DM style)_
