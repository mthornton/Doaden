# D&D 5e Game Session Planning — Project Memory

## Role
You help a Dungeon Master plan and run D&D 5th Edition sessions by maintaining a distilled, fast-to-search knowledge base of campaign material, so raw source PDFs never need to be reread just to answer a question.

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
| **Bramblefen** (Chapter 7) | `Prison_Breakdown_5E.md` | Location and mechanic reskin: Cell Block B → **Deep Cages**, Warden's Office → **Chainmaster's Hall**, Secret Tunnel → **The Drain**, Grolo → **Denrick**, Grolo's Stinky Sack → Denrick's "lucky" sack, the 1d20 armory-loot table and the 500 gp tunnel stash carry over verbatim. **"The Ghost"** (assassin-convict in Cell Block B who, if freed, kills six of the boss's men and vanishes) was the chassis behind the old **Prisoner X** slot — **now replaced by Gimble Beren, Dave's PC** (see below). |
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
| Wolfram Eisenherz - Todd.pdf | **Wolfram Eisenherz** | Paladin-coded human warrior from **Westfield, Western Diocese**; son of Konrad Eisenherz. Senses extraplanar presences. Killed Bishop Thurstan; the Citadel's version of that story is a lie the folk don't believe. Carries **two** of Fid's knitting spiders — both given by Fid out of Vozruk's sight; Wolfram told the rest of the party he had both. |
| Virgil.md | **Virgil** | Former **Alchemical Order** member; body covered in engineered edible symbiotic fungus, cones of plant matter where his eyes were; shapeshifts into a spider; staff empowered by exploding fungus (established in play). Backstory per the new file: an alchemist obsessed with fungi as "humanity's next stage of evolution," he experimented on corpses to test fungal symbiosis; jealous rivals exposed his research to the Church, which declared it blasphemous and sentenced him to the Penitent — he still believes he was right. **See continuity conflict below** re: how/why he left the Order. |

**Players → PCs:** Session 1 (Oct 20 2025) lists **JE, Todd, Channing** present and **Tyler** absent, with the DM running Luthien. So **Tyler = Luthien** and **Todd = Wolfram** (per the filename). JE and Channing map to JonLief and Virgil in some order — not yet confirmed. **Dave = Gimble Beren**, confirmed, joining in the second half of Chapter 7 (he fills the slot the notes formerly held open as "Prisoner X").

### world_lore/ — NPCs, gods & setting
- **THE PLAN** — `Campaign Arc Plan.md`: the campaign's north star from Chapter 7 to the finale. Covers the campaign's thematic spine (everything in Doaden is about imprisonment and who holds the keys), an honest critique of Ch1–7, the thread ledger (what to close, what to convert into finale assets, what to leave open), the chapter map to level 10–11, and the plan for reskinning *Return of the Jailer* into the Brudda Death finale at Ald's Star / St. Pyotr's. **Read this before prepping any new chapter**, and update it when play overtakes the plan. Its proposals are *not* canon unless echoed in `sessions/` or another `world_lore/` file.
- **Old Gods & mana** — `Old Gods.md`: old gods are near-immortal psychic beings sustained by worshippers' "mana"; most have faded. Core myth: `Myths and Legends of the Old Gods.docx`.
- **The central conflict** — `Saraswati and Adephagia.md`: **Saraswati** (goddess of the arts, now imprisoned in the *Prison Realm*) vs **Adephagia** (`Adephagia.md`, goddess of gluttony, the strongest surviving old god, who captured her). Sara created magic art-items to slowly rebuild her power — **and Luthien's bone guitar is one of them.** He does not know it yet. He is getting better with it than his own practice accounts for, and will keep getting better until he eventually learns what it is. The Chronicle seeds this from Ch1 onward; keep the hints coming and don't confirm it until the table earns it.
- **The lost first team** — `The First Penitents.md`: what happened to the five Penitents Vozruk sent to Dol Island before this party (Ch1). Taken alive by Adephagia's harvest crew and bled into the barrels; **Gimble Beren is the sole survivor and is now Dave's PC.** Marked DRAFT — it has open decisions at the bottom that need settling before it's canon.
- **Cult of Saraswati** (`Cult of Saraswati.md`) — secret artists' cult trying to free Sara; key members in `Corbin Wainwright and Orla Miller.md`.
- **How bondage works** — `Solteres.md` now carries the full two-door model: **Stock** (non-humans, owned outright, permanent) vs. **Terms** (humans, a purchased sentence, finite). The 50-year-sentence rule is the corrupt route that turns a human into Stock for life; **Terms** — voluntary self-sale to discharge a short sentence — is the common one. This is the backbone of the Chapter 7 slave roster and of Dov Brandt.
- **The city** — `Solteres.md`: capital of the Southern Diocese, merchant-run, syndicate-riddled, open slave markets. **This file is also the only home for two major NPCs** — **Lord Leofard Ironwake** (controls transport tax + the slave trade) and **Lady Ysabel Rochefort** (textile merchant he ruined and framed for her niece's murder; facing trial by combat) — **her five household servants are named and statted in `Chapter 7 DM Notes.md`**: Perrin Aske, Dov Brandt, Symon Reeve, Cael Ordway, Mina Dorn. Consider splitting them into their own files. **Needs a typo pass** — the file itself still has the spellings its own naming-conventions table (below) warns against: "Solares"/"Soleres," "illegae," "convected," "Ulfic." Worth cleaning up now that Ironwake is about to become the Ch7–8 antagonist.
- **NPCs** — `Master Thaddeus and Marion.md` (Alchemical Guild; Thaddeus human above the waist and tentacle below, telepathic mute wife Marion), `Turok.md` (chieftain of the Grey Wolf Tribe of the Mistwood), `Zelryn.md` (half-elf outcast; both Turok and Zelryn are NPCs with unusually full backstories, not PCs, and are not in play yet), plus PDFs: `Vozruk the Redeemer.pdf` (the party's Redeemer/master), `Orryn Cogspinner.pdf` + `Zookbert Nackle.pdf` + `Fid and Zook.pdf` (Fid the mad artificer and his assistant — only **Fid** has appeared in play so far). **Thaddeus's form — RESOLVED (Aug 2026, per the DM):** human from the waist up; below the waist, a single long, ringed, boneless **tentacle**, kept coiled around Marion's shoulders and torso on the outside of her clothing. She carries him, he rides her. At a glance he reads as an enormous worm and most people assume worm — but tentacle is correct, and the lore file's closing line ("not into a squid, but into a tentacle") was right all along. `Master Thaddeus and Marion.md` has been extended to cover the Ch6 reveal (the real transformation story he told Virgil) and the Underwood/Willowbread/pumpkin thread (see `world_lore/Underwood.md`).
- **The slaver arc (Chapter 7 cast)** — full NPC write-ups with stat blocks, all tied to **Lord Leofard Ironwake** of Solteres:
  - `Vaskar the Brand.md` — Chainmaster of Bramblefen; Chapter 7 boss. Cold, transactional, cannot model selflessness (*Blind to Love*).
  - `Old Cobb.md` — enslaved slaver's clerk; wrote down every sale, incl. JonLief's family. Kept a hidden **second ledger** of evidence against Ironwake.
  - `Anselm Vogt.md` — enslaved Westfield sheriff, leader of the Bramblefen revolt; served under Wolfram's father Konrad. The honest counterweight to Denrick.
  - `Denrick.md` — treacherous "trusty," now penned in the Pens; he trapped the Drain, and sells the party the way *out* (plus Anselm's name, to whoever is buying).
  - `The Juggernaut.md` — "Mott," Ironwake's giant pit-fighter; a *Rage Clock* boss you survive rather than out-damage.
  - `Durgan Half-Ear.md` — enslaved dwarf handler, Mott's only off-switch and the heart of the pair.
  - `Erwana.md` — escaped slave who opens the chapter: the pendant-recognition beat, Old Cobb's second ledger, and (if the party takes the Drain) their guide in. Half-Tabaxi, ex-circus (human fortune-teller mother, Tabaxi acrobat father, both killed when a mob branded her mother a heretic); sold off by the circus owner at 13. Held as **Stock** at Bramblefen despite being half human — the chapter's clearest example of the Stock/Terms injustice (see **The Eighteen** in `Chapter 7 DM Notes.md`).
- **Reference** — `Timeline.md` (Church history — **note: the file mixes two era labels, "PA" and "PC," for what is plainly the same era; the player handout normalises everything to PA, so pick one here too**: Church of Azerai, the High Bishops, the Sunlit Citadel; **modern day = 1126**), `The Quest for the Sun-Petal.md` (in-world legend / tapestry story).

### sessions/ — the play log and the prep pile
| File | Played? | Focus |
|------|---------|-------|
| Chapter 1 Welcome to Doaden.md | **Played** (Session 1, Oct 20 2025) | Waking as Penitents; the Mark; Vozruk; Finnian's armory; Fid's gadgets; voyage on *The Hreowan*; shipwreck on Dol. |
| Chapter 2 Dol Island.md | **Played** (mostly prep in file) | Saraswati's Island. Cultists harvest Sara's blood and ship it out; the party recovers the **amulet of transportation** (three crystals: one already burnt out, one spent by JonLief on the beach — **one charge left**) and the St. Pyotr map. |
| Chapter 3 Alds Star.md | **Played** (has a "Story (Session Notes)" log) | Ald's Star, a village of green-skinned halflings. Cage-hound hunt; Alice and Red die. |
| Chapter 4 Sy Pytor.md | **Played** (confirmed retroactively, Aug 2026 — not written up when it happened) | St. Pyotr's sanitorium (A1–A12 / B1–B7). Cleared cultist ambush in the garden — **including a cage hound, which the party recognised from Ald's Star**, giving them their own link between the sanitorium and the attacks on Ald's livestock. Witnessed the bell-tower hanging, found Father Ignatius's body and journal. Interrupted the black-fog ritual in the chapel and heard the herald's Brudda Death taunt, but the herald escaped. Rescued a tortured survivor and left her behind at the sanitorium. |
| Chapter 5 The Inn.md | **Played** | Four interlocking plots at the Inn; Ysabel's champion **Ulfric** assassinated via the Corvin/Marguerite ruse, arranged by Emeric for Ironwake. |
| Chapter 6 Swine Raid.md | **Played** | Escorting Lady Ysabel toward Solteres; Thaddeus reveals his real backstory to Virgil; Porcine beastmen raid (Marion nearly killed, stabilized); Willowbread dies, seeds the **Underwood** infestation lead; Virgil declines to join Thaddeus. |
| Chapter 7 DM Notes.md | **NOT YET PLAYED — prep** | The Chained Coast: raid on the slaver holdfast **Bramblefen**. Living working file; the older `Chapter 7 The Chained Coast.md` was deleted and replaced by it. **Erwana is caught at dawn, not at the evening fire** (an evening meeting sends the party marching overnight and wrecks the sundown clock). **Ysabel's five household servants travel with the party for the whole chapter — and one of them, Dov Brandt, is her property. **Ysabel herself owns non-human slaves** who work her mills and warehouses, and holds sincere, unembarrassed views about non-humans being beneath humans — play her reasonable, never cruel; see `Solteres.md`**: a Terms man she bought at Bramblefen two years ago, with three years left. He is the chapter's living explanation of Stock vs. Terms. **Garrison revised Aug 2026: 20 men (14 Fen Guard + 6 Ironwake), not 13** — beefed up around the Juggernaut and the sundown match. **Erwana and Ysabel will both honestly tell the party four or five**, because that is the normal complement and both are a month out of date; see item 9a. Correct it from the treeline before they commit, and let Anselm supply the real number. |
| Timeline.md | **Player-facing handout** | Two timelines on one sheet: (1) the Church's official chronology 0–1126 PA, written in two voices — the Church's line, and what common people say underneath — and (2) the party's own road, dated, Ch1 to now. Ends with four gaps in the official record, including that **the chronology gives no date for the Emperor's departure and never mentions he is gone.** No DM secrets. |
| The Unit Before Us.md | **Player-facing handout** | The story of the five Penitents sent to Dol before this party, and Gimble's capture — written as narrative, to hand out when Gimble joins in Ch7. Deliberately omits what neither the party nor Gimble knows: Saraswati's name, the 666 days, what the blood is for, and that the herald on that beach is the one who escaped St. Pyotr's. The DM version with those links and the open decisions is `world_lore/The First Penitents.md`. |
| Party History.md | **Player-facing recap** | Plain chronological account of Ch1–6, restricted to what the party actually witnessed or learned. No DM secrets. This is the factual base the other two player-facing files are built from — correct it first, then propagate. Audited against the chapter files Aug 2026. |
| The Penitents Chronicle.md | **Player-facing prose** | The same six chapters written as a story: scenes, dialogue, interiority. Events match `Party History.md`; the added texture is flavor, not canon. Seeds the Saraswati-guitar thread. Where it and the table disagree, the table wins. |
| Open Questions.md | **Player-facing handout** | The gap-between-sessions memory aid. Not a recap — a one-page list of what the party knows they *don't* know, plus what they're carrying, what they promised, and four questions they could answer right now if they asked. Contains **no DM secrets**; built strictly from `Party History.md`. Add a question per session; delete one only when the party says the answer out loud at the table. Current as of the end of Chapter 6. |
| Chapter 7 Run Sheet.md | **NOT YET PLAYED — prep** | At-table companion to the DM Notes: sundown clock, guard head-count, DC list, three entry branches, encounter math for 4 PCs at level 3, read-aloud per scene, NPC voice cards, revolt table, end-of-night checklist. The DM Notes are the *why*; the Run Sheet is the *at the table*. |

**Campaign chronology — SETTLED (Aug 2026, per the DM).** In-world dates now run: **branding 22 July 1126** → sails 23 July → three weeks at sea → **wreck 13 Aug, Dol 14 Aug** → **Ald's Star 15–16 Aug** (preserves the "mid-August" anchor in the Ch3 overview) → **St. Pyotr's 18 Aug** → **a month on the road, 19 Aug – 19 Sept** → **the Calf and Ass, 20 Sept** → depart 21 Sept, Thaddeus's confession 23 Sept, **swine raid 24 Sept** → two quiet weeks → **early October 1126, two days from Solteres.** Total elapsed ≈ **two and a half months**, which is what makes "out of contact with Vozruk for months" and Luthien's "two months? Three?" true. The month of aimless walking between Ch4 and Ch5 is the stretch that makes the arithmetic work — the map ended at St. Pyotr's, the party had no lead, and nobody came looking for them. It is now written into both `Party History.md` and `The Penitents Chronicle.md`. If you compress that leg later, the "months" language in three files has to come down with it.

**Note:** all session files use `Chapter N …` naming for story order, regardless of how many real table sessions a chapter takes. Chapter number and real-world session count are **not** one-to-one — Chapter 7 (the Bramblefen raid), for instance, is expected to take 2–3 real play sessions on its own. Use the Played? column in the table above, not the filename, to know whether a chapter has actually happened.

After a real session, offer to add a new `Chapter N ….md` (or append) and to update the related `world_lore/` NPC and `players/` files.

### Where the story stands (as of Chapter 7 prep, Aug 2026)
> **For where the story is *going*, see `world_lore/Campaign Arc Plan.md`.** This section is the snapshot; that file is the route to the finale.

Three plots run in parallel, plus a standing institutional problem:

1. **The cosmic plot (warm again as of Ch4).** Adephagia's cultists harvested Saraswati's blood on Dol Island (Ch2) and shipped it away in barrels to fuel a ritual bringing **the Jailer / Prison Master — Brudda Death**, ruler of the Prison Realm — into Doaden. At St. Pyotr's (Ch4), the party interrupted a black-fog ritual in the chapel and heard a cultist herald invoke Brudda Death directly — the party's first exposure to that name. The herald escaped before the ritual could be fully stopped, and the garden trapdoor at St. Pyotr's was never opened, so the site isn't necessarily finished business. The Chapter 7 ledger seeds the plot further: women sold to unnamed buyers who "paid well."
2. **The slaver plot (active — this is Chapter 7).** JonLief's wife **Maren** and son **Rowan** were sold, not killed. The trail runs Bramblefen → **Old Cobb's ledger** → a chimney sweep named **Barney Soot** in Solteres → **Lord Ironwake**, who is also rigging Lady Ysabel's trial by combat using the Juggernaut as his champion. Ysabel's trial lands in Chapter 8.
3. **The Underwood / Alchemical Order plot (warm, deferred).** Thaddeus and Marion are investigating a spreading magical spore/pumpkin infestation in **Underwood** (a farming village a day's ride outside Haleyon — see `world_lore/Underwood.md`) on the Alchemical Order's behalf. In Ch6, Thaddeus asked Virgil to come help directly, dangling a return to the Order's good graces, but Virgil declined, choosing to stay with the party under their standing Church orders. The pumpkin seeds are parasitic and lethal (magic is Enchantment/Necromancy/Transmutation, confirmed by Virgil to be concentrated in the seeds, not the flesh); a **coven of witches** grows them somewhere inland. Untouched since Ch6.
4. **The Church problem (standing).** The party has been out of contact with Vozruk for weeks, has no way back to camp, and is about to sack a nobleman's holding. Slavery is illegal by Church ruling, which is a defense — but a defense somebody has to accept. Nothing has been decided about consequences.

**Unresolved debts and loose ends worth remembering:** the first Penitent team lost on Dol was never found; the *Hreowan*'s crew is unaccounted for; the amulet of transportation has **one charge left** and points one-way into Saraswati's crypt; Fid gave Luthien the Ball of Undeath against Vozruk's explicit order; Wolfram promised Ald there were no more beasts nearby; the party took six jars of pickled cabbage from a dead man's house without telling anyone; the garden trapdoor at St. Pyotr's (Ch4, A7) was never opened.

> **DM-only future hook (do NOT put in `sessions/Party History.md` or otherwise reveal to players):** at St. Pyotr's (Ch4), the party rescued a tortured, mentally-broken woman from the torture chamber, healed her, then chose to leave her behind in an unlocked cell with a few days of rations rather than bring her along — reasoning they weren't equipped to care for her and needed to stay focused on the Church's mission. Per the DM (Aug 2026), she is intended to become possessed by Adephagia and return later seeking revenge on the party. Keep this out of player-facing material until it actually happens at the table.

> **DM-only future hook — TODO, needs a proper `world_lore/` write-up (do NOT put in `sessions/Party History.md` or otherwise reveal to players):** the "very old man" who approached the party at the Inn (Ch5), invisible/unnoticed to everyone else in the room, who thanked them for stopping the Brudda Death summoning at St. Pyotr's — he is **the Emperor**, unseen for over a thousand years. This is a major reveal being held back from the party; the game's recurring "May he rise again" refrain (used by NPCs across multiple villages) is presumably tied to this. Write him up properly in `world_lore/` (motive, why he can go unnoticed, why he's surfacing now, connection to `Timeline.md`'s Church history) before he reappears at the table.

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
| **Alchemical Order** | Alchemetic Order, Alchemic Order (used in `players/Virgil.md` itself — worth a fix) |
| **Adephagia** | Aldephiaga |
| **Finnian Quickstep** | Finnan |
| **Church of Azerai**; the **Mark of Atonement**; the **Sunlit Citadel** | — |
| **Brudda Death**, also called the Jailer and the Prison Master | — |
| **Maren** (JonLief's wife), **Rowan** (his son) | — |

### Known continuity conflicts (flag before using, don't silently pick one)
- **Who remembers Maren and Rowan — RESOLVED.** `Old Cobb.md` has been updated to match `Chapter 7 DM Notes.md` (item 4): Maren and Rowan arrived **together, about a month ago**; Maren died of fever shortly after. Both files now agree. (Previously this page said the Cobb file still needed updating — it's been done.)
- **Durgan duplicates Cobb — still live, and now safe to just cut.** `Durgan Half-Ear.md` still carries the "optional connective hook" letting Durgan also be the one who knows Maren and Rowan's fate. Now that `Old Cobb.md` and Ch7 DM Notes agree and Cobb is firmly established as the one who tells JonLief about his family, running Durgan's version too just makes the reveal redundant — recommend cutting the hook from `Durgan Half-Ear.md` rather than leaving it "optional."
- **Chapter 3 was retconned mid-file.** The `# Overview` section has Ald as a middle-aged human and the village farming rye, wheat, apples and goats. The `Story (Session Notes)` section has green-skinned halflings whose entire economy is heirloom cabbage. **The Story section is what happened.**
- **Real player names in prose.** Chapter 1 narrates the branding of *"Tyler"* rather than Luthien. Chapter 3 has a slur-adjacent NPC descriptor. Chapter 7 item 2 describes Mott as "mildly retarted" — `The Juggernaut.md` handles the same idea as "his mind never grew with his body," which is the phrasing to prefer.
- **Ysabel's charge.** Chapter 5 says she's accused of poisoning her niece; `Solteres.md` says Ironwake had the niece murdered and framed her. These are compatible — the second is the truth behind the first — but say so explicitly if it comes up.
- **Why Virgil left the Alchemical Order — RESOLVED (Aug 2026, per the DM).** `players/Virgil.md` is canon: rivals exposed his fungal research to the Church, it was declared blasphemous, and he was *sentenced* to the Penitent. Involuntary, and he still believes he was right. His Ch3 line to Ald — that he and the Order "no longer agree on some core principles" — is **Virgil saving face**, not a second version of events. Play it as a practiced deflection he reaches for rather than tell the real story; the party has only ever heard his account.

### House rules & file conventions (so edits match the DM's style)
- **Tiered result ladders** rather than single DCs for information delivery: `0-10: / 11-15: / 16-19: / 20: / Nat 20+:`. Plain DCs are used for physical checks.
- **A sanity stat** exists (Ch4 calls for a sanity-loss check). Not a standard 5e rule.
- **Parentheses are the DM-only aside marker** — item stats and rules notes are written inline in parentheses, mid-prose.
- **Branch logic is written as `IF the party…` lines**, including a branch for inaction.
- Encounters are listed as bare rosters ("1 demagogue / 2 cultists / 1 bruiser"); stat blocks live in `world_lore/` or the processed summaries, not in the session files.
- Read-aloud text is second-person present tense and is **not** visually marked in Chapters 1–6; the Chapter 7 files upgrade this to `> **Read-aloud —**` blockquotes. Prefer the newer convention going forward.

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
- **After any edit, just report what you changed.** Do not commit or push — see the git rule at the top of this file.
- When a fact changes in one place, check the other files that repeat it — the slaver-arc NPC files, the Chapter 7 notes, and the Run Sheet all restate the same details and drift apart easily.

## Preferences
- System: D&D 5e
- **Party:** 4 PCs — JonLief, Luthien Veynar, Wolfram Eisenherz, Virgil. **Level 3** as of Chapter 7 prep (Aug 2026). Update this when they level.
- **5th player: Dave — CONFIRMED (Aug 2026).** Playing **Gimble Beren**, gnome ranger (`players/Gimble Beren.md`), who joins in the second half of **Chapter 7**. Gimble replaces the old "Prisoner X" placeholder in the Deep Cages. **He is a Penitent and the sole survivor of the first team Vozruk sent to Dol Island** — see `world_lore/The First Penitents.md` for what happened to them. **Dave writes Gimble's personal backstory; the Dol Island events are the DM's.** Don't write stats.
- The DM writes prep in two layers: a discursive **DM Notes** file (why things are true) and a terse **Run Sheet** (what to say and roll at the table). Match that split when generating new prep.
_(add more as needed — session cadence, house rules, DM style)_
