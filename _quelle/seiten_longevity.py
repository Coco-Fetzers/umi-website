"""Linie UMI Longevity (Ansprache: du)."""
from rahmen import Page, a, book, tel, faq, price
from bausteine import hero, liste, schritte, paket, team_mini, gutschein_hinweis, kosten_box
from seiten_medizin import kuren_html
import config as C

LON = [("longevity/", "UMI Longevity")]


def card(t, tag, n, d, p, more="Mehr erfahren →"):
    pr = f'<span class="price">{p}</span>' if p else ""
    return a(t, f'<span class="tag">{tag}</span><h3>{n}</h3><p>{d}</p>{pr}<span class="more">{more}</span>', "card")


def longevity():
    return f"""{hero('UMI Longevity', 'Wissen, wo du stehst. <em>Gezielt etwas tun.</em>',
    'Für Gesunde, die verstehen wollen, wie es um ihre Gesundheit steht, und dranbleiben möchten. Ärztlich begleitet, mit Messwerten statt Versprechen und einem Plan, der zu deinem Alltag passt.',
    book('Longevity-Gespräch buchen') + a('longevity/preise/', 'Alle Preise', 'btn ghost'), 'lon')}
<section class="bg-white" id="messen"><div class="wrap"><span class="eyebrow">Messen</span><h2>Wissen, wo du stehst</h2>
<div class="grid g3" style="margin-top:24px">
{card('longevity/check/', 'Start hier', 'Longevity-Check', 'Longevity-Gespräch, Labor mit ApoB, Lp(a), HbA1c, Omega-3-Index und mehr, HRV-Messung und Auswertung mit persönlichem Plan.', price('longevity_check'))}
<div class="card"><span class="tag">bald</span><h3>Longevity-Check Plus</h3><p>Der Check, erweitert um Zellenergie, Hormone, Schwermetalle, biologisches Alter und Ultraschall.</p></div>
{card('energie-check/', 'Immer müde?', 'Energie-Check', 'Wenn du dich ständig erschöpft fühlst, schauen wir in der Medizin genauer hin.', '', 'Zum Energie-Check →')}
</div></div></section>
<section id="auftanken"><div class="wrap"><span class="eyebrow">Auftanken</span><h2>Infusionen und Regeneration</h2>
<div class="grid g3" style="margin-top:24px">
{card('longevity/nad-infusion/', 'Infusion', 'NAD+-Infusion und NAD+-Kur', 'NAD+ 250 mg, einzeln oder als Kur mit 5 oder 10 Infusionen, mit ärztlichem Gespräch vor der ersten Infusion.', price('nad_infusion') + ' je Infusion')}
{card('longevity/infusionen/', 'Menü', 'Infusionsmenü', '15 Infusionen mit klaren Rezepturen, von Winter über Night Out bis NAD+. Ohne Formular vorab, mit ärztlicher Aufklärung.', 'erste Infusion ' + price('infusion_erste'))}
{card('longevity/regenerationskuren/', 'Kur', 'Regenerationskuren', 'Wärmekur, Oxyvenierung oder Farblaser: feste Termine, die du dir für Erholung freihältst.', '')}
</div></div></section>
<section class="bg-white" id="ergaenzen"><div class="wrap"><div class="grid g2">
<div><span class="eyebrow">Ergänzen</span><h2>Ernährung und Mikronährstoffe</h2>
{card('longevity/supplement-analyse/', 'Analyse', 'Supplement-Analyse', 'Was dir fehlt, was du schon nimmst und was davon sinnvoll ist. Mit schriftlichem Plan und Kontrolle nach 3 Monaten.', price('supplement_analyse'))}</div>
<div id="apherese"><span class="eyebrow">Premium</span><h2>Apherese</h2>
{card('longevity/apherese-reset/', 'Premium', 'Apherese Reset', 'Zwei Sitzungen INUSpherese oder H.E.L.P., Labor vorher und nachher, Eluat-Analyse und Auswertungsgespräch.', price('apherese_reset'))}</div>
</div></div></section>
<section id="ausgleichen"><div class="wrap"><div class="grid g2">
<div class="box"><span class="eyebrow">Ausgleichen · bald</span><h3>Stress, Schlaf, Hormone</h3><p>Stress-Messung mit HRV, Entspannungstraining und Hormonberatung für Frauen. Bis die eigenen Angebote stehen, frag gern im Longevity-Gespräch danach.</p></div>
<div class="box"><span class="eyebrow">Dranbleiben</span><h3>Check-ins</h3><p>Nach 3 oder 6 Monaten schauen wir gemeinsam, was sich verändert hat. Check-ins buchst du direkt online.</p>{book('Check-in buchen', 'btn small ghost')}</div>
</div></div></section>
<section class="bg-soft"><div class="wrap"><div class="split">
<div><h2>So arbeiten wir</h2>{schritte([
    ('Longevity-Gespräch', ' mit unserer Ärztin: deine Ziele, deine Geschichte, was du schon tust.'),
    ('Messen', ' Labor und Messungen, die über den Routine-Check hinausgehen.'),
    ('Auswertung', ' Wir erklären die Werte und machen einen Plan, der in deinen Alltag passt.'),
    ('Check-in', ' Nach einigen Monaten wird nachgemessen.')])}</div>
<div class="box"><h3>Was wir nicht tun</h3><p>Wir versprechen keine Verjüngung und keine Wunder. Longevity heißt für uns: gesund älter werden, mit Wissen statt Bauchgefühl. Jede Infusion und jede Behandlung gibt es nur nach ärztlicher Aufklärung.</p></div>
</div></div></section>
{gutschein_hinweis(True)}"""


def check():
    return paket(
        eyebrow="Paket · UMI Longevity", line="lon", du=True,
        h1="Longevity-Check in Stuttgart",
        lead="Wissen, wo du stehst. Der Longevity-Check misst, was für gesundes Älterwerden zählt: Entzündung, Blutzucker, Blutfette, Mikronährstoffe und dein Nervensystem. Danach bekommst du einen persönlichen Plan.",
        preis_html=price("longevity_check"),
        enthalten=["Longevity-Gespräch mit der Ärztin (ca. 45 Minuten)", "Longevity-Labor: Entzündung (hsCRP), HbA1c, ApoB, Lp(a), Vitamin D, B12, Ferritin, Omega-3-Index",
                   "Nervensystem-Messung (HRV)", "Auswertung mit persönlichem Plan"],
        ablauf=[("Longevity-Gespräch", " Ziele, Vorgeschichte, Lebensstil."), ("Blutabnahme und HRV", " am selben Termin, nüchtern."),
                ("Auswertung", " nach etwa zwei bis drei Wochen, vor Ort oder per Video."), ("Check-in", " nach 3 oder 6 Monaten, wenn du magst.")],
        passt=["du gesund bist und wissen willst, wo du stehst", "du gezielt etwas tun willst statt zu raten", "du Wert auf eine ärztliche Einordnung legst"],
        passt_nicht=["du akute Beschwerden hast, dann ist der Energie-Check oder ein Erstgespräch in der Medizin besser", "du nur einzelne Werte ohne Gespräch willst"],
        team=["kafle"],
        intro_extra=f"""<section class="tight"><div class="wrap"><div class="note"><b>In den Wechseljahren?</b> Viele Frauen zwischen 45 und 55 kommen mit Fragen zu Hormonen, Schlaf und Energie. Sag es uns im Gespräch, dann ergänzen wir den Check passend. Ein eigener Frauen-Balance-Check folgt im Frühjahr.</div></div></section>""",
        faqs=[("Muss ich nüchtern kommen?", "Ja, bitte komm zur Blutabnahme nüchtern. Wasser ist erlaubt."),
              ("Zahlt die Krankenversicherung?", "Vorsorge ohne Beschwerden wird in der Regel nicht erstattet. Du bekommst vorher einen Kostenvoranschlag."),
              ("Was passiert nach dem Check?", "Du bekommst einen Plan. Je nach Ergebnis kann das Ernährung, Bewegung, Mikronährstoffe, eine Infusion oder einfach ein Check-in in sechs Monaten sein."),
              ("Was ist mit dem biologischen Alter?", "Ein epigenetischer Test ist als Zusatz möglich. Was er aussagen kann und was nicht, erklären wir dir ehrlich.")],
        next_step=("Nach dem Check: gezielt auftanken.", "longevity/nad-infusion/", "Zur NAD+-Kur"))


def nad():
    return paket(
        eyebrow="Infusion · UMI Longevity", line="lon", du=True,
        h1="NAD+-Infusion und NAD+-Kur in Stuttgart",
        lead="NAD+ ist ein Coenzym, das in jeder Zelle am Energiestoffwechsel beteiligt ist. Bei UMI bekommst du NAD+ in 250 mg als Infusion, langsam über 2 bis 4 Stunden. Vor der ersten Infusion führt die Ärztin ein Gespräch mit dir. Einzeln oder als Kur mit 5 oder 10 Infusionen.",
        preis_html=price("nad_infusion") + " für die erste Infusion, jede weitere " + price("nad_weitere"),
        enthalten=["Ärztliches Gespräch vor der ersten Infusion mit Prüfung, ob NAD+ zu dir passt", "NAD+ 250 mg in ruhiger Atmosphäre, langsam über 2 bis 4 Stunden",
                   "Überwachung durch unser Pflegeteam", "Kur: 5 oder 10 Infusionen, Preis = Summe der Einzelinfusionen"],
        ablauf=[("Gesundheitsbogen und Gespräch", " 10 Minuten früher kommen, Bogen ausfüllen, dann Gespräch mit der Ärztin."), ("Erste Infusion", " langsam, damit du sie gut verträgst."),
                ("Weitere Termine", " bei einer Kur meist ein- bis zweimal pro Woche."), ("Check-in", " Wie ging es dir, wie geht es weiter?")],
        passt=["du gesund bist und deine Regeneration unterstützen willst", "du eine ärztlich begleitete Infusion suchst, keine Drip-Bar"],
        passt_nicht=["du schwanger bist oder stillst", "du unter die Anti-Doping-Regeln fällst (Infusionen über 100 ml sind dort verboten)", "du eine schnelle Wirkung erwartest"],
        team=["kafle", "buergler"],
        faqs=[("Wie lange dauert eine NAD+-Infusion?", "Etwa 2 bis 4 Stunden für 250 mg. Eine zu schnelle Gabe ist unangenehm, deshalb lassen wir uns Zeit."),
              ("Warum ist die erste Infusion teurer?", "Beim ersten Termin kommt das ärztliche Gespräch dazu. Ab der zweiten Infusion fällt es weg, das ist kein Rabatt."),
              ("Ist NAD+ sicher?", "Infusionen sind ein medizinischer Eingriff. Häufig sind Druckgefühl, Übelkeit oder Kreislaufreaktionen, wenn NAD+ zu schnell läuft. Deshalb gibt es NAD+ bei uns nur nach ärztlichem Gespräch, langsam und unter Aufsicht."),
              ("Wie viele Infusionen brauche ich?", "Das besprechen wir vor der ersten Infusion. Viele starten mit einer einzelnen Infusion. Eine Kur kostet die Summe der Einzelinfusionen.")],
        next_step=("Noch mehr wissen?", "longevity/infusionen/", "Zum Infusionsmenü"))


INFUSIONEN = [
    # (Name, Inhalt, Preis-Schlüssel in config.INFUSIONSPREISE)
    ("Winter", "Vitamin C, Zink, Lysin", "winter"),
    ("Winter Plus", "Vitamin C, Zink, Lysin, Glutathion, Aminosäuren, Vitamine", "winter_plus"),
    ("Myers-Infusion", "Vitamin C, B-Vitamine, Folsäure", "myers"),
    ("Recharge", "Mikronährstoff-Rezeptur, als Fertigpräparat oder nach Protokoll der Praxis", "recharge"),
    ("Recharge Plus", "erweiterte Mikronährstoff-Rezeptur", "recharge_plus"),
    ("Sport", "vier Aminosäuren", "sport"),
    ("Sport Plus", "L-Carnitin, Glutathion, Mineralien, Vitamin C, B-Vitamine u. a.", "sport_plus"),
    ("Night Out", "Flüssigkeit mit Elektrolyten, B-Vitamine, Vitamin C, Magnesium", "night_out"),
    ("Longevity Basis", "Rezeptur nach Protokoll der Praxis", "longevity_basis"),
    ("Longevity Plus", "erweiterte Rezeptur mit Glutathion und Aminosäuren", "longevity_plus"),
    ("Longevity Premium", "mit Spermidin oder Polyphenolen", "longevity_premium"),
    ("Glow", "Rezeptur für Haut und Haar mit Glutathion", "glow"),
    ("Glow Plus", "Rezeptur für Haut und Haar mit Spermidin", "glow_plus"),
    ("Mito", "Mitochondrien-Rezeptur, auf Wunsch mit Spermidin", "mito"),
    ("NAD+", "NAD+ 250 mg, langsam über 2 bis 4 Stunden", "nad"),
]


def infusionen():
    def one(v):
        return v.replace(" €", "&nbsp;€") if v else '<span class="preis-offen" title="Preis folgt nach Freigabe">…&nbsp;€</span>'
    def name(n):
        return "<b>" + (a("longevity/nad-infusion/", n) if n == "NAD+" else n) + "</b>"
    rows = "".join(f'<tr><td>{name(n)}</td><td style="font-weight:400;white-space:normal">{i}</td><td style="white-space:nowrap">{one(C.INFUSIONSPREISE[k][0])}</td><td style="white-space:nowrap">{one(C.INFUSIONSPREISE[k][1]) if C.INFUSIONSPREISE[k][1] != "-" else "–"}</td></tr>' for n, i, k in INFUSIONEN)
    fh, fld = faq([
        ("Was bedeutet „Plus“?", "Die Plus-Varianten haben eine erweiterte Rezeptur mit aufwendigeren Präparaten. Deshalb prüft die Ärztin vor der ersten Infusion Rezeptur und Dosierung."),
        ("Muss ich vorher ein Formular ausfüllen?", "Nein. Komm zur ersten Infusion einfach 10 Minuten früher. Den kurzen Gesundheitsbogen füllst du bei uns aus, danach klärt dich die Ärztin oder unsere Heilpraktikerin persönlich auf."),
        ("Brauche ich vorher einen eigenen Termin für ein Gespräch?", "Meist nicht. Bei Recharge und NAD+ führt die Ärztin vor der ersten Infusion ein ausführlicheres Gespräch, das planen wir bei der Buchung mit ein. Ein ausführliches Gespräch kannst du dir bei jeder Infusion wünschen."),
        ("Warum ist die erste Infusion teurer?", "In der ersten Infusion steckt die ärztliche Aufklärung, bei manchen Infusionen auch die Prüfung von Rezeptur und Dosierung oder ein Gespräch. Ab der zweiten Infusion fällt das weg. Das ist kein Rabatt."),
    ])
    body = f"""{hero('Auftanken · UMI Longevity', 'Infusionsmenü in Stuttgart',
    '15 Infusionen mit klaren Inhaltsstoffen, von Winter bis NAD+. Ohne Formular vorab: Du kommst zur ersten Infusion 10 Minuten früher, füllst bei uns einen kurzen Gesundheitsbogen aus, und die Ärztin klärt dich vor der Infusion persönlich auf.',
    book('Infusion buchen') + a('longevity/nad-infusion/', 'NAD+', 'btn ghost'), 'lon',
    f'<p class="price-line"><b>Erste Infusion {price("infusion_erste")}, jede weitere {price("infusion_weitere")}</b> · nach GOÄ</p>')}
<section class="bg-white"><div class="wrap"><div class="split wide">
<div><div class="table-wrap"><table class="price-table"><tr><th>Infusion</th><th>Inhalt</th><th>erste ab</th><th>weitere ab</th></tr>{rows}</table></div><p class="small muted" style="margin-top:10px">Die erste Infusion enthält die ärztliche Aufklärung, deshalb kostet jede weitere weniger. Das ist kein Rabatt. Eine Kur kostet die Summe der Einzelinfusionen. Alle Preise sind voraussichtliche Kosten nach GOÄ und können je nach Rezeptur abweichen.</p></div>
<div><div class="box" style="margin-bottom:16px"><h3>So läuft deine erste Infusion</h3>{schritte([
    ('Buchen', ' online oder am Telefon, ohne Formular.'),
    ('10 Minuten früher kommen', ' und den kurzen Gesundheitsbogen ausfüllen.'),
    ('Aufklärung', ' Die Ärztin oder unsere Heilpraktikerin geht den Bogen mit dir durch und klärt dich auf.'),
    ('Infusion', ' in Ruhe, unter Aufsicht. Ab dem zweiten Mal reicht ein kurzer Check am Empfang.')])}</div>
<div class="box" style="margin-bottom:16px"><h3>Warum ärztlich?</h3><p>Das Bundesinstitut für Arzneimittel hat 2026 vor unkontrollierten Infusionen in Drip-Bars gewarnt. Bei uns gibt es jede Infusion nur nach ärztlicher Aufklärung, mit Prüfung von Gegenanzeigen und unter Aufsicht. Wir versprechen keine Wirkung.</p></div>
{kosten_box(True)}</div></div></div></section>
{team_mini(['kafle', 'buergler'], True)}{fh}{gutschein_hinweis(True)}"""
    return body, [fld]


def regeneration_lon():
    body = f"""{hero('Auftanken · UMI Longevity', 'Regenerationskuren: Zeit für Erholung',
    'Feste Termine, die du dir für dich freihältst. Wärmekur, Oxyvenierung oder Farblaser, jeweils als Kur mit festem Ablauf und nach ärztlichem Vorgespräch.',
    book('Vorgespräch buchen') + a('ganzkoerperhyperthermie/', 'Mehr zur Hyperthermie', 'btn ghost'), 'lon')}
<section class="bg-white"><div class="wrap"><div class="grid g3">{kuren_html(True)}</div></div></section>
<section><div class="wrap"><div class="split"><div><h2>So läuft eine Kur ab</h2>{schritte([
    ('Vorgespräch', ' Passt die Kur zu dir? Gibt es Gegenanzeigen?'), ('Termine', ' über einige Wochen, ein- bis zweimal pro Woche.'),
    ('Check-in', ' Wie ging es dir, was machst du weiter?')])}</div>{kosten_box(True)}</div></div></section>
{gutschein_hinweis(True)}"""
    return body


def supplement():
    return paket(
        eyebrow="Ergänzen · UMI Longevity", line="lon", du=True,
        h1="Supplement-Analyse: was du wirklich brauchst",
        lead="Viele nehmen Nahrungsergänzung nach Gefühl. Die Supplement-Analyse misst deinen Mikronährstoffstatus, prüft deine Präparate und macht daraus einen schriftlichen Plan.",
        preis_html=price("supplement_analyse"),
        enthalten=["Gespräch zu Ernährung und bisherigen Präparaten", "Mikronährstoffstatus im Blut (Vitamine, Mineralstoffe, Spurenelemente)",
                   "Prüfung der Präparate, die du schon nimmst", "Schriftlicher Plan", "Kontrollwerte nach 3 Monaten"],
        ablauf=[("Gespräch", " Bring deine Präparate oder Fotos der Packungen mit."), ("Blutabnahme", " am selben Termin."),
                ("Plan", " Was weg kann, was fehlt, in welcher Dosis."), ("Kontrolle", " nach 3 Monaten.")],
        passt=["du Nahrungsergänzung nimmst oder nehmen willst", "du wissen willst, ob sie sinnvoll ist", "du vegan oder vegetarisch lebst"],
        passt_nicht=["du Beschwerden abklären lassen möchtest, dann ist UMI Medizin der bessere Start"],
        team=["kafle", "buergler"],
        faqs=[("Verkauft ihr Supplemente?", "Nein. Wir empfehlen, was sinnvoll ist, du kaufst, wo du willst."),
              ("Brauche ich vorher den Longevity-Check?", "Nein, die Supplement-Analyse geht auch allein. Beides zusammen ergänzt sich gut.")],
        next_step=("Mehr als Mikronährstoffe messen?", "longevity/check/", "Zum Longevity-Check"))


def reset():
    return paket(
        eyebrow="Premium · UMI Longevity", line="lon", du=True,
        h1="Apherese Reset in Stuttgart",
        lead="Die Apherese filtert das Blutplasma außerhalb des Körpers. Im Apherese Reset verbinden wir zwei Sitzungen INUSpherese oder H.E.L.P. mit Labor vorher und nachher, Eluat-Analyse und einem Auswertungsgespräch. Für Gesunde, ärztlich begleitet.",
        preis_html=price("apherese_reset"),
        enthalten=["Vorgespräch mit der Ärztin", "Labor vorher und nachher (Entzündung, Blutfette, Schadstoffe)", "2 Sitzungen INUSpherese oder H.E.L.P.-Apherese",
                   "Eluat-Analyse", "Auswertungsgespräch"],
        ablauf=[("Vorgespräch", " Passt die Apherese zu dir? Aufklärung über Ablauf und Risiken."), ("Labor", " Ausgangswerte."),
                ("Zwei Sitzungen", " je etwa zwei bis drei Stunden, im Abstand von zwei bis drei Tagen."), ("Auswertung", " Eluat-Analyse und Labor danach, gemeinsam besprochen.")],
        passt=["du gesund bist und dich für die Apherese interessierst", "du Messwerte vorher und nachher sehen willst", "du dir zwei Behandlungstage freihalten kannst"],
        passt_nicht=["du schwanger bist", "Gegenanzeigen dagegen sprechen, das prüfen wir im Vorgespräch"],
        team=["kafle", "gusic", "gentsch"],
        intro_extra=f"""<section class="tight"><div class="wrap"><div class="grid g2">
<div class="box"><h3>INUSpherese einzeln</h3><p>Doppelmembran-Filtration des Plasmas, ca. 2 bis 3 Stunden, mit Vorgespräch. Voraussichtlich {price('apherese_sitzung', '')} je Sitzung.</p></div>
<div class="box"><h3>H.E.L.P.-Apherese einzeln</h3><p>Senkt gezielt LDL-Cholesterin, Lp(a) und Fibrinogen. Mit Vorgespräch, Preis nach Kostenvoranschlag.</p></div>
</div></div></section>""",
        faqs=[("Warum kostet der Reset nicht mehr als das Apherese-Programm?", "Es ist dieselbe Behandlung. Der Unterschied liegt in Begleitdiagnostik und Ziel, nicht in der Apherese selbst."),
              ("Zahlt die Versicherung?", "Bei Anwendung ohne medizinischen Anlass in der Regel nicht."),
              ("Was zeigt die Eluat-Analyse?", "Welche Bestandteile der Filter zurückgehalten hat. Was das für dich bedeutet, besprechen wir in der Auswertung.")],
        next_step=("Erst einmal wissen, wo du stehst?", "longevity/check/", "Zum Longevity-Check"))


def preise():
    rows = [
        ("longevity/check/", "Longevity-Check", "Gespräch, Labor, HRV, Auswertung", price("longevity_check")),
        ("longevity/supplement-analyse/", "Supplement-Analyse", "Mikronährstoffe, Plan, Kontrolle nach 3 Monaten", price("supplement_analyse")),
        ("longevity/nad-infusion/", "NAD+-Infusion, 250 mg", "erste Infusion mit ärztlichem Gespräch, jede weitere " + price("nad_weitere") + ", Kur = Summe der Einzelinfusionen", price("nad_infusion")),
        ("longevity/infusionen/", "Infusionsmenü, erste Infusion", "je nach Infusion, mit ärztlicher Aufklärung", price("infusion_erste")),
        ("longevity/infusionen/", "Infusionsmenü, jede weitere", "je nach Infusion", price("infusion_weitere")),
        ("longevity/regenerationskuren/", "Wärmekur", "Ganzkörperhyperthermie, 6 Sitzungen", price("kur_hyperthermie")),
        ("longevity/regenerationskuren/", "Oxyvenierung", "12 Sitzungen", price("kur_oxyvenierung")),
        ("longevity/regenerationskuren/", "Farblaser", "12 Sitzungen", price("kur_farblaser")),
        ("longevity/apherese-reset/", "Apherese Reset", "2 Sitzungen, Labor, Eluat-Analyse, Auswertung", price("apherese_reset")),
        ("inuspherese-zentrum-stuttgart/", "INUSpherese einzeln", "je Sitzung", price("apherese_sitzung", "")),
    ]
    tr = "".join(f'<tr><td>{a(t, n)}<br><span class="small muted">{d}</span></td><td>{p}</td></tr>' for t, n, d, p in rows)
    return f"""{hero('UMI Longevity', 'Preise auf einen Blick',
    'Alle Preise sind voraussichtliche Kosten nach der Gebührenordnung für Ärzte (GOÄ). Vor dem Start bekommst du einen schriftlichen Kostenvoranschlag. Rabatte gibt es bei uns nicht, dafür klare Preise.',
    book('Termin buchen') + a('kosten/', 'Kosten und Erstattung', 'btn ghost'), 'lon')}
<section class="bg-white"><div class="wrap narrow"><table class="price-table"><tr><th>Angebot</th><th>voraussichtlich</th></tr>{tr}</table>
<p class="small muted" style="margin-top:14px">Vorsorgeleistungen werden von privaten Krankenversicherungen in der Regel nicht erstattet. Ob Umsatzsteuer anfällt, hängt von der Leistung ab.</p></div></section>
{gutschein_hinweis(True)}"""


PAGES = [
    Page("longevity", "Longevity Stuttgart: ärztlich begleitet · UMI Longevity",
         "UMI Longevity in Stuttgart: Longevity-Check, NAD+-Infusion, Infusionsmenü, Supplement-Analyse und Apherese Reset. Ärztlich, mit Messwerten statt Versprechen.",
         longevity, line="lon", nav="lon", crumbs=[(None, "UMI Longevity")]),
    Page("longevity/check", "Longevity-Check Stuttgart · UMI Longevity",
         "Longevity-Check in Stuttgart: Longevity-Gespräch, Labor mit ApoB, Lp(a), HbA1c, Omega-3-Index, HRV und persönlichem Plan. Jetzt online buchen.",
         check, line="lon", nav="lon", crumbs=LON + [(None, "Longevity-Check")]),
    Page("longevity/nad-infusion", "NAD+ Infusion Stuttgart · UMI Longevity",
         "NAD+-Infusion (250 mg) und NAD+-Kur in Stuttgart, mit ärztlichem Gespräch und unter Aufsicht. Ablauf, Dauer und voraussichtliche Kosten ab 489 €.",
         nad, line="lon", nav="lon", crumbs=LON + [(None, "NAD+")]),
    Page("longevity/infusionen", "Infusionstherapie Stuttgart: Infusionsmenü · UMI",
         "Infusionsmenü bei UMI Stuttgart: 15 Infusionen von Winter bis NAD+, mit ärztlicher Aufklärung, ohne Formular vorab. Preise ab 124 €.",
         infusionen, line="lon", nav="lon", crumbs=LON + [(None, "Infusionsmenü")]),
    Page("longevity/regenerationskuren", "Regenerationskuren · UMI Longevity Stuttgart",
         "Wärmekur, Oxyvenierung oder Farblaser als Kur mit festen Terminen bei UMI Longevity in Stuttgart. Nach ärztlichem Vorgespräch.",
         regeneration_lon, line="lon", nav="lon", crumbs=LON + [(None, "Regenerationskuren")]),
    Page("longevity/supplement-analyse", "Mikronährstoffanalyse Stuttgart · UMI Longevity",
         "Supplement-Analyse bei UMI Stuttgart: Mikronährstoffstatus messen, eigene Präparate prüfen, schriftlicher Plan und Kontrolle nach 3 Monaten.",
         supplement, line="lon", nav="lon", crumbs=LON + [(None, "Supplement-Analyse")]),
    Page("longevity/apherese-reset", "Apherese Reset: Blutwäsche für Gesunde · UMI",
         "Apherese Reset in Stuttgart: zwei Sitzungen INUSpherese oder H.E.L.P., Labor vorher und nachher, Eluat-Analyse, Auswertung. Ärztlich begleitet.",
         reset, line="lon", nav="lon", crumbs=LON + [(None, "Apherese Reset")]),
    Page("longevity/preise", "Preise UMI Longevity Stuttgart",
         "Alle Preise von UMI Longevity auf einen Blick: Longevity-Check, NAD+, Infusionen, Kuren, Apherese Reset. Voraussichtliche Kosten nach GOÄ.",
         preise, line="lon", nav="lon", crumbs=LON + [(None, "Preise")]),
]
