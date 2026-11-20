"""Seiten unter dem Dach UMI Stuttgart (Ansprache: Sie)."""
from rahmen import Page, a, book, shop, tel, faq, mark, price
from bausteine import hero, liste, schritte, a_img
import config as C

GUTSCHEINE_G = [
    ("150 €", "Kleine Gesundheitspause", "Eine Pause nur für dich und deine Gesundheit."),
    ("300 €", "Zeit für deine Gesundheit", "Zeit, in Ruhe auf deine Gesundheit zu schauen."),
    ("450 €", "Gesundheit im Blick", "Wissen, wo du stehst, und was du selbst tun kannst."),
    ("ab 500 €", "Gesundheit nach Wunsch", "Ein Wert ganz nach deinem Wunsch."),
]
GUTSCHEINE_L = [
    ("150 €", "Insight"), ("300 €", "Atempause"), ("450 €", "Fokus"), ("ab 500 €", "Aufbruch"),
]


def voucher_cards(series="g"):
    out = []
    for i, item in enumerate(GUTSCHEINE_G if series == "g" else GUTSCHEINE_L, start=1):
        amount, name = item[0], item[1]
        line = item[2] if series == "g" else "Ein Geschenk an dein zukünftiges Ich."
        ring = mark("light" if i == 4 else "dach")
        out.append(f"""<div class="voucher v{i}" role="img" aria-label="Wertgutschein {amount}, {name}">
<div><div class="vname">{name}</div><div class="vline">{line}</div></div>
<div class="amount">{amount}</div>{ring}</div>""")
    return '<div class="vouchers">' + "".join(out) + "</div>"


# ------------------------------------------------------------ Gutscheine

def gutscheine():
    fh, fld = faq([
        ("Wofür kann man den Gutschein einlösen?",
         "Für alle Leistungen von UMI Stuttgart, in beiden Bereichen UMI Medizin und UMI Longevity. Welche Leistung passt, besprechen wir mit der beschenkten Person in Ruhe im ärztlichen Gespräch."),
        ("Wie lange gilt der Gutschein?",
         "Bis zum 31. Dezember des dritten Jahres nach dem Kauf. Ein Gutschein aus 2026 gilt also bis zum 31.12.2029."),
        ("Wie bekomme ich den Gutschein?",
         "Online erhalten Sie ihn sofort als PDF per E-Mail zum Ausdrucken. In der Praxis bekommen Sie ihn als gedruckte Karte mit Umschlag."),
        ("Was passiert, wenn eine Behandlung mehr oder weniger kostet?",
         "Der Gutschein wird auf die Rechnung angerechnet. Ein Restbetrag bleibt als Guthaben erhalten, ein Mehrbetrag wird ganz normal bezahlt."),
        ("Gibt es Rabatte oder Gutscheine für eine bestimmte Behandlung?",
         "Nein. Als ärztliche Praxis bieten wir nur Wertgutscheine zum vollen Preis an. Welche Behandlung sinnvoll ist, lässt sich erst im ärztlichen Gespräch entscheiden."),
        ("Kann ich den Gutschein weiterschenken?",
         "Ja, der Gutschein ist übertragbar. Bei Verlust ersetzen wir ihn gegen Nachweis des Kaufs mit der Gutscheinnummer."),
        ("Erstattet die Krankenversicherung Leistungen, die mit dem Gutschein bezahlt werden?",
         "Das richtet sich nach den Bedingungen der Versicherung oder Beihilfe. Vorsorgeleistungen werden meist nicht erstattet."),
    ])
    body = f"""
<section class="hero"><div class="wrap"><div>
{{{{CRUMBS}}}}<span class="eyebrow">Wertgutscheine von UMI Stuttgart</span>
<h1>Schenken Sie <em>Zeit für Gesundheit.</em></h1>
<p class="lead">Wertgutscheine ab 150 €, einlösbar für alle Leistungen von UMI Stuttgart und drei Jahre gültig. Sofort per E-Mail oder als Karte in unserer Praxis in Stuttgart-Vaihingen.</p>
<div class="btns">{shop()}{a('#kaufen', 'So kaufen Sie', 'btn ghost')}</div></div>
<div class="hero-mark">{mark('lon')}</div></div></section>

<section class="bg-white" id="werte"><div class="wrap">
<span class="eyebrow">Wertgutscheine</span>
<h2>Vier Werte, zwei Motive</h2>
<p class="lead" style="margin-bottom:28px">Der Wert ist fest, die Leistung wählt die beschenkte Person später selbst, gemeinsam mit unserer Ärztin. Suchen Sie sich einfach das Motiv aus, das Ihnen am besten gefällt.</p>
{voucher_cards('g')}
<div style="margin-top:24px">{voucher_cards('l')}</div>
<p class="voucher-meta muted">Ab 500 € in Schritten von 50 €. Die Beispiele auf der Karte sind eine Orientierung, kein Anspruch auf eine bestimmte Leistung.</p>
</div></section>

<section><div class="wrap"><div class="split">
<div><h2>Was man damit buchen kann</h2>
<p>Alles, was wir anbieten. Ein paar Beispiele, wofür die Werte reichen können:</p>
<table class="price-table"><tr><th>Wert</th><th>zum Beispiel</th></tr>
<tr><td>150 €</td><td style="white-space:normal;font-weight:400">eine Infusion aus dem {a('longevity/infusionen/', 'Infusionsmenü')} oder ein Vorgespräch</td></tr>
<tr><td>300 €</td><td style="white-space:normal;font-weight:400">die {a('longevity/supplement-analyse/', 'Supplement-Analyse')} oder mehrere Infusionen</td></tr>
<tr><td>450 €</td><td style="white-space:normal;font-weight:400">den {a('longevity/check/', 'Longevity-Check')}</td></tr>
<tr><td>ab 500 €</td><td style="white-space:normal;font-weight:400">{a('longevity/nad-infusion/', 'NAD+-Kur')}, {a('energie-check/', 'Energie-Check')} oder {a('inuspherese-zentrum-stuttgart/', 'Apherese')}</td></tr></table>
<p class="small muted" style="margin-top:12px">Welche Leistung passt, besprechen wir in Ruhe im ärztlichen Gespräch.</p></div>
<div id="kaufen"><h2>So kaufen Sie</h2>
{schritte([
    ('Online', ' Betrag und Motiv wählen, bezahlen, PDF kommt sofort per E-Mail. ' + ('' if C.GUTSCHEIN_SHOP else '<i>Der Online-Verkauf startet in Kürze.</i>')),
    ('In der Praxis', f' Gedruckte Karte mit Umschlag am Empfang, {C.OEFFNUNGSZEITEN}.'),
    ('Am Telefon', f' Rufen Sie uns an unter {tel()}. Wir schicken den Gutschein per Post oder legen ihn zur Abholung bereit.'),
])}
<div class="btns">{shop()}</div>
<p class="small muted" style="margin-top:14px">Jeder Gutschein hat eine Nummer, einen Wert und ein Ausstellungsdatum. Es gelten unsere {a('gutscheinbedingungen/', 'Gutscheinbedingungen')}.</p>
</div></div></div></section>

<section class="bg-white"><div class="wrap"><div class="grid g3">
<div class="box"><h3>Drei Jahre gültig</h3><p>Bis zum 31.12. des dritten Jahres nach dem Kauf. Genug Zeit, in Ruhe einen Termin zu finden.</p></div>
<div class="box"><h3>Für alle Leistungen</h3><p>UMI Medizin und UMI Longevity. Restguthaben bleibt erhalten.</p></div>
<div class="box"><h3>Ärztlich begleitet</h3><p>Jede Behandlung beginnt mit einem Gespräch. Was nicht passt, wird nicht gemacht.</p></div>
</div></div></section>

<section class="tight"><div class="wrap"><div class="hint"><p><b>Sie haben einen Gutschein bekommen?</b> So lösen Sie ihn ein.</p>{a('einloesen/', 'Gutschein einlösen', 'btn ghost small')}</div></div></section>
{fh}"""
    return body, [fld]


def einloesen():
    return f"""{hero('Gutschein einlösen', 'Sie haben einen Gutschein von UMI Stuttgart bekommen?',
    'Schön, dass Sie da sind. Der Gutschein gilt für alle unsere Leistungen. So einfach geht es:',
    book('Termin buchen') + tel('btn ghost', 'Anrufen: ' + C.TEL))}
<section class="bg-white"><div class="wrap narrow">
{schritte([
    ('Termin buchen', ' online über Doctolib oder telefonisch. Sagen Sie uns gern dazu, dass Sie einen Gutschein haben.'),
    ('Gutschein mitbringen', ' ausgedruckt, als Karte oder auf dem Handy. Wichtig ist die Gutscheinnummer.'),
    ('Im Gespräch klären, was passt', ' Unsere Ärztin bespricht mit Ihnen, welche Leistung sinnvoll ist. Zu den Kosten geben wir Ihnen gern Auskunft, auf Wunsch auch schriftlich als Kostenvoranschlag.'),
    ('Verrechnen', ' Der Gutschein wird auf die Rechnung angerechnet. Ein Rest bleibt als Guthaben für später.'),
])}
<div class="grid g2" style="margin-top:32px">
{a('medizin/', '<span class="tag">UMI Medizin</span><h3>Ich habe Beschwerden</h3><p>Ursachen finden, gründlich und ärztlich.</p><span class="more">Zu UMI Medizin →</span>', 'card')}
{a('longevity/', '<span class="tag">UMI Longevity</span><h3>Ich will gesund bleiben</h3><p>Wissen, wo du stehst. Gezielt etwas tun.</p><span class="more">Zu UMI Longevity →</span>', 'card')}
</div>
<p class="small muted" style="margin-top:24px">Gültigkeit, Restwert und alle Regeln: {a('gutscheinbedingungen/', 'Gutscheinbedingungen')}.</p>
</div></section>"""


def gutscheinbedingungen():
    return f"""<section><div class="wrap narrow legal-text">{{{{CRUMBS}}}}
<h1>Gutscheinbedingungen</h1>
<p class="muted small">Entwurf, Stand November 2026. Vor dem Verkaufsstart rechtlich prüfen lassen.</p>
<ol>
<li>Der Gutschein ist ein Wertgutschein über den angegebenen Betrag. Er kann für alle Leistungen der Praxis UMI Stuttgart eingelöst werden.</li>
<li>Er ist gültig bis zum 31. Dezember des dritten Jahres nach dem Kauf. Ein 2026 gekaufter Gutschein gilt bis zum 31.12.2029.</li>
<li>Welche Leistung sinnvoll ist, wird im ärztlichen Gespräch entschieden. Kann eine gewünschte Leistung aus medizinischen Gründen nicht erbracht werden, ist der Gutschein für andere Leistungen einlösbar. Ist das nicht möglich, erstatten wir den Restwert.</li>
<li>Ärztliche Leistungen werden nach der Gebührenordnung für Ärzte (GOÄ) berechnet. Der Gutschein wird auf die Rechnung angerechnet. Ein Restwert bleibt als Guthaben erhalten, ein Mehrbetrag wird regulär bezahlt.</li>
<li>Eine Barauszahlung ist ausgeschlossen, soweit in Punkt 3 nichts anderes geregelt ist.</li>
<li>Der Gutschein ist übertragbar. Bei Verlust ersetzen wir ihn gegen Nachweis des Kaufs (Gutscheinnummer).</li>
<li>Die Erstattung durch private Krankenversicherungen oder Beihilfe richtet sich nach deren Bedingungen. Vorsorgeleistungen werden meist nicht erstattet.</li>
</ol>
<h2>Widerrufsrecht beim Online-Kauf</h2>
<p>Beim Kauf über unseren Online-Shop gilt ein Widerrufsrecht von 14 Tagen. Die Widerrufsbelehrung und das Muster-Widerrufsformular finden Sie im Shop vor dem Kauf.</p>
<h2>Verkäufer</h2>
<p>UMI Stuttgart GmbH, {C.STRASSE}, {C.PLZ} Stuttgart · Telefon {tel()} · <a href="mailto:{C.MAIL}">{C.MAIL}</a></p>
</div></section>"""


# ------------------------------------------------------------ Startseite

def start():
    return f"""
<section class="hero" style="padding-bottom:40px"><div class="wrap" style="display:block">
<span class="eyebrow">Privatpraxis in Stuttgart-Vaihingen · seit 2023 INUSpherese-Zentrum</span>
<h1 style="max-width:900px">Medizin, die nach Ursachen sucht. <em>Und dich gesund begleitet.</em></h1>
<p class="lead">UMI Stuttgart verbindet gründliche Diagnostik mit Verfahren, die es in der Region sonst kaum gibt. Für Menschen mit anhaltenden Beschwerden und für alle, die gesund bleiben wollen.</p>
<div class="doors">
<a class="door med" href="{a_rel('medizin/')}"><span class="line-name">UMI Medizin</span><h2>Ich habe Beschwerden</h2>
<p>Gründliche Abklärung, wenn die Werte normal sind und es Ihnen trotzdem nicht gut geht. Mit Apherese, Wärmetherapie und Naturheilkunde.</p><span class="go">Ursachen finden →</span></a>
<a class="door lon" href="{a_rel('longevity/')}"><span class="line-name">UMI Longevity</span><h2>Ich will gesund bleiben</h2>
<p>Messen, verstehen, gezielt etwas tun. Ärztlich, ohne Versprechen, mit einem Plan, der zu deinem Alltag passt.</p><span class="go">Wissen, wo du stehst →</span></a>
</div></div></section>

<section class="tight"><div class="wrap"><div class="banner">
<div><span class="eyebrow">Wertgutscheine ab 150 €</span><h2>Schenken Sie Zeit für Gesundheit.</h2>
<p style="margin:0">Einlösbar für alle Leistungen, drei Jahre gültig. Sofort per E-Mail oder als Karte in der Praxis.</p></div>
<div>{a('gutscheine/', 'Gutschein wählen', 'btn')}</div></div></div></section>

<section class="tight"><div class="wrap"><div class="hint"><p><b>Immer müde, aber die Werte sind normal?</b> Der Energie-Check schaut genauer hin.</p>{a('energie-check/', 'Zum Energie-Check', 'btn ghost small')}</div></div></section>

<section class="bg-white"><div class="wrap"><div class="split">
<div><span class="eyebrow">Apherese in Stuttgart</span><h2>INUSpherese und H.E.L.P.-Apherese</h2>
<p>Bei der Apherese wird das Blutplasma außerhalb des Körpers gefiltert, umgangssprachlich oft „Blutwäsche“ genannt. UMI Stuttgart bietet als zertifizierter INUS-Partner beide Verfahren an und ist damit in Stuttgart der einzige Anbieter.</p>
<p>Betreut werden Sie von einem Team mit langjähriger Dialyse-Erfahrung. Was sich aus Ihrem Plasma filtern ließ, zeigt auf Wunsch die Eluat-Analyse.</p>
<div class="btns">{a('inuspherese-zentrum-stuttgart/', 'Mehr zur Apherese', 'btn')}{a('kosten/', 'Was kostet das?', 'btn ghost')}</div></div>
<div class="svg-schema">{schema_svg()}</div></div></div></section>

<section><div class="wrap"><span class="eyebrow">So arbeiten wir</span><h2>Zuhören, genau hinschauen, gemeinsam planen</h2>
<div class="grid g4" style="margin-top:28px">
<div class="card"><span class="tag">1</span><h3>Gespräch</h3><p>Ausführlich, mit Zeit für Ihre Geschichte und Ihre Fragen.</p></div>
<div class="card"><span class="tag">2</span><h3>Diagnostik</h3><p>Labor, Untersuchung und Messungen, die über den Routine-Check hinausgehen.</p></div>
<div class="card"><span class="tag">3</span><h3>Plan</h3><p>Ein schriftlicher Plan, auf Wunsch mit Kostenvoranschlag. Sie entscheiden in Ruhe.</p></div>
<div class="card"><span class="tag">4</span><h3>Begleitung</h3><p>Therapie, Kontrolle und Folgetermine, mit festen Ansprechpartnerinnen.</p></div>
</div></div></section>

<section class="bg-white"><div class="wrap"><span class="eyebrow">Unser Team</span><h2>Ärztin, Heilpraktikerin und Fachkräfte mit Apherese-Erfahrung</h2>
<div class="team" style="margin-top:28px">{start_team()}</div>
<p style="margin-top:20px">{a('ueber-uns/', 'Alle im Team kennenlernen')}</p></div></section>

<section><div class="wrap"><div class="split">
<div><span class="eyebrow">Ihr Besuch bei uns</span><h2>Mitten in Stuttgart-Vaihingen</h2>
<p>{C.STRASSE}<br>{C.PLZ} Stuttgart</p><p>{C.OEFFNUNGSZEITEN}</p>
<p>Telefon {tel()}<br>E-Mail <a href="mailto:{C.MAIL}">{C.MAIL}</a></p>
<div class="btns">{a('ihr-besuch/', 'Anfahrt und Ablauf', 'btn ghost')}{book()}</div></div>
<div class="box"><h3>Wir sind eine Privatpraxis</h3><p>Wir behandeln Privatversicherte, Beihilfeberechtigte und Selbstzahler. Zu den Kosten geben wir Ihnen vorab gern Auskunft, auf Wunsch auch als schriftlichen Kostenvoranschlag.</p><p style="margin:0">{a('kosten/', 'Kosten und Erstattung')}</p></div>
</div></div></section>"""


def a_rel(t):
    from rahmen import rel
    return rel(t)


def start_team():
    people = [("Namrata Kafle", "Ärztliche Leitung, Innere Medizin", "team-namrata-kafle.jpg"),
              ("Aurelia Bürgler", "Heilpraktikerin", "team-aurelia-buergler.jpg"),
              ("Michaela Gusic", "Leitung INUSpherese-Zentrum", "team-michaela-gusic.jpg"),
              ("Evelyn Gentsch", "Fachkraft, Apherese", "team-evelyn-gentsch.jpg")]
    return "".join(f"""<div class="person"><div class="ph"><img src="{a_img(i)}" alt="{n}, {r}" loading="lazy" width="480" height="720"></div><div class="tx"><h3>{n}</h3><p>{r}</p></div></div>""" for n, r, i in people)


def schema_svg():
    return """<svg viewBox="0 0 560 300" role="img" aria-label="Schema der Apherese: Blut wird entnommen, das Plasma abgetrennt und gefiltert und gereinigt zurückgegeben" style="width:100%;height:auto;font-family:'Hanken Grotesk',sans-serif">
<rect x="0" y="0" width="560" height="300" fill="#FFFFFF"/>
<g fill="#5F6770"><circle cx="70" cy="110" r="18"/><path d="M40 140 h60 v70 h-14 v60 h-12 v-60 h-8 v60 h-12 v-60 h-14z"/></g>
<path d="M100 150 C150 150 160 80 210 80" fill="none" stroke="#9B8C82" stroke-width="5"/>
<rect x="210" y="50" width="110" height="60" rx="12" fill="#EBE1D3"/><text x="265" y="78" text-anchor="middle" font-size="15" fill="#3E454D" font-weight="600">Plasma-</text><text x="265" y="96" text-anchor="middle" font-size="15" fill="#3E454D" font-weight="600">abtrennung</text>
<path d="M320 80 C360 80 360 80 380 80" fill="none" stroke="#9B8C82" stroke-width="5"/>
<rect x="380" y="50" width="130" height="60" rx="12" fill="#A8B5A5"/><text x="445" y="78" text-anchor="middle" font-size="15" fill="#3E454D" font-weight="600">Filter</text><text x="445" y="96" text-anchor="middle" font-size="13" fill="#3E454D">INUSpherese / H.E.L.P.</text>
<path d="M445 110 L445 150" stroke="#9B8C82" stroke-width="3" stroke-dasharray="5 5"/><rect x="390" y="150" width="110" height="40" rx="10" fill="#F7F3ED" stroke="#9B8C82"/><text x="445" y="175" text-anchor="middle" font-size="13" fill="#3E454D">Eluat-Analyse</text>
<path d="M380 100 C330 200 200 230 100 200" fill="none" stroke="#6F806E" stroke-width="5"/>
<text x="230" y="258" text-anchor="middle" font-size="14" fill="#6F806E" font-weight="600">gefiltertes Plasma zurück</text>
<text x="160" y="58" text-anchor="middle" font-size="14" fill="#5F6770">Blut</text>
</svg>"""


# ------------------------------------------------------------ Kosten

def kosten():
    fh, fld = faq([
        ("Was kostet eine Blutwäsche (Apherese)?",
         f"Eine Sitzung INUSpherese kostet voraussichtlich {price('apherese_sitzung', '')} nach GOÄ. Das Apherese-Programm mit Vorgespräch, Diagnostik, zwei Sitzungen und Nachgespräch kostet voraussichtlich {price('apherese_programm')}. Auf Wunsch erhalten Sie vorab einen Kostenvoranschlag."),
        ("Zahlt die private Krankenversicherung?",
         "Das hängt von Ihrem Tarif und der medizinischen Begründung ab. Bei Behandlungen wegen einer Erkrankung erstatten Versicherer und Beihilfe häufig einen Teil. Vorsorge- und Longevity-Leistungen werden in der Regel nicht erstattet. Fragen Sie am besten vorab bei Ihrer Versicherung nach. Für die Anfrage erstellen wir Ihnen auf Wunsch einen Kostenvoranschlag."),
        ("Behandeln Sie gesetzlich Versicherte?",
         "Ja, als Selbstzahler. Wir sind eine Privatpraxis und rechnen nicht mit der gesetzlichen Krankenkasse ab."),
        ("Warum steht „voraussichtlich“ vor den Preisen?",
         "Ärztliche Leistungen müssen nach der GOÄ abgerechnet werden. Der genaue Betrag ergibt sich aus den tatsächlich erbrachten Leistungen. Unsere Preise beschreiben, was ein Paket in der Regel kostet."),
        ("Gibt es Rabatte?",
         "Nein. Ärztinnen und Ärzte dürfen keine Rabatte auf Behandlungen geben. Erhalten Sie dieselbe Infusion innerhalb von 4 Wochen erneut, kostet sie etwas weniger, weil das ärztliche Gespräch nach der GOÄ dann nicht noch einmal berechnet wird."),
    ])
    body = f"""{hero('Kosten und Erstattung', 'Was kostet eine Behandlung bei UMI Stuttgart?',
    'Wir sind eine Privatpraxis und rechnen nach der Gebührenordnung für Ärzte (GOÄ) ab. Fragen Sie uns gern vorab nach den Kosten, wir geben Ihnen transparent Auskunft. Auf Wunsch erhalten Sie einen schriftlichen Kostenvoranschlag.',
    book('Vorgespräch buchen') + tel('btn ghost', 'Anrufen'))}
<section class="bg-white"><div class="wrap">
<h2>Voraussichtliche Kosten der Pakete</h2>
<p class="muted">Alle Preise sind voraussichtliche Kosten nach GOÄ. Platzhalter „ab … €“ werden mit der Freigabe der Preise ersetzt.</p>
<div class="split" style="margin-top:20px">
<table class="price-table"><tr><th colspan="2">UMI Medizin</th></tr>
<tr><td>{a('medizin/apherese-programm/', 'Apherese-Programm')}</td><td>{price('apherese_programm')}</td></tr>
<tr><td>INUSpherese, weitere Sitzung</td><td>{price('apherese_sitzung', '')}</td></tr>
<tr><td>{a('energie-check/', 'Energie-Check')}</td><td>{price('energie_check')}</td></tr>
<tr><td>{a('medizin/regenerationskuren/', 'Wärmekur')} (Ganzkörperhyperthermie, 6 Sitzungen)</td><td>{price('kur_hyperthermie')}</td></tr>
<tr><td>Oxyvenierung, 12 Sitzungen</td><td>{price('kur_oxyvenierung')}</td></tr>
<tr><td>Farblaser, 12 Sitzungen</td><td>{price('kur_farblaser')}</td></tr></table>
<table class="price-table"><tr><th colspan="2">UMI Longevity</th></tr>
<tr><td>{a('longevity/check/', 'Longevity-Check')}</td><td>{price('longevity_check')}</td></tr>
<tr><td>{a('longevity/nad-infusion/', 'NAD+-Infusion')}, je Infusion</td><td>ca. {price('nad_infusion', '')}</td></tr>
<tr><td>{a('longevity/infusionen/', 'Infusionsmenü')}, je Infusion inkl. ärztlichem Gespräch</td><td>ab ca. {price('infusion_ab', '')}</td></tr>
<tr><td>{a('longevity/supplement-analyse/', 'Supplement-Analyse')}</td><td>{price('supplement_analyse')}</td></tr>
<tr><td>{a('longevity/apherese-reset/', 'Apherese Reset')}</td><td>{price('apherese_reset')}</td></tr></table>
</div></div></section>
<section><div class="wrap"><div class="grid g3">
<div class="box"><h3>Kostenvoranschlag auf Wunsch</h3><p>Fragen Sie uns vor der Behandlung, was sie voraussichtlich kostet. Wir geben Ihnen transparent Auskunft. Wenn Sie es schriftlich möchten, zum Beispiel für Ihre Versicherung, erstellen wir Ihnen einen Kostenvoranschlag.</p></div>
<div class="box"><h3>Hilfe beim Erstattungsantrag</h3><p>Für Ihre private Krankenversicherung oder Beihilfe stellen wir die nötigen Unterlagen zusammen und erklären, was Sie einreichen.</p></div>
<div class="box"><h3>Gesetzlich versichert?</h3><p>Sie sind als Selbstzahler herzlich willkommen. Wir beraten Sie vorher offen zu den Kosten.</p></div>
</div></div></section>
{fh}"""
    return body, [fld]


# ------------------------------------------------------------ Termin und Kontakt

def termin():
    return f"""{hero('Termin und Kontakt', 'Termin vereinbaren',
    'Am schnellsten online über Doctolib. Sie erreichen uns auch telefonisch oder per E-Mail, wir melden uns schnellstmöglich zurück.',
    book('Online buchen bei Doctolib') + tel('btn ghost', 'Anrufen: ' + C.TEL))}
<section class="bg-white"><div class="wrap"><div class="grid g3">
<div class="box"><h3>Online</h3><p>Termine für Erstgespräch, Longevity-Gespräch, Vorgespräch und Folgetermine buchen Sie rund um die Uhr über Doctolib. Auch für Angehörige.</p>{book('Zu Doctolib', 'btn small')}</div>
<div class="box"><h3>Telefon</h3><p>{tel()}<br>{C.OEFFNUNGSZEITEN}</p><p class="small muted">Fax {C.FAX}</p></div>
<div class="box"><h3>E-Mail</h3><p><a href="mailto:{C.MAIL}">{C.MAIL}</a></p><p class="small muted">Bitte schicken Sie uns keine Befunde unverschlüsselt per E-Mail. Bringen Sie sie gern zum Termin mit.</p></div>
</div></div></section>
<section><div class="wrap"><div class="split">
<div><h2>Noch unsicher, was passt?</h2><p>Im <b>Vorgespräch am Telefon oder per Video</b> klären wir, ob und wie wir Ihnen weiterhelfen können, bevor Sie anreisen. Das ist besonders für Patientinnen und Patienten mit weiter Anfahrt sinnvoll.</p>
<p>Für Angehörige bieten wir ein eigenes <b>Angehörigengespräch</b> an.</p></div>
<div class="box"><h3>Adresse</h3><p>{C.NAME_LANG}<br>{C.STRASSE}<br>{C.PLZ} Stuttgart</p><p style="margin:0">{a('ihr-besuch/', 'Anfahrt, Parken und Ablauf')}</p></div>
</div></div></section>"""


def besuch():
    fh, fld = faq([
        ("Kann ich eine Begleitperson mitbringen?", "Ja, gern. Bei längeren Behandlungen wie der Apherese ist eine Begleitung für die Heimfahrt sinnvoll."),
        ("Darf ich nach der Behandlung selbst Auto fahren?", "Nach Apherese und Ganzkörperhyperthermie empfehlen wir, nicht selbst zu fahren. Wir besprechen das vorher mit Ihnen."),
        ("Was soll ich zum ersten Termin mitbringen?", "Vorbefunde, Arztbriefe, Laborwerte, eine Liste Ihrer Medikamente und Nahrungsergänzungen und, falls vorhanden, Ihren Gutschein."),
        ("Ist die Praxis barrierefrei?", "Bitte rufen Sie uns kurz an, dann besprechen wir, wie wir Ihren Besuch am besten vorbereiten."),
    ])
    body = f"""{hero('Ihr Besuch bei uns', 'Anfahrt, Parken und Ablauf',
    f'Sie finden uns in Stuttgart-Vaihingen, {C.STRASSE}. Patientinnen und Patienten kommen aus der ganzen Region Stuttgart und von weiter her zu uns.',
    book() + tel('btn ghost', 'Anrufen'))}
<section class="bg-white"><div class="wrap"><div class="grid g3">
<div class="box"><h3>Adresse</h3><p>{C.NAME_LANG}<br>{C.STRASSE}<br>{C.PLZ} Stuttgart</p><p><a href="https://www.google.com/maps/search/?api=1&amp;query=Schulze-Delitzsch-Str.+38+70565+Stuttgart" rel="noopener" target="_blank">In Google Maps öffnen</a></p></div>
<div class="box"><h3>Mit Bus und Bahn</h3><p>Angaben zu Haltestelle und Fußweg folgen.</p></div>
<div class="box"><h3>Mit dem Auto</h3><p>Angaben zum Parken folgen.</p></div>
</div></div></section>
<section><div class="wrap"><div class="split">
<div><h2>So läuft Ihr erster Termin</h2>{schritte([
    ('Ankommen', ' Am Empfang nehmen wir Ihre Daten auf. Bitte kommen Sie etwa 10 Minuten früher.'),
    ('Gespräch', ' Ausführliche Anamnese und Untersuchung mit unserer Ärztin.'),
    ('Diagnostik', ' Blutabnahme und Messungen, je nach Anlass gleich am selben Tag.'),
    ('Plan', ' Sie bekommen einen Vorschlag, auf Wunsch mit Kostenvoranschlag, und entscheiden in Ruhe.'),
])}</div>
<div><h2>Am Behandlungstag</h2><p>Für Apherese, Ganzkörperhyperthermie und Infusionen planen Sie bitte genug Zeit ein. Eine Apherese dauert etwa zwei bis drei Stunden, eine Ganzkörperhyperthermie mit Ruhephase etwa zwei Stunden. Trinken Sie vorher ausreichend und essen Sie leicht.</p>
<p>Wer von weiter her anreist, bekommt von uns gern Hinweise zur Übernachtung in der Nähe.</p></div>
</div></div></section>
{fh}"""
    return body, [fld]


# ------------------------------------------------------------ Team

TEAM = [
    ("Ärztliche Leitung", [
        ("Namrata Kafle", "Ärztin für Innere Medizin", "team-namrata-kafle.jpg",
         ["2011 Bachelor Medizin, Bangladesch", "2013 Assistenzärztin Notfall und Innere Medizin, Kathmandu, Nepal",
          "2017 Assistenzärztin, AMEOS Gruppe Halberstadt", "2019 Approbation in Deutschland",
          "2022 Assistenzärztin Innere Medizin, RKH Bietigheim-Bissingen", "2023 Assistenzärztin, Filderklinik Stuttgart"]),
    ]),
    ("Naturheilkunde", [
        ("Aurelia Bürgler", "Heilpraktikerin, Entspannungstherapeutin", "team-aurelia-buergler.jpg",
         ["2012 Entspannungstherapeutin, Stuttgart", "2015 Zulassung als Heilpraktikerin, Tübingen", "seit 2015 eigene Praxis",
          "2023 bis 2026 Therapeutin im Börner Lebenswerk, Tübingen"]),
    ]),
    ("INUSpherese-Zentrum und Fachkräfte", [
        ("Michaela Gusic", "Leitung INUSpherese-Zentrum, examinierte Krankenschwester, Fachrichtung Nephrologie", "team-michaela-gusic.jpg",
         ["1998 examinierte Krankenschwester", "1998 Dialyse, Klinikum Stuttgart", "2017 Leitung Dialysestation, Klinikum Stuttgart",
          "seit 2021 zertifizierte Qualitätsmanagement-Beauftragte"]),
        ("Evelyn Gentsch", "Examinierte Kinderkrankenschwester, Phytopraktikerin", "team-evelyn-gentsch.jpg",
         ["1999 examinierte Kinderkrankenschwester", "2001 Kinderchirurgie, Schwäbisch Hall", "2004 Kinderdialyse, Universitätsklinikum Tübingen",
          "2019 Hausarztpraxis Herrenberg", "2025 Ausbildung Heilpflanzenkunde und Phytotherapie"]),
    ]),
    ("Verwaltung", [
        ("Bini Göller", "Praxismanagement, Dipl.-Betriebswirtin (FH)", None,
         ["2003 Dipl.-Betriebswirtin (FH), Reutlingen", "Vertrieb und Controlling bei Bosch und der Daimler AG",
          "2018 Sekretariatsleitung, Institut für Psychoanalyse der DPG Stuttgart"]),
    ]),
]


def team():
    groups = []
    lds = []
    for g, people in TEAM:
        cards = []
        for name, role, img, cv in people:
            ini = "".join(w[0] for w in name.replace("Dr. med. ", "").split()[:2])
            ph = f'<img src="{a_img(img)}" alt="{name}, {role}" loading="lazy" width="480" height="720">' if img else ini
            det = ("<details><summary>Werdegang</summary>" + liste(cv, "") + "</details>") if cv else ""
            cards.append(f'<div class="person"><div class="ph">{ph}</div><div class="tx"><h3>{name}</h3><p>{role}</p>{det}</div></div>')
            if "Ärzt" in role or "Fachärztin" in role:
                lds.append({"@context": "https://schema.org", "@type": "Physician", "name": name,
                            "description": role, "worksFor": {"@type": "MedicalClinic", "name": "UMI Stuttgart"}})
        groups.append(f'<h2 style="margin-top:12px">{g}</h2><div class="team" style="margin:20px 0 48px">{"".join(cards)}</div>')
    body = f"""{hero('Über uns', 'Das Team von UMI Stuttgart',
    'Ärztinnen, Heilpraktikerin und Fachkräfte mit langjähriger Erfahrung in Dialyse und Apherese. Wir nehmen uns Zeit, hören zu und erklären, was wir tun.',
    book() + a('praxis/', 'Unsere Räume', 'btn ghost'))}
<section class="bg-white"><div class="wrap">{''.join(groups)}</div></section>
<section><div class="wrap"><div class="hint"><p><b>Wir suchen Verstärkung</b> für Pflege und Ärzteteam.</p>{a('karriere-stellenangebote-jobs/', 'Zu den Stellen', 'btn ghost small')}</div></div></section>"""
    return body, lds


def praxis():
    rooms = ["Empfang", "Wartezimmer", "Behandlungszimmer", "Infusionsraum", "INUSpherese-Raum", "Praxis"]
    tiles = "".join(f'<div class="person"><div class="ph" style="aspect-ratio:3/2;font-size:20px;font-family:var(--sans)">Foto folgt</div><div class="tx"><h3>{r}</h3></div></div>' for r in rooms)
    return f"""{hero('Unsere Räume', 'Ruhige Räume für Gespräch und Behandlung',
    'Unsere Praxis in Stuttgart-Vaihingen hat eigene Räume für Gespräche, Infusionen, Wärmetherapie und Apherese. Hier ein erster Eindruck.',
    a('ihr-besuch/', 'Ihr Besuch bei uns', 'btn') + book('Termin buchen', 'btn ghost'))}
<section class="bg-white"><div class="wrap"><div class="team" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">{tiles}</div>
<p class="small muted" style="margin-top:16px">Die Fotos der heutigen Website werden hier übernommen.</p></div></section>"""


def karriere():
    jobs = [
        ("Dialyse- oder Apheresefachkraft (m/w/d)", "Voll- oder Teilzeit",
         "Sie betreuen Patientinnen und Patienten bei INUSpherese und H.E.L.P.-Apherese. Sie bringen eine Ausbildung in der Krankenpflege mit, idealerweise Erfahrung in der Dialyse. Wir bieten geregelte Arbeitszeiten ohne klassische Klinikdienste."),
        ("Ärztin oder Arzt (m/w/d) mit Interesse an Umweltmedizin und ganzheitlicher Medizin", "Voll- oder Teilzeit",
         "Sie haben eine Approbation und möchten Patientinnen und Patienten gründlich und mit Zeit betreuen. Wir behandeln Privatversicherte und Selbstzahler."),
        ("Assistenz- oder Fachärztin, -arzt als regelmäßige Vertretung (m/w/d)", "angestellt oder auf Honorarbasis",
         "Vertretung bei Urlaub, Fortbildung und Krankheit in unserer Praxis in Stuttgart-Vaihingen. Eine Einarbeitung in die INUSpherese ist inklusive."),
        ("Ärztin oder Arzt im Ruhestand als regelmäßige Vertretung (m/w/d)", "auf Honorarbasis",
         "Wie oben, für erfahrene Kolleginnen und Kollegen, die weiter in einem kleinen Team arbeiten möchten."),
    ]
    cards = "".join(f'<div class="card"><span class="tag">{t}</span><h3>{n}</h3><p>{d}</p></div>' for n, t, d in jobs)
    return f"""{hero('Karriere', 'Werden Sie Teil unseres Teams',
    'Gestalten Sie mit uns Medizin, die den Menschen in den Mittelpunkt stellt. Ein kleines Team, eine besondere Therapie und Zeit für Patientinnen und Patienten.',
    f'<a class="btn" href="mailto:{C.MAIL_BEWERBUNG}">Jetzt bewerben</a>')}
<section class="bg-white"><div class="wrap"><div class="grid g2">{cards}</div>
<p style="margin-top:24px">Bewerbungen bitte per E-Mail an <a href="mailto:{C.MAIL_BEWERBUNG}">{C.MAIL_BEWERBUNG}</a>.</p></div></section>"""


# ------------------------------------------------------------ Rechtliches

def impressum():
    return f"""<section><div class="wrap narrow legal-text">{{{{CRUMBS}}}}
<h1>Impressum</h1>
<p class="muted small">Entwurf auf Grundlage des heutigen Impressums. Vor dem Livegang prüfen lassen.</p>
<h2>Angaben gemäß § 5 DDG</h2>
<p>UMI Stuttgart GmbH<br>Umweltmedizinisches Institut Stuttgart<br>{C.STRASSE}<br>{C.PLZ} Stuttgart</p>
<p>Handelsregister: HRB 788067, Amtsgericht Stuttgart<br>Umsatzsteuer-Identifikationsnummer: DE359171405</p>
<p>Vertreten durch die Geschäftsführung: Andreas Braig, Bettina Fetzer, Dirk Fetzer</p>
<h2>Kontakt</h2>
<p>Telefon: {tel()}<br>Fax: {C.FAX}<br>E-Mail: <a href="mailto:{C.MAIL}">{C.MAIL}</a></p>
<h2>Ärztliche Leitung</h2>
<p>Namrata Kafle, Ärztin</p>
<h2>Berufsrechtliche Angaben</h2>
<p>Gesetzliche Berufsbezeichnung: Ärztin bzw. Arzt, verliehen in der Bundesrepublik Deutschland.<br>
Zuständige Kammer: Landesärztekammer Baden-Württemberg, Jahnstraße 40, 70597 Stuttgart, <a href="https://www.aerztekammer-bw.de" rel="noopener" target="_blank">www.aerztekammer-bw.de</a></p>
<p>Es gelten die Berufsordnung der Landesärztekammer Baden-Württemberg, das Heilberufe-Kammergesetz Baden-Württemberg und die Gebührenordnung für Ärzte (GOÄ). Die Regelungen sind über die Website der Landesärztekammer abrufbar.</p>
<p>Heilpraktikerin: Aurelia Bürgler. Berufsbezeichnung Heilpraktikerin, Erlaubnis nach dem Heilpraktikergesetz. Abrechnung nach dem Gebührenverzeichnis für Heilpraktiker (GebüH).</p>
<h2>Berufshaftpflichtversicherung</h2>
<p>Allianz, Reutlingen. Räumlicher Geltungsbereich: Deutschland.</p>
<h2>Verantwortlich für den Inhalt</h2>
<p>Andreas Braig, UMI Stuttgart GmbH, {C.STRASSE}, {C.PLZ} Stuttgart</p>
<h2>Verbraucherstreitbeilegung</h2>
<p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte und Links</h2>
<p>Wir erstellen die Inhalte dieser Website mit Sorgfalt. Sie ersetzen keine ärztliche Beratung. Für Inhalte externer Websites, auf die wir verlinken, sind deren Betreiber verantwortlich. Werden uns Rechtsverletzungen bekannt, entfernen wir solche Links umgehend.</p>
<h2>Urheberrecht</h2>
<p>Texte, Bilder und Gestaltung dieser Website unterliegen dem Urheberrecht. Eine Verwendung außerhalb der Grenzen des Urheberrechts bedarf unserer Zustimmung.</p>
</div></section>"""


def datenschutz():
    return f"""<section><div class="wrap narrow legal-text">{{{{CRUMBS}}}}
<h1>Datenschutzerklärung</h1>
<p class="muted small">Entwurf für die neue Website, Stand November 2026. Er beschreibt die Seite, wie sie gebaut ist: ohne Cookies, ohne Analyse-Werkzeuge, mit Schriften vom eigenen Server. Vor dem Livegang prüfen lassen und ergänzen, sobald Analytics, Cookie-Banner oder Gutschein-Shop dazukommen.</p>
<h2>1. Verantwortlich</h2>
<p>UMI Stuttgart GmbH, {C.STRASSE}, {C.PLZ} Stuttgart, Telefon {tel()}, E-Mail <a href="mailto:{C.MAIL}">{C.MAIL}</a>.</p>
<h2>2. Aufruf der Website</h2>
<p>Beim Aufruf speichert unser Hosting-Anbieter (Host Europe GmbH) technisch notwendige Daten in Server-Protokollen: IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browser und Betriebssystem. Das dient dem sicheren Betrieb der Website (Art. 6 Abs. 1 lit. f DSGVO). Die Protokolle werden nach kurzer Zeit gelöscht. Mit dem Anbieter besteht ein Vertrag zur Auftragsverarbeitung.</p>
<h2>3. Cookies und Analyse</h2>
<p>Diese Website setzt keine Cookies und verwendet keine Analyse- oder Werbewerkzeuge. Schriften werden von unserem eigenen Server geladen.</p>
<h2>4. Kontakt per Telefon und E-Mail</h2>
<p>Wenn Sie uns anrufen oder schreiben, verarbeiten wir Ihre Angaben, um Ihre Anfrage zu beantworten (Art. 6 Abs. 1 lit. b DSGVO, bei Gesundheitsdaten Art. 9 Abs. 2 lit. h DSGVO). Bitte senden Sie uns keine Befunde unverschlüsselt per E-Mail.</p>
<h2>5. Terminbuchung über Doctolib</h2>
<p>Für die Online-Terminbuchung verlinken wir auf Doctolib. Erst wenn Sie den Link anklicken, verlassen Sie unsere Website. Für die Verarbeitung dort gilt die Datenschutzerklärung von Doctolib.</p>
<h2>6. Gutscheinkauf</h2>
<p>Der Online-Kauf von Gutscheinen läuft über einen externen Shop-Anbieter. Angaben dazu ergänzen wir mit dem Start des Shops. Beim Gutscheinkauf fragen wir nicht nach Gesundheitsdaten.</p>
<h2>7. Links zu sozialen Netzwerken</h2>
<p>Wir verlinken auf unsere Seiten bei Instagram und Facebook. Es handelt sich um einfache Links, es werden keine Daten übertragen, bevor Sie sie anklicken.</p>
<h2>8. Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, sich bei einer Aufsichtsbehörde zu beschweren, zum Beispiel beim Landesbeauftragten für den Datenschutz und die Informationsfreiheit Baden-Württemberg.</p>
</div></section>"""


def nicht_gefunden():
    return f"""{hero('Seite nicht gefunden', 'Diese Seite gibt es nicht (mehr).',
    'Vielleicht ist sie umgezogen. Hier geht es weiter:',
    a('', 'Zur Startseite', 'btn') + a('medizin/', 'UMI Medizin', 'btn ghost') + a('longevity/', 'UMI Longevity', 'btn ghost') + a('gutscheine/', 'Gutscheine', 'btn ghost'))}"""


PAGES = [
    Page("", "UMI Stuttgart · Privatpraxis und INUSpherese-Zentrum in Stuttgart",
         "Privatpraxis in Stuttgart-Vaihingen: UMI Medizin für Menschen mit Beschwerden, UMI Longevity für alle, die gesund bleiben wollen. INUSpherese, H.E.L.P., Diagnostik.",
         start),
    Page("gutscheine", "Gesundheitsgutschein Stuttgart: Wertgutscheine · UMI",
         "Schenken Sie Zeit für Gesundheit: Wertgutscheine von UMI Stuttgart ab 150 €, für alle Leistungen, 3 Jahre gültig. Sofort per E-Mail oder als Karte.",
         gutscheine, nav="gut", crumbs=[(None, "Gutscheine")]),
    Page("einloesen", "Gutschein einlösen · UMI Stuttgart",
         "So lösen Sie Ihren Wertgutschein von UMI Stuttgart ein: Termin buchen, Gutschein mitbringen, im ärztlichen Gespräch klären, was passt.",
         einloesen, nav="gut", crumbs=[("gutscheine/", "Gutscheine"), (None, "Einlösen")]),
    Page("gutscheinbedingungen", "Gutscheinbedingungen · UMI Stuttgart",
         "Bedingungen für Wertgutscheine von UMI Stuttgart: Gültigkeit, Einlösung, Restwert, Übertragbarkeit.",
         gutscheinbedingungen, crumbs=[("gutscheine/", "Gutscheine"), (None, "Bedingungen")]),
    Page("kosten", "Blutwäsche Kosten, GOÄ und Erstattung · UMI Stuttgart",
         "Was kosten Apherese, Hyperthermie und Longevity-Check? Voraussichtliche Kosten nach GOÄ, Kostenvoranschlag auf Wunsch, Hilfe beim Erstattungsantrag.",
         kosten, crumbs=[(None, "Kosten und Erstattung")]),
    Page("terminvereinbarung", "Termin vereinbaren · UMI Stuttgart",
         f"Termin bei UMI Stuttgart online über Doctolib buchen, telefonisch unter {C.TEL} oder per E-Mail. Auch Vorgespräch per Telefon oder Video.",
         termin, crumbs=[(None, "Termin und Kontakt")]),
    Page("ihr-besuch", "Ihr Besuch bei uns: Anfahrt und Ablauf · UMI Stuttgart",
         "Anfahrt, Parken und Ablauf Ihres Termins bei UMI Stuttgart in Stuttgart-Vaihingen. Was Sie mitbringen sollten und wie lange Behandlungen dauern.",
         besuch, crumbs=[(None, "Ihr Besuch bei uns")]),
    Page("ueber-uns", "Team · UMI Stuttgart",
         "Lernen Sie das Team von UMI Stuttgart kennen: Ärztinnen, Heilpraktikerin und Fachkräften mit Dialyse- und Apherese-Erfahrung.",
         team, nav="ueber", crumbs=[(None, "Über uns")]),
    Page("praxis", "Unsere Räume · UMI Stuttgart",
         "Eindrücke aus der Praxis von UMI Stuttgart in Stuttgart-Vaihingen: Empfang, Behandlungszimmer, Infusionsraum, INUSpherese-Raum.",
         praxis, nav="ueber", crumbs=[("ueber-uns/", "Über uns"), (None, "Unsere Räume")]),
    Page("karriere-stellenangebote-jobs", "Karriere und Stellenangebote · UMI Stuttgart",
         "Jobs bei UMI Stuttgart: Apheresefachkraft, Ärztin oder Arzt, Vertretung. Kleines Team, geregelte Arbeitszeiten, Stuttgart-Vaihingen.",
         karriere, nav="ueber", crumbs=[("ueber-uns/", "Über uns"), (None, "Karriere")]),
    Page("impressum", "Impressum · UMI Stuttgart", "Impressum der UMI Stuttgart GmbH.", impressum,
         crumbs=[(None, "Impressum")]),
    Page("datenschutzerklaerung-umi-stuttgart-gmbh", "Datenschutz · UMI Stuttgart",
         "Datenschutzerklärung der UMI Stuttgart GmbH.", datenschutz, crumbs=[(None, "Datenschutz")]),
    Page("404", "Seite nicht gefunden · UMI Stuttgart", "Diese Seite gibt es nicht.", nicht_gefunden),
]
