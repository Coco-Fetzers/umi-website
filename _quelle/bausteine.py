"""Wiederkehrende Bausteine für die Seiten."""
from rahmen import a, book, shop, tel, faq, mark, price  # noqa: F401
from grafiken import hero_bild
import config as C


def hero(eyebrow, h1, lead, buttons="", line="dach", extra=""):
    return f"""<section class="hero"><div class="wrap"><div>
{{{{CRUMBS}}}}<span class="eyebrow">{eyebrow}</span>
<h1>{h1}</h1>
<p class="lead">{lead}</p>{extra}
<div class="btns">{buttons}</div></div>
<div class="hero-mark">{hero_bild(line) or mark('light')}</div>
</div></section>"""


def liste(items, cls="checklist"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def schritte(items):
    """items = [(titel, text)]"""
    return '<ol class="steps">' + "".join(f"<li><b>{t}</b>{x}</li>" for t, x in items) + "</ol>"


def gutschein_hinweis(du=False):
    if du:
        t = "Du möchtest jemandem Zeit für Gesundheit schenken? Unsere Wertgutscheine gibt es ab 150 €, einlösbar für alle Leistungen."
    else:
        t = "Sie möchten jemandem Zeit für Gesundheit schenken? Unsere Wertgutscheine gibt es ab 150 €, einlösbar für alle Leistungen."
    return f"""<section class="tight"><div class="wrap"><div class="hint"><p>{t}</p>{a('gutscheine/', 'Zu den Gutscheinen', 'btn ghost small')}</div></div></section>"""


def kosten_box(du=False, extra=""):
    if du:
        txt = ("Ärztliche Leistungen werden nach der Gebührenordnung für Ärzte (GOÄ) berechnet, auch wenn du selbst zahlst. "
               "Der genannte Preis ist deshalb ein voraussichtlicher Betrag. Frag uns gern, wir sagen dir vorher offen, womit du rechnen kannst. Auf Wunsch bekommst du einen schriftlichen Kostenvoranschlag. "
               "Private Krankenversicherungen erstatten Vorsorgeleistungen in der Regel nicht.")
    else:
        txt = ("Ärztliche Leistungen berechnen wir nach der Gebührenordnung für Ärzte (GOÄ). Der genannte Preis ist ein voraussichtlicher Betrag. "
               "Auf Nachfrage geben wir Ihnen vorab transparent Auskunft zu den Kosten, auf Wunsch auch als schriftlichen Kostenvoranschlag. Ob und in welcher Höhe Ihre private Krankenversicherung "
               "oder Beihilfe erstattet, hängt von Ihrem Tarif ab. Wir helfen Ihnen beim Antrag.")
    return f"""<div class="box"><h3>Kosten</h3><p>{txt}</p>{extra}<p style="margin:0">{a('kosten/', 'Mehr zu Kosten und Erstattung')}</p></div>"""


def team_mini(names, du=False):
    data = {
        "kafle": ("Namrata Kafle", "Ärztliche Leitung, Ärztin für Innere Medizin", "team-namrata-kafle.jpg"),
        "buergler": ("Aurelia Bürgler", "Heilpraktikerin, Entspannungstherapeutin", "team-aurelia-buergler.jpg"),
        "gusic": ("Michaela Gusic", "Leitung INUSpherese-Zentrum, Krankenschwester Nephrologie", "team-michaela-gusic.jpg"),
        "gentsch": ("Evelyn Gentsch", "Fachkraft, Phytopraktikerin", "team-evelyn-gentsch.jpg"),
    }
    cards = []
    for n in names:
        name, role, img = data[n]
        cards.append(f"""<div class="person"><div class="ph"><img src="{a_img(img)}" alt="{name}, {role}" loading="lazy" width="480" height="720"></div>
<div class="tx"><h3>{name}</h3><p>{role}</p></div></div>""")
    head = "Wer dich betreut" if du else "Wer Sie betreut"
    return f"""<section><div class="wrap"><h2>{head}</h2><div class="team" style="grid-template-columns:repeat(auto-fill,minmax(200px,240px))">{''.join(cards)}</div>
<p style="margin-top:20px">{a('ueber-uns/', 'Das ganze Team kennenlernen')}</p></div></section>"""


def a_img(name):
    from rahmen import rel
    return rel("assets/img/" + name)


def naechster(text, target, label, du=False):
    return f"""<section class="bg-soft"><div class="wrap"><div class="split wide"><div>
<span class="eyebrow">{'Und danach' if du else 'Der nächste Schritt'}</span><h2>{text}</h2></div>
<div class="btns" style="align-self:center">{a(target, label, 'btn')}{book('Termin buchen', 'btn ghost')}</div></div></div></section>"""


def paket(*, eyebrow, h1, lead, preis_html, enthalten, ablauf, passt, passt_nicht,
          team, faqs, next_step=None, du=False, line="med", kosten_extra="", intro_extra=""):
    """Paketseite nach dem Muster aus der Sitemap (8 Blöcke)."""
    buttons = book("Termin buchen") + tel("btn ghost", "Anrufen: " + C.TEL)
    price_line = f'<p class="price-line"><b>{"Voraussichtliche Kosten" if not du else "Voraussichtlich"}: {preis_html}</b> · nach GOÄ, Kostenvoranschlag auf Wunsch</p>'
    parts = [hero(eyebrow, h1, lead, buttons, line, price_line)]
    if intro_extra:
        parts.append(intro_extra)
    parts.append(f"""<section class="bg-white"><div class="wrap"><div class="split">
<div><h2>{'Was enthalten ist' }</h2>{liste(enthalten)}</div>
<div><h2>{'So läuft es ab'}</h2>{schritte(ablauf)}</div></div></div></section>""")
    parts.append(f"""<section><div class="wrap"><div class="grid g3">
<div class="box"><h3>{'Passt zu dir, wenn …' if du else 'Passt zu Ihnen, wenn …'}</h3>{liste(passt)}</div>
<div class="box"><h3>{'Eher nicht, wenn …'}</h3>{liste(passt_nicht)}</div>
{kosten_box(du, kosten_extra)}</div></div></section>""")
    parts.append(team_mini(team, du))
    fh, fld = faq(faqs)
    parts.append(fh)
    if next_step:
        parts.append(naechster(*next_step, du=du))
    parts.append(gutschein_hinweis(du))
    return "".join(parts), [fld]
