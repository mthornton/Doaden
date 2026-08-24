#!/usr/bin/env python3
"""
Bramblefen Session 2 — Table Kit.

Five printable pages:
  1. Sundown clock strips (cut out, slide a marker along)
  2. Board state + flags sheet (write on it)
  3-4. Read-aloud, in running order
  5. Names at a glance

Run:  python3 make_table_kit.py
Out:  Bramblefen Table Kit.pdf
"""

import os, sys

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
except ModuleNotFoundError as missing:
    sys.exit(
        "\nMissing Python library: %s\n"
        "\nThis script needs 'reportlab'. Install it with:\n"
        "\n    pip3 install reportlab\n"
        "\nIf that fails with \"externally-managed-environment\", use:\n"
        "\n    pip3 install --user reportlab\n" % missing.name
    )

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Bramblefen Table Kit.pdf")
PW, PH = letter
M = 0.55 * inch

INK = (0.12, 0.11, 0.10)
MUTED = (0.45, 0.43, 0.41)
RULE = (0.72, 0.70, 0.67)
OX = (0.42, 0.13, 0.11)
STEEL = (0.16, 0.24, 0.34)
GREEN = (0.24, 0.34, 0.24)
VIOLET = (0.32, 0.22, 0.36)
AMBER = (0.60, 0.42, 0.10)
CHAR = (0.18, 0.18, 0.18)


def wrap(c, text, font, size, maxw):
    c.setFont(font, size)
    out, line = [], ""
    for w in text.split():
        t = (line + " " + w).strip()
        if c.stringWidth(t, font, size) <= maxw:
            line = t
        else:
            if line:
                out.append(line)
            line = w
    if line:
        out.append(line)
    return out


def para(c, x, y, text, maxw, font="Helvetica", size=8.4, lead=0.135, colour=INK):
    c.setFillColorRGB(*colour)
    for ln in wrap(c, text, font, size, maxw):
        c.setFont(font, size)
        c.drawString(x, y, ln)
        y -= lead * inch
    return y


def page_title(c, title, sub=""):
    c.setFillColorRGB(*CHAR)
    c.rect(0, PH - 0.72 * inch, PW, 0.72 * inch, stroke=0, fill=1)
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(M, PH - 0.44 * inch, title)
    if sub:
        c.setFont("Helvetica", 8)
        c.drawRightString(PW - M, PH - 0.42 * inch, sub)
    return PH - 0.72 * inch - 0.30 * inch


def checkbox(c, x, y, label, size=8.6, box=0.115):
    c.setStrokeColorRGB(*MUTED)
    c.setLineWidth(0.7)
    c.rect(x, y - 0.012 * inch, box * inch, box * inch, stroke=1, fill=0)
    c.setFillColorRGB(*INK)
    c.setFont("Helvetica", size)
    c.drawString(x + (box + 0.06) * inch, y, label)


def ruled(c, x, y, w, n, gap=0.235):
    c.setStrokeColorRGB(*RULE)
    c.setLineWidth(0.5)
    for i in range(n):
        c.line(x, y - i * gap * inch, x + w, y - i * gap * inch)
    return y - n * gap * inch


# ---------------------------------------------------------------- 1. the clock
def clock_strip(c, x, y, w, h):
    """5:30 -> 8:00 timeline."""
    start, end = 5 * 60 + 30, 8 * 60
    span = end - start

    def px(minutes):
        return x + (minutes - start) / span * w

    c.setFillColorRGB(0.97, 0.96, 0.93)
    c.setStrokeColorRGB(*MUTED)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 0.08 * inch, stroke=1, fill=1)

    axis = y + h * 0.40
    c.setStrokeColorRGB(*CHAR)
    c.setLineWidth(2.2)
    c.line(x + 0.18 * inch, axis, x + w - 0.18 * inch, axis)

    # ticks
    t = start
    while t <= end:
        major = (t % 30 == 0)
        tx = px(t)
        c.setStrokeColorRGB(*CHAR)
        c.setLineWidth(1.6 if major else 0.8)
        c.line(tx, axis, tx, axis - (0.15 if major else 0.09) * inch)
        if major:
            c.setFillColorRGB(*INK)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(tx, axis - 0.31 * inch, "%d:%02d" % (t // 60, t % 60))
        t += 15

    beats = [
        (5 * 60 + 30, "IN THE GATE", MUTED, 0.13),
        (7 * 60 + 15, "HAMMERING STOPS", AMBER, 0.13),
        (7 * 60 + 45, "COBB DIES", OX, 0.30),
        (8 * 60, "SUNDOWN \u00b7 THE MATCH", CHAR, 0.13),
    ]
    for minutes, label, col, row in beats:
        bx = px(minutes)
        c.setFillColorRGB(*col)
        c.circle(bx, axis, 0.055 * inch, stroke=0, fill=1)
        if row > 0.2:
            c.setStrokeColorRGB(*col)
            c.setLineWidth(0.7)
            c.line(bx, axis + 0.06 * inch, bx, axis + row * inch - 0.02 * inch)
        c.setFont("Helvetica-Bold", 6.6)
        tw = c.stringWidth(label, "Helvetica-Bold", 6.6)
        lx = min(max(bx - tw / 2, x + 0.06 * inch), x + w - tw - 0.06 * inch)
        c.drawString(lx, axis + row * inch, label)

    c.setFillColorRGB(*MUTED)
    c.setFont("Helvetica-Oblique", 6.4)
    c.drawCentredString(x + w / 2, y + 0.075 * inch,
                        "Put this where the players can see it. Slide the marker. Say the time out loud.")


def page_clock(c):
    y = page_title(c, "The Sundown Clock", "Chapter 7 · Bramblefen · Session 2")
    w = PW - 2 * M
    for i in range(3):
        clock_strip(c, M, y - (i + 1) * 1.62 * inch + 0.15 * inch, w, 1.42 * inch)

    ty = y - 3 * 1.62 * inch
    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M, ty, "MARKERS — cut out, fold, sit one on the line")
    ty -= 0.28 * inch
    for i in range(8):
        mx = M + i * 0.62 * inch
        c.setFillColorRGB(*OX)
        p = c.beginPath()
        p.moveTo(mx, ty)
        p.lineTo(mx + 0.30 * inch, ty)
        p.lineTo(mx + 0.15 * inch, ty - 0.26 * inch)
        p.close()
        c.drawPath(p, stroke=0, fill=1)

    ty -= 0.72 * inch
    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M, ty, "WHAT EACH BEAT MEANS")
    ty -= 0.24 * inch
    for label, txt in [
        ("5:30", "Party inside the gate. Yard working, whipping post active, ring half-built. Vaskar is told a buyer has arrived within a minute."),
        ("~6:00", "Vaskar receives them in the Hall. Courteous. Lies for ten minutes. Cobb is in that building."),
        ("6:30–7:15", "The party's window. Pens, stock, Denrick, Corvant, Anselm, the yard."),
        ("7:15", "Hammering stops. Ring finished. Off-duty Ironwake men wake and drift out. Cobb's interrogation goes quiet — Vaskar has decided he is empty."),
        ("7:45", "Vaskar leaves the office for the arena. COBB DIES HERE if nobody reached him."),
        ("8:00", "Sundown. The match. Every eye on the ring. Anselm's signal lands here."),
        ("after", "Vaskar's move on Ysabel — only if all three conditions hold."),
    ]:
        c.setFillColorRGB(*OX)
        c.setFont("Helvetica-Bold", 8.4)
        c.drawString(M, ty, label)
        ty = para(c, M + 0.62 * inch, ty, txt, PW - 2 * M - 0.62 * inch, size=8.2, lead=0.128)
        ty -= 0.05 * inch

    ty -= 0.10 * inch
    c.setFillColorRGB(*OX)
    c.setFont("Helvetica-Bold", 8.6)
    c.drawString(M, ty, "Anything that keeps Vaskar in his office keeps Cobb breathing.")
    ty -= 0.16 * inch
    para(c, M, ty, "A buyer to receive, a price to haggle, an alarm to answer, a noblewoman to be courteous to. "
                   "Ysabel's cover story is a life-support machine for a man the party has never met, and they will never know it.",
         PW - 2 * M, size=8.2)


# --------------------------------------------------------- 2. board state page
def page_board(c):
    y = page_title(c, "Board State — write on this", "Session 2 · positions live on the table, not here")
    colw = (PW - 2 * M - 0.30 * inch) / 2
    rx = M + colw + 0.30 * inch

    # ---- hour / rests
    c.setStrokeColorRGB(*CHAR)
    c.setLineWidth(1.2)
    c.rect(M, y - 0.42 * inch, colw, 0.42 * inch, stroke=1, fill=0)
    c.setFillColorRGB(*MUTED)
    c.setFont("Helvetica", 7)
    c.drawString(M + 0.08 * inch, y - 0.15 * inch, "THE HOUR")
    c.setFillColorRGB(*RULE)
    c.setFont("Helvetica-Bold", 17)
    c.drawString(M + 0.60 * inch, y - 0.34 * inch, "_____ : _____")

    c.setStrokeColorRGB(*CHAR)
    c.rect(rx, y - 0.42 * inch, colw, 0.42 * inch, stroke=1, fill=0)
    c.setFillColorRGB(*MUTED)
    c.setFont("Helvetica", 7)
    c.drawString(rx + 0.08 * inch, y - 0.15 * inch, "SHORT RESTS TAKEN (1 hr each — off the clock)")

    ly = y - 0.64 * inch

    # ---- WHAT THEY'VE LEARNED (left)
    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M, ly, "WHAT THEY'VE LEARNED")
    c.setFillColorRGB(*MUTED)
    c.setFont("Helvetica-Oblique", 6.6)
    c.drawRightString(M + colw, ly, "don't re-reveal · don't contradict")
    ly -= 0.21 * inch
    for label, pre in [
        ("Elizabeth and Rowan were brought here", True),
        ("Elizabeth died of the fever, days after", False),
        ("Rowan was cleaned up and sold on", False),
        ("The buyer's name — BARNEY SOOT", False),
        ("The true count: twenty men", False),
        ("Six are Ironwake's, not Vaskar's", False),
        ("The masked one is branded — a Penitent", False),
        ("…and the first Dol team's only survivor", False),
        ("Cobb kept the ledger · is being tortured for it", False),
        ("Durgan can switch Mott off", False),
        ("What Vaskar is (Corvant's account)", False),
        ("The hooded buyers took all the women", True),
        ("Denrick sold the tunnel and trapped it", False),
    ]:
        checkbox(c, M, ly, label, size=7.8)
        if pre:
            c.setFillColorRGB(*MUTED)
            c.setFont("Helvetica-Oblique", 6.2)
            c.drawRightString(M + colw, ly, "known in S1")
        ly -= 0.183 * inch
    ly -= 0.04 * inch
    ly = ruled(c, M, ly, colw, 4, gap=0.195)

    # ---- YSABEL'S FIVE — JOBS (left)
    ly -= 0.16 * inch
    c.setFillColorRGB(*VIOLET)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M, ly, "YSABEL'S FIVE — WHAT THEY'VE BEEN TOLD TO DO")
    ly -= 0.14 * inch
    c.setFillColorRGB(*OX)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(M, ly, "No job = they break the moment one of them drops.")
    ly -= 0.20 * inch
    for name in ["Perrin Aske", "Dov Brandt", "Symon Reeve", "Cael Ordway", "Mina Dorn"]:
        c.setFillColorRGB(*INK)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(M, ly, name)
        c.setStrokeColorRGB(*RULE)
        c.setLineWidth(0.5)
        c.line(M + 1.05 * inch, ly - 0.02 * inch, M + colw, ly - 0.02 * inch)
        ly -= 0.215 * inch

    # ---- RESOURCES (left)
    ly -= 0.14 * inch
    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M, ly, "RESOURCES — no long rest tonight")
    ly -= 0.19 * inch
    c.setFillColorRGB(*MUTED)
    c.setFont("Helvetica", 6.6)
    c.drawString(M + 1.05 * inch, ly, "HP")
    c.drawString(M + 1.70 * inch, ly, "SLOTS")
    c.drawString(M + 2.45 * inch, ly, "OTHER")
    ly -= 0.13 * inch
    for name in ["JonLief", "Wolfram", "Virgil", "Luthien", "Gimble"]:
        c.setFillColorRGB(*INK)
        c.setFont("Helvetica", 8)
        c.drawString(M, ly, name)
        c.setStrokeColorRGB(*RULE)
        c.setLineWidth(0.5)
        for sx, sw in [(1.05, 0.55), (1.70, 0.65), (2.45, colw / inch - 2.45)]:
            c.line(M + sx * inch, ly - 0.02 * inch, M + (sx + sw) * inch, ly - 0.02 * inch)
        ly -= 0.205 * inch
    c.setFillColorRGB(*OX)
    c.setFont("Helvetica-Bold", 7.4)
    c.drawString(M, ly, "Wolfram's Lay on Hands: ______ / 15 — does NOT come back tonight")

    # ================= RIGHT COLUMN =================
    fy = y - 0.64 * inch
    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(rx, fy, "FLAGS")
    c.setFillColorRGB(*MUTED)
    c.setFont("Helvetica-Oblique", 6.6)
    c.drawRightString(rx + colw, fy, "state, not knowledge")
    fy -= 0.21 * inch
    for label in [
        "Cover still intact",
        "Vaskar met — he has counted them",
        "Anselm has SEEN Wolfram",
        "Anselm SPOKEN to",
        "Denrick talked to · believed?",
        "Deep Cages entered",
        "Durgan spoken to · kindness shown to Mott",
        "Gimble freed / unmasked",
        "Cobb reached ALIVE",
        "Working ledger taken from the office",
        "Armory opened",
        "Talwyn Ceth freed (the ledger backup)",
        "Second ledger STILL WITH THE PARTY",
        "Revolt has fired",
    ]:
        checkbox(c, rx, fy, label, size=7.8)
        fy -= 0.183 * inch

    # Ysabel conditions
    fy -= 0.16 * inch
    c.setFillColorRGB(*VIOLET)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(rx, fy, "YSABEL IS DETAINED ONLY IF ALL THREE")
    fy -= 0.21 * inch
    for label in ["The match happened", "Revolt put down, or never fired", "Party never engaged Vaskar"]:
        checkbox(c, rx, fy, label, size=7.8)
        fy -= 0.183 * inch
    c.setFillColorRGB(*OX)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(rx, fy, "Break any ONE and she walks.")
    fy -= 0.30 * inch

    # Mott
    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(rx, fy, "MOTT — decides the TRIAL, not the match")
    fy -= 0.21 * inch
    for label in ["Still Ironwake's champion", "Dead", "Hurt — can't fight in two days", "Gone with Durgan"]:
        checkbox(c, rx, fy, label, size=7.8)
        fy -= 0.183 * inch

    # guards down
    fy -= 0.16 * inch
    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(rx, fy, "GUARDS DOWN")
    fy -= 0.23 * inch
    c.setFillColorRGB(*OX)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawString(rx, fy, "FEN ×14")
    c.setStrokeColorRGB(*MUTED)
    c.setLineWidth(0.7)
    for i in range(14):
        c.rect(rx + 0.62 * inch + i * 0.145 * inch, fy - 0.025 * inch, 0.095 * inch, 0.095 * inch, stroke=1, fill=0)
    fy -= 0.23 * inch
    c.setFillColorRGB(*STEEL)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawString(rx, fy, "IRONWAKE ×6")
    for i in range(6):
        c.rect(rx + 0.90 * inch + i * 0.145 * inch, fy - 0.025 * inch, 0.095 * inch, 0.095 * inch, stroke=1, fill=0)
    fy -= 0.28 * inch
    c.setFillColorRGB(*OX)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawString(rx, fy, "NEVER MORE THAN 5 ACTING IN A ROUND.")

    fy -= 0.30 * inch
    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(rx, fy, "NOTES")
    ruled(c, rx, fy - 0.22 * inch, colw, 7, gap=0.215)


# ------------------------------------------------------------ 3-4. read-aloud
BLOCKS = [
    ("The yard, walking in", "5:30 · they are already here", OX,
     "The yard is muddy underfoot and the air sits heavy and humid and full of the smell of a great many "
     "unwashed people who are frightened all of the time. Guards shouting across each other. Hammering from "
     "the middle of the yard. And under it, a low sound that takes a moment to identify as a man.",
     "Then: the drunk guard at the post, and the escort saying not to trouble themselves — he's a half-orc, they take a beating."),

    ("The whipping post", "Marek Osu is the one taking it", OX,
     "The guard is drunk and he is not very good at this, which is somehow worse. He is taking his time "
     "because he keeps losing his place. Three men are on their knees in the mud with their heads held up so "
     "they have to watch. One of them has stopped watching. He is looking at you.",
     "Then: the cover costs something to keep. Let them not intervene, and let that sit."),

    ("The Chainmaster's Hall — Vaskar receives them", "~6:00 · Cobb is in this building", OX,
     "He does not get up, and he is not rude about it. He looks at Lady Ysabel the way a man looks at a "
     "column of figures that has come out right. 'My lady. You'll forgive the state of the place — we have a "
     "guest of Lord Ironwake's and the whole fen has lost its head over it.' A pause, exactly long enough. "
     "'You've brought rather a lot of people to look at cloth-hands.'",
     "Then: ten minutes of courteous lying. He is counting them. Somewhere behind a door there is a chair leg, or a cough, or breathing that isn't one of theirs."),

    ("Old Cobb", "gone at 7:45 if nobody reaches him", OX,
     "The old man in the chair does not look up when the door opens. He has learned what it means when the "
     "door opens. His hands are wrong. When he finally does lift his head, one eye is swollen closed and the "
     "other is trying very hard to focus on you, and what comes out of him is not a plea. It's a "
     "professional's habit, forty years deep: 'I've told him. The record would indicate — there is no record. "
     "There's no record left to give him.'",
     "He is telling the truth. He gave the book away and does not know where it went. Vaskar cannot tell the difference between a man protecting a secret and a man who has none."),

    ("The Pens — JonLief's scene", "give him the room, slow it down", GREEN,
     "Stone, and dark, and forty years of men. They come to the bars when they hear the door — not fast. "
     "Nobody in here moves fast. Someone asks if you're the buyer. Someone else tells him to shut up. And "
     "then, from the back, where it's darkest, an old voice that has clearly asked this before and stopped "
     "expecting an answer: 'Is there anyone out there still looking for us?'",
     "Then: nobody here knows about the woman and the boy. Make him ask five times. Empty cell at the end, Investigation DC 12 → the hollow under the flagstone, and the dust disturbed within the month."),

    ("Anselm knows him", "near-miss FIRST, then the real thing", GREEN,
     "The old man at the back of the cage has not moved since you came in. Now he stands, and he takes his "
     "time about it, and he looks at you the way a man looks at a debt he never expected to collect. "
     "'Eisenherz,' he says. Not a question. 'I gave a statement about you to a clerk in the Citadel. He never "
     "wrote it down.'",
     "NO Insight roll — tell the table plainly this man is telling the truth. Then he gives the true count: twenty. Fourteen and six. Then he asks Wolfram: 'Who's in charge of you?'"),

    ("The Deep Cages", "1 Fen Guard outside · 2 Ironwake inside", CHAR,
     "Two cells. In the first, a dwarf sits with his back to the bars, watching. In the second — and it takes "
     "a moment to understand the scale of what you are seeing — a man the size of a cart horse is sitting "
     "cross-legged in the straw, holding a bundle of twine and stalks in the shape of a doll, and he is "
     "walking it very carefully along his own knee.",
     "Durgan speaks first, and it's a warning: 'Don't shout. He's having a good day.'"),

    ("The masked one", "the reveal is the SHOULDER, not the face", CHAR,
     "The second cell holds something much smaller. It is sitting cross-legged in the exact centre of the "
     "floor, in rags, with a riveted iron mask over the whole of its head, and it is not asleep — it is facing "
     "the door, and it was facing the door before you opened it. It does not move when the light hits it. One "
     "of the guards behind you laughs and says something about not bothering to learn its name.",
     "Rags, one bare shoulder, a sun with a single tear. Let a PC find it. The moment they see it, the cover is over — and that is a good way for it to end."),

    ("Sundown — the ring", "8:00 · Anselm's signal lands here", CHAR,
     "They've dragged the fence into a circle in the middle of the yard, and every man in Bramblefen who "
     "isn't chained is leaning on it. The masked man is walked out. He doesn't struggle. He doesn't look at "
     "anyone. And then the doors of the Deep Cages open, and the crowd makes a sound you've heard before at "
     "fairs and hangings, and the ground moves.",
     "Sequence the minute: match starts → Anselm signals → the yard goes up → THEN the outcome and Ysabel. One at a time, and let the party act between each."),
]


def page_readaloud(c, blocks, part):
    y = page_title(c, "Read-Aloud — in running order", "Session 2 · part %d" % part)
    w = PW - 2 * M
    for title, note, col, quote, then in blocks:
        c.setFillColorRGB(*col)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(M, y, title)
        c.setFillColorRGB(*MUTED)
        c.setFont("Helvetica-Oblique", 7.4)
        c.drawRightString(PW - M, y, note)
        y -= 0.10 * inch

        lines = wrap(c, quote, "Helvetica-Oblique", 9.2, w - 0.34 * inch)
        bh = len(lines) * 0.152 * inch + 0.20 * inch
        c.setFillColorRGB(0.965, 0.955, 0.925)
        c.setStrokeColorRGB(*col)
        c.setLineWidth(0.8)
        c.rect(M, y - bh, w, bh, stroke=1, fill=1)
        c.setFillColorRGB(*col)
        c.rect(M, y - bh, 0.055 * inch, bh, stroke=0, fill=1)

        ty = y - 0.18 * inch
        c.setFillColorRGB(*INK)
        for ln in lines:
            c.setFont("Helvetica-Oblique", 9.2)
            c.drawString(M + 0.20 * inch, ty, ln)
            ty -= 0.152 * inch
        y -= bh + 0.11 * inch
        y = para(c, M + 0.06 * inch, y, then, w - 0.12 * inch, size=8.0, lead=0.125, colour=MUTED)
        y -= 0.19 * inch


# ------------------------------------------------------------------- 5. names
EIGHTEEN = [
    ("1", "Anselm Vogt", "Term", "Pens", "Westfield sheriff. Leader. Knows Wolfram's crest."),
    ("2", "Haskel Mundt", "Term", "Pens", "Smith, huge hands, forty words a day. Anselm's second."),
    ("3", "Bertie Kranz", "Term", "Pens", "22, loud, aches to fight. Anselm fears losing him."),
    ("4", "Corvant Hale", "Term", "Pens", "Sellsword. Tried this a year ago. WATCHED VASKAR KILL FOUR MEN."),
    ("5", "Ondrej Fisk", "Term", "Pens", "Fen fisherman. Knows the water."),
    ("6", "Rusk", "Term", "Pens", "No surname, no speech. Does not understand 'free.'"),
    ("7", "Mirek Vole", "Term", "Post", "Farmer. Weeps quietly and constantly."),
    ("8", "Wendel Crook", "Term", "Post", "Was a guard here until 8 weeks ago. The moral bill."),
    ("9", "Ivo Lantz", "Term", "Post", "16. His dead father's debt. Under the lash."),
    ("10", "Talwyn Ceth", "Stock", "Pens", "Scribe. CAN COPY A LEDGER FROM MEMORY — protect him."),
    ("11", "Kesh Vanner", "Stock", "Auction", "Navigator, 40 yrs at sea. Remembers buyers asking for artists."),
    ("12", "Yarel Stoke", "Stock", "Pens", "Pit fighter. Count him as three men. Wants Vaskar."),
    ("13", "Marek Osu", "Stock", "Post", "Temple servant. Still prays — to Azerai."),
    ("14", "Sabbath Ivry", "Stock", "Auction", "19, tiefling. Branded twice. Furious, reckless."),
    ("15", "Tobrun Ashfoot", "Stock", "Auction", "Halfling housebreaker. Opens most things with a bent nail."),
    ("16", "Bosk Dunmar", "Stock", "Pens", "Dwarf mason. Built two of these walls as a free man."),
    ("17", "Nim Tarrow", "Stock", "Pens", "Gnome tinker. Deaf one ear — will miss a whispered signal."),
    ("18", "Ghesh Saltscale", "Stock", "Pens", "Lizardfolk, fen-born. Everyone keeps a space around him."),
]

HOUSEHOLD = [
    ("Perrin Aske", "54", "Steward. Won't run. Won't leave without Ysabel."),
    ("Dov Brandt", "31", "HER PROPERTY — Terms, 3 yrs left. Sold on this block. Remembers Cobb."),
    ("Symon Reeve", "26", "Driver. The carts — how 18 freed men leave the fen."),
    ("Cael Ordway", "18", "Terrified. If you need one death to land, it's him."),
    ("Mina Dorn", "40s", "Lady-in-waiting. Bandages. Kind to Erwana unprompted."),
]

KEY = [
    ("Vaskar", OX, "Calm, courteous, transactional. Prices everything. Never raises his voice, never rages, never dies for Ironwake."),
    ("Old Cobb", OX, "Precise, hedging, clerkish. 'The record would indicate.' Qualifies everything, even now. Needs to confess."),
    ("Denrick", OX, "Ingratiating, twitchy. 'Friend.' 'Of course.' Smooth on big lies, fumbles small details. Insight DC 13."),
    ("Anselm", GREEN, "Slow, level, unhurried. Says a thing once. Produces an exact number mid-scene. Never pleads."),
    ("Durgan", CHAR, "Low, economical, dry. A rare joke means he's decided you're safe. Folds instantly if Mott is threatened."),
    ("Mott", CHAR, "Few words, child's cadence. Names things he likes. The straw doll. Never raises a hand to Durgan."),
    ("Ysabel", VIOLET, "Fraying nobility. On slavery: bewildered, then the Church, then cold. Never cruel, never converted by one roll."),
]


def page_names(c):
    y = page_title(c, "Names at a Glance", "somebody asks — answer in one second")
    w = PW - 2 * M

    c.setFillColorRGB(*GREEN)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(M, y, "THE EIGHTEEN")
    c.setFillColorRGB(*MUTED)
    c.setFont("Helvetica", 7)
    c.drawRightString(PW - M, y, "9 Term (human) · 9 Stock (non-human)")
    y -= 0.20 * inch
    for num, name, kind, where, note in EIGHTEEN:
        c.setFillColorRGB(*MUTED)
        c.setFont("Helvetica", 7)
        c.drawString(M, y, num)
        c.setFillColorRGB(*INK)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(M + 0.20 * inch, y, name)
        c.setFillColorRGB(*(GREEN if kind == "Term" else VIOLET))
        c.setFont("Helvetica-Bold", 6.6)
        c.drawString(M + 1.42 * inch, y, kind.upper())
        c.setFillColorRGB(*MUTED)
        c.setFont("Helvetica", 6.6)
        c.drawString(M + 1.86 * inch, y, where)
        c.setFillColorRGB(*INK)
        c.setFont("Helvetica", 7.6)
        c.drawString(M + 2.42 * inch, y, note)
        y -= 0.168 * inch

    y -= 0.10 * inch
    c.setFillColorRGB(*OX)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawString(M, y, "DEATHS, IN THIS ORDER — guards go for the slow, the small, the already bleeding")
    y -= 0.15 * inch
    c.setFillColorRGB(*INK)
    c.setFont("Helvetica", 7.4)
    c.drawString(M, y, "Ivo → Mirek → Nim → Sabbath → Rusk → Bertie → Marek → Ondrej → Bosk → Wendel → Kesh → Tobrun → Ghesh → Talwyn → Corvant → Yarel → Haskel → Anselm")
    y -= 0.34 * inch

    c.setFillColorRGB(*VIOLET)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(M, y, "YSABEL'S FIVE — inside the wall with the party")
    y -= 0.20 * inch
    for name, age, note in HOUSEHOLD:
        c.setFillColorRGB(*INK)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(M, y, name)
        c.setFillColorRGB(*MUTED)
        c.setFont("Helvetica", 6.8)
        c.drawString(M + 1.15 * inch, y, age)
        c.setFillColorRGB(*INK)
        c.setFont("Helvetica", 7.6)
        c.drawString(M + 1.50 * inch, y, note)
        y -= 0.175 * inch
    c.setFillColorRGB(*MUTED)
    c.setFont("Helvetica-Oblique", 7.2)
    c.drawString(M, y, "AC 13 · HP 9 · shortsword +2 (1d6). One drops and the rest break, unless a PC gave them a job.")
    y -= 0.36 * inch

    c.setFillColorRGB(*CHAR)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(M, y, "VOICES — one line each")
    y -= 0.20 * inch
    for name, col, note in KEY:
        c.setFillColorRGB(*col)
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(M, y, name)
        y = para(c, M + 0.85 * inch, y, note, w - 0.85 * inch, size=7.6, lead=0.125)
        y -= 0.045 * inch


# ---------------------------------------------------------------------- build
def build():
    c = canvas.Canvas(OUT, pagesize=letter)
    page_clock(c); c.showPage()
    page_board(c); c.showPage()
    page_readaloud(c, BLOCKS[:5], 1); c.showPage()
    page_readaloud(c, BLOCKS[5:], 2); c.showPage()
    page_names(c); c.showPage()
    c.save()
    return OUT


if __name__ == "__main__":
    print("Wrote", build())
