"""Linie UMI Medizin (Ansprache: Sie) und die gemeinsame Apherese-Seite."""
from rahmen import Page, a, book, tel, faq, price
from bausteine import hero, liste, schritte, paket, team_mini, gutschein_hinweis, kosten_box
from seiten_dach import schema_svg
import config as C

MED = [("medizin/", "UMI Medizin")]


# ------------------------------------------------------------ Einstieg

SCHWERPUNKTE = [
    ("ganzheitliche-sprechstunde/", "Ganzheitliche Medizin", "Für alle, die nicht wissen, wo sie hinsollen. Wir nehmen Ihre ganze Geschichte auf und suchen nach Zusammenhängen."),
    ("internistische-sprechstunde/", "Innere Medizin", "Abklärung mit Labor, EKG und Ultraschall. Auch als Vorsorge-Untersuchung."),
    ("sub-health-syndrom/", "Erschöpfung und Energie", "Immer müde, aber die Werte sind normal? Wir schauen genauer hin, bis zum Energie-Check."),
    ("long-covid-sprechstunde/", "Beschwerden nach Infektionen", "Wenn Beschwerden nach einer Infektion oder Impfung bleiben. Gründliche Abklärung und Begleitung."),
]


def medizin():
    sp = "".join(a(t, f'<span class="tag">Schwerpunkt</span><h3>{n}</h3><p>{d}</p><span class="more">Mehr erfahren →</span>', "card") for t, n, d in SCHWERPUNKTE)
    sp += ('<div class="card"><span class="tag">Weitere Schwerpunkte</span><h3>Schmerz, Frauengesundheit, Kinder</h3>'
           '<p>Mit unserer Heilpraktikerin und unserer Ärztin. Buchbar als Erstgespräch, Seiten folgen.</p></div>')
    pk = "".join(a(t, f'<span class="tag">Paket</span><h3>{n}</h3><p>{d}</p><span class="price">{p}</span><span class="more">Zum Paket →</span>', "card") for t, n, d, p in [
        ("medizin/apherese-programm/", "Apherese-Programm", "Vorgespräch, Diagnostik, zwei Sitzungen INUSpherese oder H.E.L.P., Eluat-Analyse und Nachgespräch.", price("apherese_programm")),
        ("energie-check/", "Energie-Check", "Gründliche Abklärung bei anhaltender Erschöpfung, mit Befundgespräch und Therapieplan.", price("energie_check")),
        ("medizin/regenerationskuren/", "Regenerationskuren", "Ganzkörperhyperthermie, Oxyvenierung oder Farblaser als Kur mit festem Ablauf.", price("kur_oxyvenierung")),
    ])
    return f"""{hero('UMI Medizin', 'Ursachen finden.',
    'Für Menschen mit anhaltenden Beschwerden, die eine gründliche Abklärung suchen und eine Therapie, die es in Stuttgart sonst kaum gibt. Wir verbinden schulmedizinische Diagnostik mit Umweltmedizin, Apherese und Naturheilkunde.',
    book('Erstgespräch buchen') + tel('btn ghost', 'Anrufen: ' + C.TEL), 'med')}
<section class="bg-white" id="schwerpunkte"><div class="wrap">
<span class="eyebrow">Schwerpunkte · früher „Sprechstunden“</span><h2>Wo fangen wir an?</h2>
<p class="lead">In jedem Schwerpunkt beginnt die Behandlung mit einem ausführlichen Erstgespräch. Danach folgen Diagnostik und ein Plan mit Kostenvoranschlag.</p>
<div class="grid g3" style="margin-top:28px">{sp}</div></div></section>
<section><div class="wrap"><span class="eyebrow">Pakete</span><h2>Klare Abläufe, voraussichtliche Kosten vorab</h2>
<div class="grid g3" style="margin-top:28px">{pk}</div></div></section>
<section class="bg-white"><div class="wrap"><div class="grid g3">
{a('inuspherese-zentrum-stuttgart/', '<span class="tag">Apherese</span><h3>INUSpherese und H.E.L.P.</h3><p>Blutplasma-Filtration im einzigen INUSpherese-Zentrum in Stuttgart.</p><span class="more">Zur Apherese →</span>', 'card')}
{a('labordiagnostik/', '<span class="tag">Diagnostik</span><h3>Genau hinschauen</h3><p>Immunstatus, Entzündung, Zellenergie, Mikronährstoffe, Umweltbelastungen und mehr.</p><span class="more">Zur Diagnostik →</span>', 'card')}
{a('ganzkoerperhyperthermie/', '<span class="tag">Regeneration</span><h3>Ganzkörperhyperthermie</h3><p>Kontrollierte Erwärmung des Körpers, ärztlich überwacht.</p><span class="more">Zur Hyperthermie →</span>', 'card')}
</div>
<div class="split" style="margin-top:48px">
<div><h2>Begleittherapien</h2><p>Nach ärztlicher Empfehlung: Infusionstherapie, Akupunktur, Neuraltherapie, Darmaufbau, Hormontherapie, Stress- und Entspannungstherapie sowie Naturheilkunde bei unserer Heilpraktikerin Aurelia Bürgler.</p></div>
<div class="box"><h3>Für Angehörige</h3><p>Sie suchen Hilfe für Ihre Mutter, Ihren Vater oder Ihren Partner? Im <b>Angehörigengespräch</b> klären wir Ihre Fragen, auch zu Belastung, Ablauf und Anreise. Termine können Sie auch für eine andere Person buchen.</p>{tel('btn small ghost', 'Anrufen')}</div>
</div></div></section>
<section><div class="wrap"><div class="hint"><p><b>Noch unsicher?</b> Im Vorgespräch am Telefon oder per Video klären wir, ob wir Ihnen weiterhelfen können.</p>{book('Vorgespräch buchen', 'btn small')}</div></div></section>"""


# ------------------------------------------------------------ Schwerpunkte

def schwerpunkt(eyebrow, h1, lead, wer, ablauf, faqs, weiter):
    fh, fld = faq(faqs)
    body = f"""{hero(eyebrow, h1, lead, book('Erstgespräch buchen') + tel('btn ghost', 'Anrufen'), 'med')}
<section class="bg-white"><div class="wrap"><div class="split">
<div><h2>Für wen dieser Schwerpunkt da ist</h2>{liste(wer)}</div>
<div><h2>So gehen wir vor</h2>{schritte(ablauf)}</div></div></div></section>
<section><div class="wrap"><div class="grid g2">{weiter}{kosten_box()}</div></div></section>
{team_mini(['kafle', 'buergler'])}
{fh}{gutschein_hinweis()}"""
    return body, [fld]


ABLAUF_STD = [
    ("Erstgespräch", " Ausführliche Anamnese und körperliche Untersuchung, etwa 45 bis 60 Minuten."),
    ("Diagnostik", " Gezielte Laboruntersuchungen und Messungen, je nach Fragestellung."),
    ("Befundgespräch", " Wir erklären die Ergebnisse und schlagen einen Plan mit Kostenvoranschlag vor."),
    ("Begleitung", " Therapie und Folgetermine, mit festen Ansprechpartnerinnen."),
]


def ganzheitlich():
    return schwerpunkt("Schwerpunkt · UMI Medizin", "Ganzheitliche Medizin in Stuttgart",
        "Viele Beschwerden passen in keine Schublade. Im Schwerpunkt Ganzheitliche Medizin nehmen wir uns Zeit für Ihre ganze Geschichte und verbinden schulmedizinische Diagnostik mit naturheilkundlichen Verfahren.",
        ["Sie haben mehrere Beschwerden und bisher keine Erklärung gefunden", "Sie wünschen sich eine Ärztin, die zuhört und Zusammenhänge sucht",
         "Sie möchten Schulmedizin und Naturheilkunde verbinden", "Sie wissen nicht, welcher Schwerpunkt der richtige ist"],
        ABLAUF_STD,
        [("Was ist der Unterschied zur Inneren Medizin?", "Die Innere Medizin klärt gezielt Organe und Stoffwechsel ab. Die Ganzheitliche Medizin ist der breitere Einstieg und bezieht Lebensumstände, Umwelt und Naturheilkunde mit ein."),
         ("Bringe ich Vorbefunde mit?", "Ja, bitte. Arztbriefe, Laborwerte und eine Liste Ihrer Medikamente helfen uns, nichts doppelt zu machen."),
         ("Wie lange dauert das Erstgespräch?", "In der Regel 45 bis 60 Minuten.")],
        a("labordiagnostik/", '<span class="tag">Weiter</span><h3>Diagnostik</h3><p>Welche Laborbausteine wir einsetzen und wofür.</p><span class="more">Zur Diagnostik →</span>', "card"))


def internistisch():
    return schwerpunkt("Schwerpunkt · UMI Medizin", "Innere Medizin in Stuttgart-Vaihingen",
        "Gründliche internistische Abklärung mit Labor, Ruhe-EKG und Ultraschall der Bauchorgane. Für die Klärung von Beschwerden und als ausführliche Vorsorge-Untersuchung.",
        ["Sie möchten Beschwerden internistisch abklären lassen", "Sie wünschen eine ausführliche Vorsorge-Untersuchung als Privatpatient oder Selbstzahler",
         "Sie suchen eine zweite Meinung zu Befunden"],
        [("Erstgespräch und Untersuchung", " Anamnese, körperliche Untersuchung, Blutdruck, Puls und Sauerstoffsättigung."),
         ("Technische Untersuchungen", " Ruhe-EKG, Ultraschall der Bauchorgane und Nieren, Lungenfunktion nach Bedarf."),
         ("Labor", " Organscreening von Leber, Niere und Schilddrüse, erweitert je nach Fragestellung."),
         ("Befundgespräch", " Ergebnisse, Empfehlungen und, wenn nötig, ein Therapieplan.")],
        [("Ersetzt das den Hausarzt?", "Nein. Wir arbeiten gern mit Ihrer Hausärztin oder Ihrem Hausarzt zusammen und schicken auf Wunsch einen Befundbericht."),
         ("Wird die Untersuchung erstattet?", "Bei medizinischem Anlass erstatten private Versicherungen und Beihilfe in der Regel nach ihren Bedingungen. Reine Vorsorge oft nur teilweise.")],
        a("energie-check/", '<span class="tag">Passend dazu</span><h3>Energie-Check</h3><p>Bei anhaltender Erschöpfung ohne klaren Befund.</p><span class="more">Zum Energie-Check →</span>', "card"))


def subhealth():
    return schwerpunkt("Schwerpunkt · UMI Medizin", "Erschöpfung und Energie: wenn Sie ständig müde sind",
        "Viele Menschen fühlen sich dauerhaft erschöpft, obwohl die Routinewerte unauffällig sind. Diese Beschwerden zwischen den Befunden nehmen wir ernst. Wir suchen wir gezielt nach Ursachen, etwa in Zellenergie, Mikronährstoffen, Hormonen und Stressregulation.",
        ["Sie sind seit Monaten müde und erschöpft", "Die Werte beim Hausarzt sind „normal“", "Schlaf und Urlaub bringen keine Erholung mehr",
         "Sie möchten verstehen, woran es liegt, bevor Sie etwas einnehmen"],
        ABLAUF_STD,
        [("Was ist der Energie-Check?", f"Ein festes Paket mit Erstgespräch, Neurostress-Profil, Zellenergie, Mikronährstoffen, Schilddrüse, HRV-Messung und Befundgespräch. Voraussichtlich {price('energie_check')}."),
         ("Früher hieß das Sub-Health-Sprechstunde?", "Ja. Inhaltlich ist es dasselbe, der neue Name sagt besser, worum es geht.")],
        a("energie-check/", '<span class="tag">Paket</span><h3>Energie-Check</h3><p>Alle wichtigen Bausteine in einem Ablauf, mit Therapieplan.</p><span class="more">Zum Energie-Check →</span>', "card"))


def infektionen():
    return schwerpunkt("Schwerpunkt · UMI Medizin", "Beschwerden nach Infektionen",
        "Manche Beschwerden bleiben nach einer Infektion oder Impfung über Wochen und Monate bestehen, etwa Erschöpfung, Konzentrationsprobleme oder Belastungsintoleranz. Wir klären gründlich ab und begleiten Sie mit einem Plan, der zu Ihrer Belastbarkeit passt.",
        ["Ihre Beschwerden bestehen seit einer Infektion oder Impfung", "Sie haben schon viele Untersuchungen hinter sich, ohne Erklärung",
         "Sie suchen eine Praxis, die sich mit anhaltender Erschöpfung auskennt", "Sie möchten wissen, ob eine Apherese für Sie in Frage kommt"],
        [("Vorgespräch", " Am Telefon oder per Video, wenn die Anreise anstrengend ist."),
         ("Erstgespräch", " Ausführliche Anamnese, Untersuchung, Sichtung Ihrer Vorbefunde."),
         ("Diagnostik", " Je nach Bild Immunstatus, Entzündungswerte, Zellenergie, Nervensystem-Messung."),
         ("Plan", " Schonend, schrittweise, mit Kostenvoranschlag. Ob eine Apherese sinnvoll sein kann, besprechen wir offen.")],
        [("Behandeln Sie Long-COVID und Post-Vac?", "Wir betreuen Menschen mit anhaltenden Beschwerden nach Infektionen und Impfungen. Welche Diagnostik und Behandlung in Ihrem Fall sinnvoll ist, klären wir im Erstgespräch. Eine Heilung können wir nicht versprechen."),
         ("Kann ich das Gespräch per Video führen?", "Ja, das Vorgespräch ist per Telefon oder Video möglich."),
         ("Was ist mit der Apherese?", "Die Apherese ist eine von mehreren Möglichkeiten. Ob sie für Sie in Frage kommt, prüfen wir im Beratungsgespräch. Für einige Anwendungen ist sie nicht zugelassen. Darüber klären wir Sie vorher auf.")],
        a("inuspherese-zentrum-stuttgart/", '<span class="tag">Therapie</span><h3>Apherese</h3><p>Wie INUSpherese und H.E.L.P. funktionieren.</p><span class="more">Zur Apherese →</span>', "card"))


# ------------------------------------------------------------ Apherese (Dach)

def apherese():
    fh, fld = faq([
        ("Was ist eine Blutwäsche?", "„Blutwäsche“ ist der Alltagsbegriff für die Apherese. Dabei wird Blut außerhalb des Körpers in Blutzellen und Plasma getrennt, das Plasma gefiltert und anschließend zurückgegeben. Mit Dialyse oder einem Plasmaaustausch ist sie nicht gleichzusetzen."),
        ("Wie lange dauert eine Sitzung?", "Etwa zwei bis drei Stunden. Sie liegen bequem, wir überwachen Kreislauf und Werte die ganze Zeit."),
        ("Wie viele Sitzungen sind sinnvoll?", "Häufig werden zwei Sitzungen im Abstand von zwei bis drei Tagen empfohlen. Wie viele es bei Ihnen sind, besprechen wir im Vorgespräch."),
        ("Ist die Apherese anstrengend?", "Die meisten empfinden sie als gut verträglich. Über mögliche Nebenwirkungen und Risiken klären wir Sie vorher genau auf."),
        ("Was kostet die Apherese?", f"Eine Sitzung INUSpherese kostet voraussichtlich {price('apherese_sitzung', '')}, das Apherese-Programm voraussichtlich {price('apherese_programm')}. Die genauen Kosten stehen in Ihrem Kostenvoranschlag."),
        ("Zahlt die Krankenversicherung?", "Private Krankenversicherungen und Beihilfe erstatten bei medizinischem Anlass teilweise. Wir helfen Ihnen beim Antrag. Bei Anwendung zur Vorsorge wird in der Regel nicht erstattet."),
        ("Was ist die Eluat-Analyse?", "Die abgefilterten Bestandteile werden im Labor untersucht. So sehen Sie, was sich in Ihrem Fall herausfiltern ließ."),
    ])
    proc = {"@context": "https://schema.org", "@type": "MedicalTherapy", "name": "INUSpherese",
            "alternateName": ["Blutwäsche", "Doppelfiltrations-Plasmapherese"],
            "description": "Ambulante Filtration des Blutplasmas mit Doppelmembranfiltern bei UMI Stuttgart."}
    body = f"""{hero('Apherese in Stuttgart · INUSpherese-Zentrum', 'INUSpherese und H.E.L.P.-Apherese in Stuttgart',
    'Bei der Apherese, oft „Blutwäsche“ genannt, wird das Blutplasma außerhalb des Körpers gefiltert. UMI Stuttgart ist seit 2023 zertifizierter INUS-Partner und bietet in Stuttgart als einzige Praxis INUSpherese und H.E.L.P.-Apherese an. Ambulant, etwa zwei bis drei Stunden je Sitzung.',
    book('Beratungsgespräch buchen') + a('kosten/', 'Kosten', 'btn ghost'), 'dach',
    f'<p class="price-line"><b>Sitzung INUSpherese voraussichtlich {price("apherese_sitzung", "")}</b> · nach GOÄ, mit Kostenvoranschlag</p>')}
<section class="bg-white"><div class="wrap"><div class="split">
<div><h2>Wie funktioniert die Apherese?</h2>
<p>Über eine Vene am Arm wird Blut entnommen. Ein erster Filter trennt das Plasma von den Blutzellen. Das Plasma läuft durch einen zweiten, feineren Filter, der bestimmte große Bestandteile zurückhält, zum Beispiel Fette, Eiweißkomplexe und Entzündungsbotenstoffe. Das gefilterte Plasma fließt zusammen mit den Blutzellen über die andere Armvene zurück.</p>
<p>Weil das eigene Plasma zurückgegeben wird, ist keine Ersatzlösung nötig. Das unterscheidet die INUSpherese vom Plasmaaustausch.</p></div>
<div class="svg-schema">{schema_svg()}</div></div></div></section>
<section id="ablauf"><div class="wrap"><div class="split">
<div><h2>Wie läuft die Behandlung ab?</h2>{schritte([
    ('Beratungsgespräch', ' Unsere Ärztin prüft, ob eine Apherese für Sie in Frage kommt, und klärt Sie über Nutzen und Risiken auf.'),
    ('Voruntersuchung', ' Labor und Untersuchung vor der ersten Sitzung, Kostenvoranschlag.'),
    ('Behandlung', ' Etwa zwei bis drei Stunden, im Liegen, mit ständiger Überwachung durch unser Pflegeteam mit Dialyse-Erfahrung.'),
    ('Eluat-Analyse', ' Auf Wunsch untersuchen wir, was der Filter zurückgehalten hat.'),
    ('Nachgespräch', ' Ergebnisse, Verlauf und die Frage, ob weitere Sitzungen sinnvoll sind.'),
])}</div>
<div id="unterscheidung"><h2>INUSpherese oder H.E.L.P.?</h2>
<div class="box" style="margin-bottom:16px"><h3>INUSpherese</h3><p>Doppelmembran-Filtration des Plasmas (DFPP). Die Filter halten große Moleküle zurück. Entwickelt und zertifiziert vom INUS Medical Center in Cham, mit dem wir zusammenarbeiten.</p></div>
<div class="box"><h3>H.E.L.P.-Apherese</h3><p>Heparin-induzierte extrakorporale LDL-Präzipitation. Sie senkt gezielt LDL-Cholesterin, Lipoprotein(a) und Fibrinogen und ist bei schweren Fettstoffwechselstörungen ein etabliertes Verfahren.</p></div>
<p class="small muted" style="margin-top:12px">Welches Verfahren passt, entscheidet die Ärztin im Beratungsgespräch.</p></div></div></div></section>
<section class="bg-white" id="indikation"><div class="wrap"><div class="split">
<div><h2>Für wen kommt die Apherese in Frage?</h2>
<p>Die Apherese ist kein Allheilmittel. Wir setzen sie ein, wenn Voruntersuchung und Gespräch dafür sprechen. Dazu gehören zum Beispiel Fettstoffwechselstörungen, ausgewählte chronisch-entzündliche Verläufe und Belastungen durch Umweltstoffe. Für manche Anwendungen ist sie nicht zugelassen. Darüber sprechen wir offen.</p>
<p>Auch gesunde Menschen fragen nach der Apherese zur Vorsorge. Dafür gibt es bei UMI Longevity den {a('longevity/apherese-reset/', 'Apherese Reset')}.</p></div>
<div class="grid" style="gap:16px">
{a('medizin/apherese-programm/', '<span class="tag">UMI Medizin</span><h3>Apherese-Programm</h3><p>Mit Diagnostik, zwei Sitzungen, Eluat-Analyse und Hilfe beim Erstattungsantrag.</p><span class="more">Zum Programm →</span>', 'card')}
{a('longevity/apherese-reset/', '<span class="tag">UMI Longevity</span><h3>Apherese Reset</h3><p>Für Gesunde, mit Labor vorher und nachher und Auswertungsgespräch.</p><span class="more">Zum Reset →</span>', 'card')}
</div></div></div></section>
<section id="studien"><div class="wrap narrow"><h2>Was sagt die Forschung?</h2>
<p>Für die Lipoprotein-Apherese bei schweren Fettstoffwechselstörungen ist der Nutzen gut belegt. Für andere Anwendungen gibt es erste Studien und Erfahrungsberichte, aber noch keine abschließende Bewertung. Gern sprechen wir im Beratungsgespräch über den aktuellen Stand für Ihre Situation.</p>
<div class="note"><b>Für Angehörige:</b> Eine Begleitperson ist willkommen. Nach der Behandlung sollten Sie nicht selbst Auto fahren. Mehr unter {a('ihr-besuch/', 'Ihr Besuch bei uns')}.</div></div></section>
{team_mini(['kafle', 'gusic', 'gentsch'])}
{fh}{gutschein_hinweis()}"""
    return body, [fld, proc]


# ------------------------------------------------------------ Pakete

def apherese_programm():
    return paket(
        eyebrow="Paket · UMI Medizin", line="med",
        h1="Apherese-Programm",
        lead="Für Menschen mit anhaltenden Beschwerden, bei denen eine Apherese sinnvoll sein kann. Das Programm bündelt Vorgespräch, Diagnostik, zwei Sitzungen INUSpherese oder H.E.L.P.-Apherese, Eluat-Analyse und Nachgespräch in einem festen Ablauf.",
        preis_html=price("apherese_programm"),
        enthalten=["Beratungs- und Vorgespräch mit der Ärztin", "Diagnostik vor der Behandlung", "2 Sitzungen INUSpherese oder H.E.L.P.-Apherese",
                   "Eluat-Analyse der abgefilterten Bestandteile", "Begleitende Infusionen nach ärztlicher Empfehlung", "Nachgespräch mit Befunden",
                   "Hilfe beim Erstattungsantrag an PKV oder Beihilfe"],
        ablauf=[("Vorgespräch", " Telefon, Video oder in der Praxis. Wir prüfen, ob die Apherese für Sie passt."),
                ("Diagnostik", " Labor und Untersuchung, danach Kostenvoranschlag."),
                ("Zwei Sitzungen", " Je etwa zwei bis drei Stunden, im Abstand von zwei bis drei Tagen."),
                ("Nachgespräch", " Ergebnisse der Eluat-Analyse, Verlauf, nächste Schritte.")],
        passt=["Ihre Beschwerden bestehen seit Langem", "Sie haben eine gründliche Abklärung hinter sich oder wollen sie bei uns machen", "Sie möchten die Apherese in einem klaren Rahmen ausprobieren"],
        passt_nicht=["Sie haben eine akute, schwere Erkrankung", "Gegenanzeigen sprechen dagegen, das prüfen wir im Vorgespräch", "Sie suchen eine schnelle Lösung ohne Diagnostik"],
        kosten_extra=f'<p>Jede weitere Sitzung voraussichtlich {price("apherese_sitzung", "")}.</p>',
        team=["kafle", "gusic", "gentsch"],
        faqs=[("Kann ich nur eine Sitzung buchen?", "Ja, einzelne Sitzungen sind nach Kostenvoranschlag möglich. Das Programm ist für alle gedacht, die einen festen Rahmen mit Diagnostik möchten."),
              ("Muss ich für das Programm in Stuttgart übernachten?", "Nicht unbedingt. Wer weit anreist, bekommt Tipps für Unterkünfte in der Nähe."),
              ("Werden die Kosten erstattet?", "Je nach Tarif und Anlass erstatten PKV und Beihilfe einen Teil. Wir stellen die Unterlagen für Ihren Antrag zusammen.")],
        next_step=("Erst wissen, was die Apherese ist?", "inuspherese-zentrum-stuttgart/", "Mehr zur Apherese"))


def energie_check():
    return paket(
        eyebrow="Paket · UMI Medizin", line="med",
        h1="Energie-Check: wenn Sie immer müde sind",
        lead="Für alle, die sich seit Langem erschöpft fühlen, obwohl die Routinewerte normal sind. Der Energie-Check schaut auf Stressregulation, Zellenergie, Mikronährstoffe und Schilddrüse und endet mit einem Therapieplan.",
        preis_html=price("energie_check"),
        enthalten=["Erstgespräch im Schwerpunkt Erschöpfung und Energie", "Neurostress-Profil", "Zellenergie (Mitochondrien, oxidativer Stress)",
                   "Mikronährstoffe", "Schilddrüse", "Nervensystem-Messung (HRV)", "Befundgespräch mit Therapieplan"],
        ablauf=[("Erstgespräch", " Ausführliche Anamnese, etwa 45 Minuten."), ("Labor und HRV", " Blutabnahme und Messung, am selben Tag möglich."),
                ("Auswertung", " Die Ergebnisse liegen meist nach zwei bis drei Wochen vor."), ("Befundgespräch", " Ergebnisse verstehen, Plan festlegen.")],
        passt=["Sie sind seit Monaten erschöpft", "Ihre Werte beim Hausarzt sind unauffällig", "Sie wollen wissen, woran es liegt"],
        passt_nicht=["Sie haben akute Beschwerden, die rasch abgeklärt werden müssen", "Sie suchen nur eine einzelne Infusion"],
        team=["kafle", "buergler"],
        faqs=[("Ist der Energie-Check auch für gesunde Menschen?", "Er ist für Menschen mit Beschwerden gedacht. Wer ohne Beschwerden vorsorgen möchte, ist beim Longevity-Check richtig."),
              ("Was passiert nach dem Check?", "Je nach Ergebnis empfehlen wir zum Beispiel gezielte Mikronährstoffe, Infusionen, Stresstraining oder eine Regenerationskur.")],
        next_step=("Gesund, aber neugierig auf deine Werte?", "longevity/check/", "Zum Longevity-Check"))


KUREN = [
    ("Wärmekur", "Ganzkörperhyperthermie, 6 Sitzungen", "kur_hyperthermie",
     "Kontrollierte Erwärmung des ganzen Körpers bis etwa 40,5 °C mit wassergefilterter Infrarot-A-Strahlung, ärztlich überwacht. Je Sitzung etwa zwei Stunden mit Ruhephase."),
    ("Oxyvenierung", "nach Regelsberger, 12 Sitzungen", "kur_oxyvenierung",
     "Sauerstoff wird in kleinen Mengen langsam in die Vene gegeben. Ein über Jahrzehnte angewandtes naturheilkundliches Verfahren."),
    ("Farblaser", "intravasale Farblasertherapie, 12 Sitzungen", "kur_farblaser",
     "Licht verschiedener Wellenlängen wird über eine feine Kanüle in die Vene geleitet. Eine Sitzung dauert etwa 30 bis 60 Minuten."),
]


def kuren_html(du=False):
    return "".join(f'<div class="card"><span class="tag">{s}</span><h3>{n}</h3><p>{d}</p><span class="price">voraussichtlich {price(k, "")}</span></div>' for n, s, k, d in KUREN)


def regeneration_med():
    fh, fld = faq([
        ("Welche Kur passt zu mir?", "Das besprechen wir im Erstgespräch. Wichtig sind Ihre Beschwerden, Vorerkrankungen und wie viel Zeit Sie haben."),
        ("Kann ich Kuren kombinieren?", "Ja, zum Beispiel mit Infusionen. Wir stimmen den Ablauf mit Ihnen ab."),
        ("Wie oft komme ich?", "Die Wärmekur hat 6 Termine, Oxyvenierung und Farblaser je 12. Meist ein- bis zweimal pro Woche."),
    ])
    body = f"""{hero('Paket · UMI Medizin', 'Regenerationskuren', 'Drei Verfahren, jeweils als Kur mit festem Ablauf und voraussichtlichem Preis: Ganzkörperhyperthermie, Oxyvenierung und intravasaler Farblaser. Jede Kur beginnt mit einem ärztlichen Gespräch, in dem wir prüfen, ob sie zu Ihnen passt.',
    book('Erstgespräch buchen') + tel('btn ghost', 'Anrufen'), 'med')}
<section class="bg-white"><div class="wrap"><div class="grid g3">{kuren_html()}</div>
<p style="margin-top:20px">{a('ganzkoerperhyperthermie/', 'Alles zur Ganzkörperhyperthermie')}</p></div></section>
<section><div class="wrap"><div class="split"><div><h2>So läuft eine Kur ab</h2>{schritte([
    ('Erstgespräch', ' Wir klären, ob und welche Kur passt, und schließen Gegenanzeigen aus.'),
    ('Kostenvoranschlag', ' Sie bekommen den voraussichtlichen Preis schriftlich.'),
    ('Termine', ' Feste Termine über einige Wochen, bequem online oder am Empfang vereinbart.'),
    ('Abschluss', ' Gespräch zum Verlauf und zu weiteren Schritten.')])}</div>
{kosten_box()}</div></div></section>
{team_mini(['kafle', 'buergler'])}{fh}{gutschein_hinweis()}"""
    return body, [fld]


def hyperthermie():
    fh, fld = faq([
        ("Wie fühlt sich eine Ganzkörperhyperthermie an?", "Wie ein künstliches Fieber: Es wird warm, Sie schwitzen. Viele empfinden die Ruhephase danach als angenehm entspannend."),
        ("Wie lange dauert eine Sitzung?", "Insgesamt etwa zwei Stunden mit Vorbereitung, Erwärmung, Plateau- und Ruhephase."),
        ("Was soll ich vorher beachten?", "Ausreichend trinken, leicht essen, Metallschmuck zu Hause lassen. Bequeme Kleidung zum Wechseln mitbringen."),
        ("Wie wird überwacht?", "Temperatur, Puls und Sauerstoffsättigung werden während der ganzen Behandlung gemessen."),
        ("Wie viele Sitzungen sind sinnvoll?", "Das hängt vom Anlass ab. Häufig ist eine Kur mit 6 Sitzungen."),
        ("Kann ich danach Auto fahren?", "Wir empfehlen, sich abholen zu lassen oder öffentliche Verkehrsmittel zu nutzen."),
        ("Was kostet eine Ganzkörperhyperthermie?", f"Die Wärmekur mit 6 Sitzungen kostet voraussichtlich {price('kur_hyperthermie', '')}. Einzelne Sitzungen nach Kostenvoranschlag."),
    ])
    proc = {"@context": "https://schema.org", "@type": "MedicalTherapy", "name": "Ganzkörperhyperthermie",
            "alternateName": ["Fieberbett", "Fiebertherapie"], "description": "Moderate Ganzkörperhyperthermie bis etwa 40,5 °C mit wIRA bei UMI Stuttgart."}
    body = f"""{hero('Regeneration · UMI Medizin', 'Ganzkörperhyperthermie in Stuttgart',
    'Bei der Ganzkörperhyperthermie wird der Körper kontrolliert erwärmt, ähnlich wie bei Fieber. Wir arbeiten mit dem IRATHERM 1000M und wassergefilterter Infrarot-A-Strahlung (wIRA), moderat bis etwa 40,5 °C und ärztlich überwacht. Viele kennen das Verfahren auch als „Fieberbett“ oder „Fiebertherapie“.',
    book('Erstgespräch buchen') + a('medizin/regenerationskuren/', 'Zur Wärmekur', 'btn ghost'), 'med',
    f'<p class="price-line"><b>Wärmekur mit 6 Sitzungen voraussichtlich {price("kur_hyperthermie", "")}</b> · nach GOÄ</p>')}
<section class="bg-white"><div class="wrap"><div class="split">
<div><h2>Wie läuft eine Sitzung ab?</h2>{schritte([
    ('Vorgespräch und Aufklärung', ' Ärztliche Untersuchung, Gegenanzeigen ausschließen.'),
    ('Vorbereitung', ' In einem eigenen Raum, Metallschmuck ablegen.'),
    ('Erwärmung', ' Langsamer Anstieg der Körpertemperatur unter Überwachung von Temperatur, Puls und Sauerstoff.'),
    ('Plateauphase', ' Die Zieltemperatur wird für eine festgelegte Zeit gehalten.'),
    ('Ruhephase', ' 15 bis 30 Minuten nachruhen, auf Wunsch lauwarm duschen.')])}</div>
<div><h2>Milde und moderate Hyperthermie</h2>
<p>Bei der milden Form steigt die Körpertemperatur auf etwa 38,5 °C, bei der moderaten auf bis zu 40,5 °C. Welche Form für Sie passt, legt die Ärztin fest.</p>
<h3 style="margin-top:28px">Wann wir keine Hyperthermie machen</h3>
{liste(['höhergradige Herzschwäche', 'schwere arterielle Durchblutungsstörungen', 'schwere Organschwäche', 'akute schwere Entzündungen',
        'nicht eingestellter Bluthochdruck', 'nicht eingestellte Schilddrüsenüberfunktion', 'Schwangerschaft', 'Epilepsie und andere Anfallsleiden'])}
<p class="small muted">Nach einer Krebserkrankung nur nach abgeschlossener Erstbehandlung und in Absprache mit den behandelnden Ärzten.</p></div>
</div></div></section>
<section><div class="wrap"><div class="grid g2">{kosten_box()}
{a('longevity/regenerationskuren/', '<span class="tag">Auch bei UMI Longevity</span><h3>Wärmekur zur Erholung</h3><p>Für Gesunde, die sich bewusst Zeit für Regeneration nehmen.</p><span class="more">Zu Longevity →</span>', 'card')}</div></div></section>
{team_mini(['kafle', 'gusic'])}{fh}{gutschein_hinweis()}"""
    return body, [fld, proc]


def diagnostik():
    blocks = [
        ("Basisdiagnostik", [("Immunstatus", "Immunglobuline, IL-6, optional Lymphozytenprofil und NK-Zellen"),
                             ("Entzündungsstatus", "hsCRP, IL-6, optional TNF-α und weitere Marker"),
                             ("Belastungsscreening", "oxidativer Stress, Glutathion, Q10, optional Schwermetalle"),
                             ("Organscreening", "Leber, Niere, Schilddrüse")]),
        ("Erweiterte Diagnostik", [("Darm-Analyse", "Mikrobiom, Entzündung, Barrierefunktion"),
                                   ("Mikronährstoffe", "Vitamine, Mineralstoffe, Spurenelemente, Aminosäuren"),
                                   ("Zellenergie", "oxidativer Stress und Mitochondrienfunktion"),
                                   ("Schwermetalle und Umweltstoffe", "z. B. Blei, Cadmium, Quecksilber, ausgewählte PFAS"),
                                   ("Hormon- und Neurostress-Profil", "Hormonachsen und Stressbotenstoffe"),
                                   ("Nervensystem-Messung (HRV)", "Herzratenvariabilität, vegetatives Nervensystem"),
                                   ("Omega-3-Index", "Verhältnis der Fettsäuren im Blut")]),
        ("Untersuchungen in der Praxis", [("Körperliche Untersuchung", "mit ausführlicher Anamnese"), ("Ruhe-EKG", ""),
                                          ("Ultraschall", "Bauchorgane und Nieren"), ("Lungenfunktion und Sauerstoffsättigung", ""),
                                          ("Eluat-Analyse", "nach der Apherese")]),
    ]
    html = ""
    for i, (h, items) in enumerate(blocks):
        anchor = ["basisdiagnostik", "erweitertediagnosik", "untersuchungen"][i]
        cards = "".join(f'<div class="card"><h3>{n}</h3><p class="small">{d}</p></div>' for n, d in items)
        html += f'<section class="{"bg-white" if i % 2 == 0 else ""}" id="{anchor}"><div class="wrap"><h2>{h}</h2><div class="grid g3" style="margin-top:20px">{cards}</div></div></section>'
    fh, fld = faq([
        ("Kann ich einzelne Laborwerte bestellen?", "In der Medizin stellen wir die Diagnostik nach dem Gespräch zusammen, damit nur gemacht wird, was weiterhilft. Feste Pakete sind der Energie-Check und bei UMI Longevity der Longevity-Check."),
        ("Wer rechnet das Labor ab?", "Häufig rechnet das Fachlabor direkt mit Ihnen ab. Das steht vorab in Ihrem Kostenvoranschlag."),
    ])
    body = f"""{hero('Diagnostik · UMI Medizin', 'Labordiagnostik in Stuttgart: genau hinschauen',
    'Mehr als der Routine-Check: Viele Ursachen bleiben bei einer üblichen Untersuchung unentdeckt. Nach dem Erstgespräch wählt unsere Ärztin die Bausteine aus, die in Ihrem Fall weiterhelfen.',
    book('Erstgespräch buchen') + a('energie-check/', 'Energie-Check', 'btn ghost'), 'med')}
{html}{fh}"""
    return body, [fld]


PAGES = [
    Page("medizin", "Umweltmedizin und ganzheitliche Medizin Stuttgart · UMI Medizin",
         "UMI Medizin in Stuttgart-Vaihingen: Ursachen finden bei anhaltenden Beschwerden. Schwerpunkte, Apherese, Diagnostik, Hyperthermie. Erstgespräch online buchen.",
         medizin, line="med", nav="med", crumbs=[(None, "UMI Medizin")]),
    Page("ganzheitliche-sprechstunde", "Ganzheitliche Medizin Stuttgart · UMI Medizin",
         "Ganzheitliche Medizin in Stuttgart-Vaihingen: ausführliches Erstgespräch, Schulmedizin und Naturheilkunde verbunden. Privatpraxis UMI Stuttgart.",
         ganzheitlich, line="med", nav="med", crumbs=MED + [(None, "Ganzheitliche Medizin")]),
    Page("internistische-sprechstunde", "Innere Medizin Stuttgart-Vaihingen · UMI Medizin",
         "Internistische Abklärung und Vorsorge in Stuttgart-Vaihingen mit Labor, EKG und Ultraschall. Privatpraxis UMI Stuttgart, Termin online.",
         internistisch, line="med", nav="med", crumbs=MED + [(None, "Innere Medizin")]),
    Page("sub-health-syndrom", "Ständig müde? Erschöpfung abklären in Stuttgart · UMI",
         "Erschöpfung und Energie: Ursachen finden, wenn Sie ständig müde sind und die Werte normal. Erstgespräch oder Energie-Check bei UMI Stuttgart.",
         subhealth, line="med", nav="med", crumbs=MED + [(None, "Erschöpfung und Energie")]),
    Page("long-covid-sprechstunde", "Beschwerden nach Infektionen · UMI Medizin Stuttgart",
         "Anhaltende Beschwerden nach Infektion oder Impfung: gründliche Abklärung und Begleitung in Stuttgart-Vaihingen. Vorgespräch auch per Video.",
         infektionen, line="med", nav="med", crumbs=MED + [(None, "Beschwerden nach Infektionen")]),
    Page("inuspherese-zentrum-stuttgart", "INUSpherese & H.E.L.P.-Apherese in Stuttgart · UMI",
         "Blutwäsche (Apherese) in Stuttgart-Vaihingen: INUSpherese und H.E.L.P., Ablauf, Kosten nach GOÄ, Eluat-Analyse. Beratungsgespräch online buchen.",
         apherese, nav="aph", crumbs=[(None, "Apherese")]),
    Page("medizin/apherese-programm", "Apherese-Programm Stuttgart · UMI Medizin",
         "Apherese-Programm bei UMI Stuttgart: Vorgespräch, Diagnostik, zwei Sitzungen INUSpherese oder H.E.L.P., Eluat-Analyse. Voraussichtliche Kosten nach GOÄ.",
         apherese_programm, line="med", nav="med", crumbs=MED + [(None, "Apherese-Programm")]),
    Page("energie-check", "Energie-Check: immer müde? · UMI Stuttgart",
         "Energie-Check bei UMI Stuttgart: Erschöpfung abklären mit Neurostress, Zellenergie, Mikronährstoffen, HRV und Therapieplan. Termin online buchen.",
         energie_check, line="med", nav="med", crumbs=MED + [(None, "Energie-Check")]),
    Page("medizin/regenerationskuren", "Regenerationskuren: Hyperthermie, Oxyvenierung, Farblaser · UMI",
         "Regenerationskuren in Stuttgart: Ganzkörperhyperthermie, Oxyvenierung und Farblaser als Kur mit festem Ablauf und voraussichtlichem Preis.",
         regeneration_med, line="med", nav="med", crumbs=MED + [(None, "Regenerationskuren")]),
    Page("ganzkoerperhyperthermie", "Ganzkörperhyperthermie Stuttgart (Fieberbett) · UMI",
         "Ganzkörperhyperthermie in Stuttgart-Vaihingen: moderat bis 40,5 °C mit wIRA, ärztlich überwacht. Ablauf, Gegenanzeigen, Kosten der Wärmekur.",
         hyperthermie, line="med", nav="med", crumbs=MED + [(None, "Ganzkörperhyperthermie")]),
    Page("labordiagnostik", "Labordiagnostik Stuttgart privat · UMI Medizin",
         "Labordiagnostik bei UMI Stuttgart: Immunstatus, Entzündung, Zellenergie, Mikronährstoffe, Schwermetalle, HRV. Ärztlich ausgewählt nach dem Erstgespräch.",
         diagnostik, line="med", nav="med", crumbs=MED + [(None, "Diagnostik")]),
]
