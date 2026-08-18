#!/usr/bin/env python3
"""
Bramblefen stat cards — Chapter 7.

Generates print-ready poker-sized (2.5" x 3.5") stat cards, 9 per US Letter page,
with crop marks for cutting.

ART
---
Drop image files in an "art" folder next to this script, named:

    art/vaskar.jpg        art/juggernaut.jpg     art/ironwake_thug.jpg
    art/fen_guard.jpg     art/durgan.jpg         art/anselm.jpg
    art/denrick.jpg       art/yarel.jpg          art/slave.jpg
    art/servant.jpg       art/ysabel.jpg

.png works too. Any image found is cropped to fill the art panel.
Anything missing falls back to a generated emblem, so this always produces a PDF.

Run:  python3 make_stat_cards.py
Out:  Bramblefen Stat Cards.pdf
"""

import os, math, sys

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.utils import ImageReader
    from PIL import Image, ImageDraw
except ModuleNotFoundError as missing:
    sys.exit(
        "\nMissing Python library: %s\n"
        "\nThis script needs 'reportlab' and 'pillow'. Install them with:\n"
        "\n    pip3 install reportlab pillow\n"
        "\nIf that fails with \"externally-managed-environment\", use:\n"
        "\n    pip3 install --user reportlab pillow\n"
        "\nThen run this script again.\n" % missing.name
    )

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "art")
OUT = os.path.join(HERE, "Bramblefen Stat Cards.pdf")

CARD_W, CARD_H = 2.5 * inch, 3.5 * inch
PAGE_W, PAGE_H = letter
COLS, ROWS = 3, 3
MARGIN_X = (PAGE_W - COLS * CARD_W) / 2
MARGIN_Y = (PAGE_H - ROWS * CARD_H) / 2

INK = (0.12, 0.11, 0.10)
MUTED = (0.42, 0.40, 0.38)
PAPER = (0.98, 0.97, 0.94)

FACTION = {
    "bramblefen": (0.42, 0.13, 0.11),   # oxblood
    "ironwake":   (0.16, 0.24, 0.34),   # cold steel
    "beast":      (0.30, 0.26, 0.22),   # iron grey
    "captive":    (0.24, 0.34, 0.24),   # green
    "household":  (0.32, 0.22, 0.36),   # violet
    "reference":  (0.18, 0.18, 0.18),   # charcoal
}


# ----------------------------------------------------------------- emblem art
def emblem(key, colour, size=(600, 380)):
    """Generated fallback art: a bold flat emblem on a textured field."""
    w, h = size
    r, g, b = [int(c * 255) for c in colour]
    img = Image.new("RGB", (w, h), (r, g, b))
    d = ImageDraw.Draw(img)

    # subtle diagonal hatching
    for x in range(-h, w, 14):
        d.line([(x, h), (x + h, 0)], fill=(min(r + 14, 255), min(g + 14, 255), min(b + 14, 255)), width=3)

    cx, cy = w // 2, h // 2
    pale = (238, 232, 220)
    S = 96

    def ring(rad, wd=7):
        d.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], outline=pale, width=wd)

    if key == "fen_guard":                     # crossed spears
        for sgn in (1, -1):
            d.line([(cx - sgn * S, cy + S), (cx + sgn * S, cy - S)], fill=pale, width=11)
            d.polygon([(cx + sgn * S, cy - S), (cx + sgn * S - sgn * 26, cy - S + 10),
                       (cx + sgn * S - sgn * 10, cy - S + 30)], fill=pale)
    elif key == "ironwake_thug":               # portcullis
        for i in range(-2, 3):
            d.line([(cx + i * 34, cy - S), (cx + i * 34, cy + S)], fill=pale, width=9)
        for j in (-1, 0, 1):
            d.line([(cx - S - 10, cy + j * 52), (cx + S + 10, cy + j * 52)], fill=pale, width=9)
    elif key == "vaskar":                      # chain links
        for i in (-1, 0, 1):
            d.ellipse([cx + i * 70 - 44, cy - 30, cx + i * 70 + 44, cy + 30], outline=pale, width=12)
    elif key == "juggernaut":                  # fist / broken chain
        d.rounded_rectangle([cx - 78, cy - 58, cx + 78, cy + 58], radius=26, fill=pale)
        for i in range(4):
            d.line([(cx - 60 + i * 40, cy - 58), (cx - 60 + i * 40, cy + 10)], fill=(r, g, b), width=8)
    elif key == "durgan":                      # hammer
        d.rectangle([cx - 16, cy - 20, cx + 16, cy + S], fill=pale)
        d.rounded_rectangle([cx - 84, cy - 76, cx + 84, cy - 16], radius=12, fill=pale)
    elif key == "anselm":                      # broken shackle
        d.arc([cx - S, cy - S, cx + S, cy + S], start=200, end=520, fill=pale, width=16)
        d.line([(cx - 30, cy - 96), (cx + 34, cy - 60)], fill=(r, g, b), width=14)
    elif key == "denrick":                     # two-faced mask
        d.ellipse([cx - 74, cy - 84, cx + 74, cy + 84], outline=pale, width=10)
        d.line([(cx, cy - 84), (cx, cy + 84)], fill=pale, width=8)
        d.ellipse([cx - 46, cy - 34, cx - 22, cy - 10], fill=pale)
        d.arc([cx + 18, cy - 40, cx + 52, cy - 6], start=0, end=180, fill=pale, width=8)
    elif key == "yarel":                       # broken collar + tusks
        d.arc([cx - 82, cy - 62, cx + 82, cy + 62], start=150, end=390, fill=pale, width=18)
        d.polygon([(cx - 40, cy + 40), (cx - 22, cy + 96), (cx - 6, cy + 40)], fill=pale)
        d.polygon([(cx + 40, cy + 40), (cx + 22, cy + 96), (cx + 6, cy + 40)], fill=pale)
    elif key == "slave":                       # collar
        ring(72, 20)
        d.rectangle([cx - 16, cy - 96, cx + 16, cy - 56], fill=pale)
    elif key == "servant":                     # household knot
        ring(46, 9)
        d.ellipse([cx - 86, cy - 24, cx - 8, cy + 54], outline=pale, width=9)
        d.ellipse([cx + 8, cy - 24, cx + 86, cy + 54], outline=pale, width=9)
    elif key == "ysabel":                      # spindle and thread
        d.line([(cx, cy - S), (cx, cy + S)], fill=pale, width=10)
        for i in range(5):
            d.ellipse([cx - 54 + i * 4, cy - 46 + i * 16, cx + 54 - i * 4, cy - 14 + i * 16],
                      outline=pale, width=5)
    else:                                      # reference: sun and tear
        ring(52, 10)
        for i in range(12):
            a = i * math.pi / 6
            d.line([(cx + math.cos(a) * 66, cy + math.sin(a) * 66),
                    (cx + math.cos(a) * 92, cy + math.sin(a) * 92)], fill=pale, width=7)
        d.polygon([(cx, cy + 26), (cx - 16, cy + 66), (cx + 16, cy + 66)], fill=pale)

    # vignette
    dark = Image.new("L", (w, h), 0)
    ImageDraw.Draw(dark).rectangle([6, 6, w - 6, h - 6], fill=90)
    img = Image.composite(img, Image.new("RGB", (w, h), (0, 0, 0)), dark.point(lambda v: 255 - (255 - v) // 3))
    return img


def art_for(key, colour, panel_px=(600, 380)):
    for ext in (".jpg", ".jpeg", ".png", ".JPG", ".PNG"):
        p = os.path.join(ART, key + ext)
        if os.path.exists(p):
            im = Image.open(p).convert("RGB")
            tw, th = panel_px
            scale = max(tw / im.width, th / im.height)
            im = im.resize((max(1, round(im.width * scale)), max(1, round(im.height * scale))), Image.LANCZOS)
            left, top = (im.width - tw) // 2, (im.height - th) // 2
            return im.crop((left, top, left + tw, top + th)), True
    return emblem(key, colour, panel_px), False


# ----------------------------------------------------------------- text utils
def wrap(c, text, font, size, maxw):
    c.setFont(font, size)
    out, line = [], ""
    for word in text.split():
        t = (line + " " + word).strip()
        if c.stringWidth(t, font, size) <= maxw:
            line = t
        else:
            if line:
                out.append(line)
            line = word
    if line:
        out.append(line)
    return out


# ----------------------------------------------------------------- card draw
def draw_card(c, x, y, card):
    col = FACTION[card["faction"]]
    P = 0.11 * inch

    c.saveState()
    c.setFillColorRGB(*PAPER)
    c.setStrokeColorRGB(*MUTED)
    c.setLineWidth(0.6)
    c.roundRect(x, y, CARD_W, CARD_H, 0.09 * inch, stroke=1, fill=1)

    # header
    hh = 0.40 * inch
    c.setFillColorRGB(*col)
    c.roundRect(x, y + CARD_H - hh, CARD_W, hh, 0.09 * inch, stroke=0, fill=1)
    c.rect(x, y + CARD_H - hh, CARD_W, hh * 0.45, stroke=0, fill=1)

    c.setFillColorRGB(1, 1, 1)
    name, fs = card["name"], 11.5
    while c.stringWidth(name, "Helvetica-Bold", fs) > CARD_W - 2 * P and fs > 7:
        fs -= 0.5
    c.setFont("Helvetica-Bold", fs)
    c.drawString(x + P, y + CARD_H - hh + 0.185 * inch, name)
    if card.get("tag"):
        c.setFont("Helvetica", 5.6)
        tag = card["tag"]
        while c.stringWidth(tag, "Helvetica", 5.6) > CARD_W - 2 * P and len(tag) > 8:
            tag = tag[:-1]
        c.drawString(x + P, y + CARD_H - hh + 0.062 * inch, tag)

    # art panel
    ah = 1.00 * inch
    ay = y + CARD_H - hh - ah
    im, real = art_for(card["key"], col, (600, 380))
    c.drawImage(ImageReader(im), x, ay, CARD_W, ah, mask=None)
    if not real:
        c.setFillColorRGB(1, 1, 1)
        c.setFont("Helvetica-Oblique", 5.2)
        c.drawRightString(x + CARD_W - 0.06 * inch, ay + 0.05 * inch, "art/%s.jpg" % card["key"])

    # stat strip
    sh = 0.30 * inch
    sy = ay - sh
    c.setFillColorRGB(*col)
    c.rect(x, sy, CARD_W, sh, stroke=0, fill=1)
    boxes = card["stats"]
    bw = CARD_W / len(boxes)
    for i, (label, val) in enumerate(boxes):
        bx = x + i * bw
        if i:
            c.setStrokeColorRGB(1, 1, 1)
            c.setLineWidth(0.4)
            c.line(bx, sy + 0.035 * inch, bx, sy + sh - 0.035 * inch)
        c.setFillColorRGB(1, 1, 1)
        c.setFont("Helvetica", 5.0)
        c.drawCentredString(bx + bw / 2, sy + sh - 0.105 * inch, label)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(bx + bw / 2, sy + 0.055 * inch, val)

    # body
    ty = sy - 0.125 * inch
    maxw = CARD_W - 2 * P
    for kind, text in card["body"]:
        if ty < y + 0.20 * inch:
            break
        if kind == "h":
            c.setFillColorRGB(*col)
            c.setFont("Helvetica-Bold", 6.0)
            c.drawString(x + P, ty, text.upper())
            c.setStrokeColorRGB(*col)
            c.setLineWidth(0.4)
            tw = c.stringWidth(text.upper(), "Helvetica-Bold", 6.0)
            c.line(x + P + tw + 3, ty + 2, x + CARD_W - P, ty + 2)
            ty -= 0.105 * inch
        else:
            bold = kind == "b"
            font = "Helvetica-Bold" if bold else "Helvetica"
            c.setFillColorRGB(*(INK if not bold else col))
            for ln in wrap(c, text, font, 6.1, maxw):
                if ty < y + 0.20 * inch:
                    break
                c.setFont(font, 6.1)
                c.drawString(x + P, ty, ln)
                ty -= 0.088 * inch
            ty -= 0.022 * inch

    # tracker
    if card.get("track"):
        c.setFillColorRGB(*MUTED)
        c.setFont("Helvetica", 5.0)
        c.drawString(x + P, y + 0.085 * inch, "HP")
        c.setStrokeColorRGB(*MUTED)
        c.setLineWidth(0.5)
        n = card["track"]
        avail = CARD_W - 2 * P - 0.15 * inch
        gap = avail / n
        bw2 = gap - 0.035 * inch
        for i in range(n):
            lx = x + P + 0.15 * inch + i * gap
            c.rect(lx, y + 0.045 * inch, bw2, 0.115 * inch, stroke=1, fill=0)

    c.restoreState()


def crop_marks(c):
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(0.3)
    m = 0.11 * inch
    for i in range(COLS + 1):
        gx = MARGIN_X + i * CARD_W
        c.line(gx, MARGIN_Y - m, gx, MARGIN_Y)
        c.line(gx, MARGIN_Y + ROWS * CARD_H, gx, MARGIN_Y + ROWS * CARD_H + m)
    for j in range(ROWS + 1):
        gy = MARGIN_Y + j * CARD_H
        c.line(MARGIN_X - m, gy, MARGIN_X, gy)
        c.line(MARGIN_X + COLS * CARD_W, gy, MARGIN_X + COLS * CARD_W + m, gy)


def build(cards):
    c = canvas.Canvas(OUT, pagesize=letter)
    for i, card in enumerate(cards):
        slot = i % (COLS * ROWS)
        if slot == 0:
            if i:
                c.showPage()
            crop_marks(c)
        r, col_i = divmod(slot, COLS)
        draw_card(c, MARGIN_X + col_i * CARD_W,
                  MARGIN_Y + (ROWS - 1 - r) * CARD_H, card)
    c.save()
    return OUT


# ----------------------------------------------------------------- the cards
H, T, B = "h", "t", "b"

CARDS = [
    dict(key="vaskar", name="Vaskar the Brand", tag="CR 5 · TUNED FOR LVL 3",
         faction="bramblefen", track=1,
         stats=[("AC", "16"), ("HP", "80"), ("SPD", "30"), ("PP", "18")],
         body=[(H, "Multiattack"),
               (T, "Two chain, or one chain + branding iron."),
               (B, "Spiked Chain +7 · 2d6+4 · reach 10"),
               (T, "DC 15 STR or pulled 5 ft and knocked prone."),
               (B, "Branding Iron +7 · 1d8+4 + 2d6 fire"),
               (T, "DC 15 CON or Branded: he has advantage on you; you have disadvantage vs frightened."),
               (B, "Feed on Their Fear (5-6)"),
               (T, "10 temp HP + advantage, off anyone frightened, Branded, grappled or at 0."),
               (H, "Reaction"),
               (B, "Someone Else's Skin — 1/round"),
               (T, "Interpose a minion or captive within 5 ft. They take the hit instead.")]),

    dict(key="vaskar", name="Vaskar — How He Fights", tag="RUN HIM FROM THIS SIDE",
         faction="bramblefen",
         stats=[("SAVES", "S+7 C+6 W+5"), ("IMMUNE", "charm · fear")],
         body=[(B, "BLIND TO LOVE — the win condition"),
               (T, "First time each round someone Helps, shields an ally, or acts against their own interest: disadvantage on his next roll. SAY IT OUT LOUD every time."),
               (B, "Relentless (1/rest)"),
               (T, "Dropped to 0 but not killed outright: he is at 1 HP instead."),
               (B, "Expects Betrayal"),
               (T, "Cannot be surprised. Advantage on Insight to spot a lie."),
               (H, "Tactics"),
               (T, "Fights from behind people. Brands the front-liner early. NO Villain Actions at level 3 — give him 2 Thugs instead."),
               (B, "At ~25 HP he stops fighting."),
               (T, "Hostage, deal, run. He never dies on principle. Captured is worth an arc; dead is worth a strongbox.")]),

    dict(key="juggernaut", name="The Juggernaut · Mott", tag="CR 5 · SEE RAGE CLOCK",
         faction="beast", track=1,
         stats=[("AC", "14"), ("HP", "90"), ("SPD", "40"), ("PP", "9")],
         body=[(B, "Slam +8 · 2d8+7 · reach 10"),
               (T, "2d8+5 when not raging. DC 16 STR or prone."),
               (B, "Multiattack — Full Fury only"),
               (T, "Two Slams."),
               (B, "Ground Slam (5-6) — Full Fury only"),
               (T, "10 ft radius, DC 16 STR, 2d10 + prone. HITS HIS OWN SIDE. He does not aim it."),
               (B, "Fling — in place of one Slam"),
               (T, "DC 16 STR or grabbed (escape 16). Hurl 20 ft: 2d6 + prone, and 2d6 to whatever he lands on."),
               (H, "Always true"),
               (T, "Attacks the NEAREST creature, friend or foe. Never Durgan. Ignores a downed PC if someone nearer is standing. Reckless: advantage to hit, advantage against him.")]),

    dict(key="juggernaut", name="★ THE RAGE CLOCK", tag="COUNT ROUNDS FROM RAGE START",
         faction="beast",
         stats=[("FULL FURY", "1-4"), ("FLAGGING", "5-6"), ("BURNED OUT", "7+")],
         body=[(B, "1-4 FULL FURY"),
               (T, "Multiattack, Ground Slam, Fling. +2 damage. RESISTS bludg/pierc/slash. Speed 40."),
               (B, "5-6 FLAGGING"),
               (T, "One Slam only. No resistance. 2d8+5. DISADVANTAGE on attacks and STR. Speed 20."),
               (B, "7+ BURNED OUT"),
               (T, "Prone, incapacitated, speed 0, 2 exhaustion, down 1d4 rounds. Melee within 5 ft auto-crits."),
               (H, "Three ways to win"),
               (T, "Outlast him · reach Durgan · use the room and stay past 10 ft."),
               (B, "GRIEF-RAGE — if Durgan is hurt or killed"),
               (T, "Cannot be calmed by ANYONE. Full Fury lasts 6 rounds. He hunts whoever struck Durgan.")]),

    dict(key="durgan", name="Durgan Half-Ear", tag="THE OFF-SWITCH",
         faction="beast", track=1,
         stats=[("AC", "12"), ("HP", "16"), ("SPD", "25")],
         body=[(T, "No fighter. Commoner with a bad temper. The bond is the point, not the sword arm."),
               (B, "Calm the Beast (action)"),
               (T, "If Mott can SEE and HEAR him, the rage ends. Automatic — no roll. This is trust, not magic."),
               (B, "Rouse (action)"),
               (T, "Deliberately provokes the rage. Ironwake's men make him do it. He hates it."),
               (H, "Levers"),
               (T, "Threaten Mott and Durgan folds instantly. Offer them both a way out and he is yours for life."),
               (B, "Killing him is the worst outcome at the table."),
               (T, "Grief-Rage: nobody can stop Mott after that.")]),

    dict(key="anselm", name="Anselm Vogt", tag="CR 1/2 · REVOLT LEADER",
         faction="captive", track=1,
         stats=[("AC", "11"), ("HP", "26"), ("SPD", "30"), ("PP", "14")],
         body=[(T, "Starts with 1 level of EXHAUSTION — four months of short rations and the lash."),
               (B, "Improvised weapon +4 · 1d6+2"),
               (B, "Spear (if armed) +4 · 1d6+2"),
               (T, "1d8+2 two-handed, or thrown 20/60. Give him a spear and he is a sheriff again — play the difference."),
               (B, "Steady Hand"),
               (T, "Freed captives within 30 ft that see and hear him have advantage on saves vs frightened. If he falls they lose it instantly, and morale with it."),
               (H, "Reaction"),
               (B, "Pull Him Back"),
               (T, "Ally within 5 ft is hit: move them 5 ft and give +2 AC against that attack.")]),

    dict(key="denrick", name="Denrick", tag="CR 1/2 · THE TRUSTY",
         faction="bramblefen", track=1,
         stats=[("AC", "12"), ("HP", "22"), ("SPD", "30"), ("PP", "10")],
         body=[(B, "Cudgel +2 · 1d6"),
               (T, "He fights only when cornered, and badly."),
               (B, "Light Crossbow +3 · 1d8+1 · 80/320"),
               (T, "Prefers to shoot from behind somebody else."),
               (B, "Coward's Instinct"),
               (T, "The moment a fight turns or he drops below half, he surrenders, grovels or bolts — always with a fresh deal on his lips."),
               (H, "Reaction"),
               (B, "Shove the Weak — 1/round"),
               (T, "Shoves another creature within 5 ft into the blow. The attacker may redirect the hit."),
               (H, "Social"),
               (T, "Insight DC 13 to catch him. Deception +6.")]),

    dict(key="yarel", name="Yarel Stoke", tag="THE ONE WHO ACTUALLY FIGHTS",
         faction="captive", track=1,
         stats=[("AC", "13"), ("HP", "32"), ("SPD", "30")],
         body=[(T, "Half-orc. Pit fighter before the collar. In any revolt, count Yarel as three men."),
               (B, "Unarmed / improvised +5 · 1d6+3"),
               (B, "Any real weapon +5 · 1d8+3"),
               (B, "Relentless Endurance (1/day)"),
               (T, "Dropped to 0 but not killed outright: he is at 1 HP instead."),
               (B, "Savage Attacks"),
               (T, "On a melee crit, roll one extra weapon die."),
               (H, "Warning"),
               (T, "He wants Vaskar personally, which makes him very hard to aim. If the party needs a line held, he is not the one who will hold it.")]),

    dict(key="ysabel", name="Lady Ysabel Rochefort", tag="NONCOMBATANT",
         faction="household", track=1,
         stats=[("AC", "12"), ("HP", "9"), ("SPD", "30")],
         body=[(T, "She has never been in a fight and will not start one. If steel comes out she goes behind Perrin."),
               (B, "Dagger +2 · 1d4"),
               (T, "Only if cornered, and she will be bad at it."),
               (H, "If combat starts"),
               (T, "She is a hostage waiting to happen. Vaskar knows exactly what she is worth to Lord Ironwake."),
               (B, "She is carrying nothing the party needs."),
               (T, "The ledger is in the PARTY's hands until everyone is clear of the fen. That was the deal."),
               (H, "Remember"),
               (T, "Her mills run on bought labour. She owns Dov. She is being perfectly reasonable about all of it.")]),

    dict(key="fen_guard", name="Fen Guard", tag="CR 1/8 · 25 XP · 14 IN THE COMPOUND",
         faction="bramblefen", track=6,
         stats=[("AC", "16"), ("HP", "11"), ("SPD", "30"), ("PP", "12")],
         body=[(T, "Bramblefen's own. Underfed, unpaid, unenthusiastic. Brutes rather than soldiers."),
               (B, "Spear +3 · 1d6+1"),
               (T, "1d8+1 two-handed."),
               (B, "Light Crossbow +3 · 1d8+1 · 80/320"),
               (H, "Morale — use this"),
               (B, "When half of any group drops, the rest run."),
               (T, "For the gate, or for the Hall. LET THEM RUN — a fleeing guard raising the alarm is better drama than a corpse."),
               (H, "Posts"),
               (T, "3 gate · 4 yard · 2 arena fence · 1 whipping post · 1 auction yard · 1 Hall door · 1 Pens · 1 Deep Cages")]),

    dict(key="fen_guard", name="Fen Guard", tag="CR 1/8 · SECOND COPY",
         faction="bramblefen", track=6,
         stats=[("AC", "16"), ("HP", "11"), ("SPD", "30"), ("PP", "12")],
         body=[(B, "Spear +3 · 1d6+1 (1d8+1 two-handed)"),
               (B, "Light Crossbow +3 · 1d8+1 · 80/320"),
               (T, "Passive Perception 12."),
               (H, "Morale"),
               (T, "Half a group drops, the rest run. Let them."),
               (H, "Never more than 5 acting in a round"),
               (T, "All 20 at once is roughly 3,800 adjusted XP against a Deadly threshold of 1,600. Bramblefen is a sequence of small fights, not a battle.")]),

    dict(key="fen_guard", name="Fen Guard", tag="CR 1/8 · THIRD COPY",
         faction="bramblefen", track=6,
         stats=[("AC", "16"), ("HP", "11"), ("SPD", "30"), ("PP", "12")],
         body=[(B, "Spear +3 · 1d6+1 (1d8+1 two-handed)"),
               (B, "Light Crossbow +3 · 1d8+1 · 80/320"),
               (T, "Passive Perception 12."),
               (H, "Release valves if the alarm goes up"),
               (T, "1. Anselm fires early — 18 men hit the yard.  2. Mott gets loose — subtract 1-2 guards a round, add 1d4 slave deaths.  3. Guards break — they have no reason to die for Vaskar.")]),

    dict(key="ironwake_thug", name="Ironwake Thug", tag="CR 1/2 · 100 XP · 6 TOTAL",
         faction="ironwake", track=4,
         stats=[("AC", "11"), ("HP", "32"), ("SPD", "30"), ("PP", "10")],
         body=[(T, "Lord Ironwake's own, brought in with the giant. They do NOT take Vaskar's orders."),
               (B, "Multiattack: two Mace attacks"),
               (B, "Mace +4 · 1d6+2 each"),
               (B, "Heavy Crossbow +2 · 1d10 · 100/400"),
               (B, "Pack Tactics"),
               (T, "Advantage on attacks if an ally is within 5 ft of the target."),
               (H, "They do not break"),
               (T, "And they do not chase individuals. They hold the arena and the Hall door."),
               (H, "Positions"),
               (T, "4 asleep in the barracks · 2 INSIDE the Deep Cages on Mott's cell. Those two do not leave it, alarm or no alarm.")]),

    dict(key="ironwake_thug", name="Ironwake Thug", tag="CR 1/2 · SECOND COPY",
         faction="ironwake", track=4,
         stats=[("AC", "11"), ("HP", "32"), ("SPD", "30"), ("PP", "10")],
         body=[(B, "Multiattack: 2x Mace +4 · 1d6+2"),
               (B, "Heavy Crossbow +2 · 1d10 · 100/400"),
               (B, "Pack Tactics"),
               (H, "Encounter maths"),
               (T, "4 asleep, surprised: ~550 effective — Medium.  4 awake: 800 — Medium/Hard.  Deep Cages (1 Guard + 2 Thug): 450 — Easy/Medium.")]),

    dict(key="ironwake_thug", name="Ironwake Thug", tag="CR 1/2 · THIRD COPY",
         faction="ironwake", track=4,
         stats=[("AC", "11"), ("HP", "32"), ("SPD", "30"), ("PP", "10")],
         body=[(B, "Multiattack: 2x Mace +4 · 1d6+2"),
               (B, "Heavy Crossbow +2 · 1d10 · 100/400"),
               (B, "Pack Tactics"),
               (H, "Remember"),
               (T, "AC 11 is soft. They die to focused fire — the danger is the 4 mace attacks a round two of them put out, not their durability.")]),

    dict(key="slave", name="The Eighteen", tag="FREED CAPTIVE · GENERIC",
         faction="captive", track=6,
         stats=[("AC", "10"), ("HP", "7"), ("SPD", "30")],
         body=[(T, "Starved, unarmed, and mostly not fighters. Nine Stock, nine Terms."),
               (B, "Improvised +2 · 1d4"),
               (B, "Armed from the Armory +2 · 1d6"),
               (H, "Use them in blocks, not individually"),
               (T, "Roll one attack for every three men. Do not track them singly or the night will take four hours."),
               (H, "Deaths, in this order"),
               (T, "Ivo · Mirek · Nim · Sabbath · Rusk · Bertie · Marek · Ondrej · Bosk · Wendel · Kesh · Tobrun · Ghesh · Talwyn · Corvant · Yarel · Haskel · Anselm"),
               (B, "Protect Talwyn if you can."),
               (T, "He is the party's backup copy of the ledger.")]),

    dict(key="servant", name="Rochefort Servant", tag="YSABEL'S FIVE",
         faction="household", track=5,
         stats=[("AC", "13"), ("HP", "9"), ("SPD", "30")],
         body=[(T, "Perrin Aske 54 · Dov Brandt 31 · Symon Reeve 26 · Cael Ordway 18 · Mina Dorn 40s"),
               (B, "Shortsword +2 · 1d6"),
               (H, "Morale"),
               (B, "One drops and the rest break."),
               (T, "Unless a PC has given them a specific job — hold this door, mind the horses, get him on the cart."),
               (H, "Notes"),
               (T, "Perrin will not run and will not leave without Ysabel. Dov was sold on this block and knows the ground. Cael is the death that will land hardest — the party knew his name yesterday.")]),

    dict(key="reference", name="Bramblefen — At a Glance", tag="QUICK REFERENCE",
         faction="reference",
         stats=[("SUNDOWN", "8:00"), ("IN AT", "5:30"), ("MEN", "20")],
         body=[(B, "NEVER MORE THAN 5 ENEMIES ACTING PER ROUND."),
               (H, "The clock"),
               (T, "7:15 hammering stops, ring done, barracks empty out. 7:45 Vaskar leaves the office — COBB DIES. 8:00 the match, and Anselm's signal."),
               (H, "DCs"),
               (T, "Bribe gate 10 · Spot Denrick's lie 13 · Force Armory 15 (break 20) · Cobb's flagstone 12 · Vaskar chain STR 15 · Vaskar brand CON 15 · Mott STR 16 · Sneak the yard at sundown 13"),
               (H, "Party thresholds — 4 PCs, level 3"),
               (T, "Easy 300 · Medium 600 · Hard 900 · DEADLY 1600")]),
]

if __name__ == "__main__":
    os.makedirs(ART, exist_ok=True)
    path = build(CARDS)
    found = sum(1 for cd in {c["key"] for c in CARDS} if art_for(cd, (0, 0, 0))[1])
    print("Wrote %s — %d cards, %d pages." % (path, len(CARDS), math.ceil(len(CARDS) / 9)))
    print("Custom art found for %d of %d subjects. Drop files in %s to replace the rest."
          % (found, len({c['key'] for c in CARDS}), ART))
