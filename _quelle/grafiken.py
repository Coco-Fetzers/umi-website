"""Grafiken (SVG) und Bildplätze.

Bildplätze: assets/img/bild-<name>.webp, immer mit dem Hinweis "Symbolbild".
Fehlt eine Datei, bleibt der Farbverlauf. Startseiten-Hero: bild-hero.webp
"""
import os
import rahmen as R

INK, BROWN, CLAY, PEACH, TERRA, SAND = "#190301", "#573B24", "#E08D5F", "#FFB57F", "#B14F25", "#ECE8D7"


ALT = {
    "apherese": "Frau im Ledersessel während einer Apherese, Pfleger am Gerät", "ankommen": "Frau geht durch einen hellen Empfang",
    "gespraech": "Ärztin im Gespräch mit einem Patienten", "labor": "Pfleger mit Blutproben im Labor", "warten": "Mann mit Tee im Ledersessel am Fenster",
    "blutprobe": "Hand mit Blutröhrchen", "zuhoeren": "Ärztin hört aufmerksam zu", "blutdruck": "Ärztin misst den Blutdruck",
    "flur": "Heller Flur mit Olivenbaum", "wartebereich": "Wartebereich mit Ledersesseln und Pflanzen", "empfang": "Empfang mit Granittresen und Olivenbaum",
}

# Bild im Seitenkopf je Adresse. Team und Räume bleiben bewusst ohne Symbolbild.
KOPFBILD = {
    "inuspherese-zentrum-stuttgart": "apherese", "medizin/apherese-programm": "apherese", "medizin/help-apherese": "apherese", "longevity/apherese-reset": "apherese",
    "medizin": "blutdruck", "internistische-sprechstunde": "blutdruck", "ganzheitliche-sprechstunde": "zuhoeren", "darmgesundheit": "zuhoeren",
    "long-covid-sprechstunde": "gespraech", "sub-health-syndrom": "gespraech", "medizin/kinder": "wartebereich", "umweltmedizin": "labor",
    "labordiagnostik": "blutprobe", "energie-check": "blutprobe", "medizin/regenerationskuren": "wartebereich", "ganzkoerperhyperthermie": "wartebereich",
    "longevity": "ankommen", "longevity/check": "gespraech", "longevity/infusionen": "warten", "longevity/nad-infusion": "warten",
    "longevity/supplement-analyse": "labor", "longevity/regenerationskuren": "wartebereich", "longevity/preise": "empfang", "longevity/pflanzenwissen": "wartebereich",
    "leistungen": "blutdruck", "gutscheine": "wartebereich", "einloesen": "wartebereich", "terminvereinbarung": "empfang", "ihr-besuch": "flur", "kosten": "gespraech",
    "karriere-stellenangebote-jobs": "labor",
}


def bild(name):
    """Pfad zum Bild oder None."""
    f = f"assets/img/bild-{name}.webp"
    return R.rel(f) if os.path.exists(os.path.join(R.ROOT, f)) else None


def bild_img(name, cls="slot", alt=None):
    p = bild(name)
    if not p:
        return ""
    return f'<img class="{cls} b-{name}" src="{p}" alt="{ALT.get(name, "") if alt is None else alt}" width="1600" height="1194"><span class="symbolbild">Symbolbild</span>'


def foto(name):
    """Bild im Text, 4:3."""
    i = bild_img(name)
    return f'<div class="foto">{i.replace("<img ", "<img loading=\'lazy\' ")}</div>' if i else ""


def hero_bild(line):
    n = KOPFBILD.get(R._current["path"])
    return bild_img(n) if n else ""


def kreislauf():
    def box(x, y, w, h, fill, t, sub="", col=INK):
        s = f'<text x="{x+w/2}" y="{y+h/2+24}" text-anchor="middle" font-size="14" fill="{col}">{sub}</text>' if sub else ""
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'
                f'<text x="{x+w/2}" y="{y+h/2+(2 if sub else 6)}" text-anchor="middle" font-size="18" style="font-weight:600" fill="{col}">{t}</text>{s}')

    def nr(x, y, n):
        return f'<text x="{x}" y="{y}" font-size="14" fill="{TERRA}">0{n}</text>'
    return f"""<svg class="grafik" viewBox="0 0 640 430" role="img" aria-label="Kreislauf der Apherese: Blut wird entnommen, das Plasma abgetrennt, im Filter gereinigt und zusammen mit den Blutzellen zurückgegeben. Die Filterrückstände können als Eluat analysiert werden.">
<defs><marker id="pf" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9" fill="none" stroke="context-stroke" stroke-width="1.8"/></marker></defs>
<g fill="none" stroke-width="3">
<path d="M110 158 V75 H206" stroke="{TERRA}" marker-end="url(#pf)"/>
<path d="M370 75 H446" stroke="{CLAY}" marker-end="url(#pf)"/>
<path d="M530 120 V210 H530 V346 H206" stroke="{CLAY}" marker-end="url(#pf)"/>
<path d="M290 120 V346" stroke="{TERRA}"/>
<path d="M206 346 H110 V272" stroke="{TERRA}" marker-end="url(#pf)"/>
<path d="M560 120 V196" stroke="{INK}" stroke-dasharray="4 5" stroke-width="2"/></g>
<circle cx="290" cy="346" r="6" fill="{TERRA}"/>
{box(30, 160, 160, 110, SAND, 'Sie', 'liegen bequem')}
{box(210, 30, 160, 90, PEACH, 'Trennung', 'Plasma und Zellen')}
{box(450, 30, 160, 90, CLAY, 'Filter', 'Plasma gereinigt')}
{box(544, 200, 90, 60, INK, 'Eluat', '', '#fff')}
<text x="544" y="280" font-size="13" fill="{BROWN}">auf Wunsch</text><text x="544" y="297" font-size="13" fill="{BROWN}">Analyse</text>
{nr(30, 150, 1)}{nr(210, 20, 2)}{nr(450, 20, 3)}
<g font-size="14" fill="{BROWN}"><text x="122" y="62">Blut</text><text x="384" y="62">Plasma</text>
<text x="300" y="215">Blutzellen</text><text x="350" y="334">gereinigtes Plasma</text><text x="30" y="384">zurück in den Körper</text></g>
<text x="30" y="416" font-size="13" fill="{BROWN}">Vereinfachte Darstellung</text></svg>"""


def filterprinzip():
    gross = [(70, 90), (140, 190), (95, 270), (205, 120), (225, 260), (155, 60)]
    klein = [(60, 150), (120, 130), (180, 225), (110, 220), (235, 190), (200, 60), (250, 80), (60, 230)]
    durch = [(400, 80), (450, 140), (385, 180), (510, 100), (560, 180), (430, 240), (500, 220), (570, 270), (380, 280), (480, 290)]
    b = "".join(f'<circle cx="{x}" cy="{y}" r="22" fill="{INK}"/><circle cx="{x+15}" cy="{y-15}" r="6" fill="{CLAY}"/>' for x, y in gross)
    k = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{PEACH}" stroke="{TERRA}"/>' for x, y in klein + durch)
    m = "".join(f'<rect x="308" y="{y}" width="14" height="24" fill="{INK}"/>' for y in range(36, 310, 38))
    return f"""<svg class="grafik" viewBox="0 0 640 400" role="img" aria-label="Prinzip des Filters: Kleine Bestandteile wie Wasser, Salze und die meisten Nährstoffe gehen durch den Filter, große Eiweiße und Fette mit daran gebundenen Stoffen werden zurückgehalten.">
<rect x="20" y="30" width="288" height="290" fill="{SAND}"/><rect x="322" y="30" width="298" height="290" fill="#FDFAEE"/>
{b}{k}{m}
<g fill="none" stroke="{TERRA}" stroke-width="2"><path d="M268 174 H358 M350 167 L358 174 L350 181"/></g>
<g font-size="14" fill="{INK}"><text x="20" y="20">Plasma vor dem Filter</text><text x="340" y="20">Gereinigtes Plasma, zurück zu Ihnen</text></g>
<g font-size="13" fill="{BROWN}"><circle cx="30" cy="351" r="9" fill="{INK}"/><text x="48" y="356">große Eiweiße und Fette</text>
<circle cx="30" cy="381" r="5" fill="{CLAY}"/><text x="48" y="386">daran gebundene Stoffe</text>
<circle cx="336" cy="351" r="5" fill="{PEACH}" stroke="{TERRA}"/><text x="354" y="356">Wasser, Salze, die meisten Nährstoffe</text>
<text x="336" y="386">Vereinfachte Darstellung</text></g></svg>"""


ICONS = {
    "gespraech": '<path d="M6 8h26v18H18l-7 7v-7H6z"/><path d="M38 18h4v18h-5v6l-6-6H20v-4"/>',
    "diagnostik": '<path d="M17 5h14M20 5v13L9 39a3 3 0 0 0 3 4h24a3 3 0 0 0 3-4L28 18V5"/><path d="M14 31h20"/>',
    "plan": '<path d="M10 5h20l8 8v30H10z"/><path d="M30 5v8h8M17 22h14M17 29h14M17 36h8"/>',
    "begleitung": '<circle cx="17" cy="13" r="6"/><circle cx="34" cy="16" r="5"/><path d="M5 42V33a11 11 0 0 1 24 0v9M33 27a9 9 0 0 1 11 8v7"/>',
}


def icon(name):
    return f'<svg class="icon" viewBox="0 0 48 48" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'
