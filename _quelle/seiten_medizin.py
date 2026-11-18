"""Linie UMI Medizin (Ansprache: Sie) und die gemeinsame Apherese-Seite."""
from rahmen import Page, a, book, tel, faq, price
from bausteine import hero, liste, schritte, paket, team_mini, gutschein_hinweis, kosten_box, a_img
from seiten_dach import schema_svg
import config as C

MED = [("medizin/", "UMI Medizin")]


# ------------------------------------------------------------ Einstieg

SCHWERPUNKTE = [
    ("ganzheitliche-sprechstunde/", "Ganzheitliche Medizin", "Für alle, die nicht wissen, wo sie hinsollen. Wir nehmen Ihre ganze Geschichte auf und suchen nach Zusammenhängen."),
    ("internistische-sprechstunde/", "Innere Medizin", "Abklärung mit Labor, EKG und Ultraschall. Auch als Vorsorge-Untersuchung."),
    ("sub-health-syndrom/", "Erschöpfung und Energie", "Immer müde, aber die Werte sind normal? Wir schauen genauer hin, bis zum Energie-Check."),
    ("long-covid-sprechstunde/", "Beschwerden nach Infektionen", "Wenn Beschwerden nach einer Infektion oder Impfung bleiben. Gründliche Abklärung und Begleitung."),
    ("darmgesundheit/", "Darm und Verdauung", "Blähungen, Unverträglichkeiten, ein Bauch, der nicht zur Ruhe kommt? Mit Mikrobiom-Analyse und Plan."),
    ("internistische-sprechstunde/#check-up", "Gesundheits-Check-up", "Gründliche Rundum-Untersuchung mit Labor, Ultraschall, EKG, Lungenfunktion und HRV-Messung."),
]


def medizin():
    sp = "".join(a(t, f'<span class="tag">Schwerpunkt</span><h3>{n}</h3><p>{d}</p><span class="more">Mehr erfahren →</span>', "card") for t, n, d in SCHWERPUNKTE)
    hp = liste(["Schmerz", "Stress und Entspannung", "Frauengesundheit", "Kindergesundheit", "Naturheilkunde und ganzheitliche Begleitung",
                "Begleitung bei anhaltender Erschöpfung"])
    th = "".join((a(t, f'<span class="tag">{tag}</span><h3>{n}</h3><p>{d}</p><span class="more">Mehr erfahren →</span>', "card") if t else
                  f'<div class="card"><span class="tag">{tag}</span><h3>{n}</h3><p>{d}</p></div>') for t, tag, n, d in [
        ("inuspherese-zentrum-stuttgart/", "Apherese", "INUSpherese®", "Blutplasma außerhalb des Körpers filtern, mit Eluat-Analyse."),
        ("medizin/help-apherese/", "Apherese", "H.E.L.P.-Apherese", "Off-Label-Anwendung, nur nach ärztlicher Prüfung."),
        ("ganzkoerperhyperthermie/", "Wärme", "Ganzkörperhyperthermie", "Kontrollierte Erwärmung des Körpers, ärztlich überwacht."),
        (None, "Infusionen", "Infusionstherapie", "Nach ärztlicher Verordnung, abgestimmt auf Ihre Befunde."),
        ("medizin/regenerationskuren/", "Kur", "Oxyvenierung nach Regelsberger", "Kleine Mengen Sauerstoff über die Vene, als Kur."),
        ("medizin/regenerationskuren/", "Kur", "Intravasale Farblasertherapie", "Licht über eine feine Faser in der Vene, als Kur."),
        (None, "Naturheilkunde", "Akupunktur", "Traditionelle Nadeltherapie, auch begleitend."),
        (None, "Naturheilkunde", "Neuraltherapie", "Gezielte Injektionen mit einem örtlichen Betäubungsmittel."),
        ("labordiagnostik/", "Diagnostik", "Labordiagnostik", "Immunstatus, Entzündung, Mikrobiom, Mikronährstoffe, Umweltstoffe und mehr."),
    ])
    pk = "".join(a(t, f'<span class="tag">Paket</span><h3>{n}</h3><p>{d}</p><span class="price">{p}</span><span class="more">Zum Paket →</span>', "card") for t, n, d, p in [
        ("medizin/apherese-programm/", "Apherese-Programm", "Vorgespräch, Diagnostik, zwei Sitzungen INUSpherese, Eluat-Analyse und Nachgespräch.", price("apherese_programm")),
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
<section class="bg-white" id="therapien"><div class="wrap">
<span class="eyebrow">Therapien</span><h2>Was wir in der Praxis anbieten</h2>
<p class="lead">Welche Therapie für Sie infrage kommt, entscheiden wir gemeinsam nach dem Erstgespräch und der Diagnostik.</p>
<div class="grid g3" style="margin-top:28px">{th}</div>
<div class="split" style="margin-top:48px">
<div><h2>Begleitend</h2>{liste(["Darmaufbau und Mikrobiom-Management", "Orthomolekulare und funktionelle Nährstofftherapie", "Hormontherapie", "Stress- und Schlafmanagement", "Ernährung, Lebensstil und Stressregulation", "Gesundheitsberatung mit Evelyn Gentsch"])}</div>
<div class="box" id="heilpraktikerin"><h3>Bei unserer Heilpraktikerin</h3><p>Aurelia Bürgler begleitet Sie naturheilkundlich, auch ergänzend zur ärztlichen Behandlung. Buchbar als Erstgespräch:</p>{hp}</div>
</div>
<div class="split" style="margin-top:32px">
<div class="box"><h3>Umweltmedizin</h3><p>Das „U“ in UMI: Wir fragen nach Wohnung, Beruf und Alltag und messen, wo es sinnvoll ist, Umweltstoffe wie Schwermetalle, Pestizide oder ausgewählte PFAS.</p><p style="margin:0">{a('labordiagnostik/#umwelt', 'Zur Umweltdiagnostik')}</p></div>
<div class="box"><h3>Für Angehörige</h3><p>Sie suchen Hilfe für Ihre Mutter, Ihren Vater oder Ihren Partner? Im <b>Angehörigengespräch</b> klären wir Ihre Fragen, auch zu Belastung, Ablauf und Anreise. Termine können Sie auch für eine andere Person buchen.</p>{tel('btn small ghost', 'Anrufen')}</div>
</div></div></section>
<section><div class="wrap"><div class="hint"><p><b>Noch unsicher?</b> Im Vorgespräch am Telefon oder per Video klären wir, ob wir Ihnen weiterhelfen können.</p>{book('Vorgespräch buchen', 'btn small')}</div></div></section>"""


# ------------------------------------------------------------ Schwerpunkte

def schwerpunkt(eyebrow, h1, lead, wer, ablauf, faqs, weiter, extra=""):
    fh, fld = faq(faqs)
    body = f"""{hero(eyebrow, h1, lead, book('Erstgespräch buchen') + tel('btn ghost', 'Anrufen'), 'med')}
<section class="bg-white"><div class="wrap"><div class="split">
<div><h2>Für wen dieser Schwerpunkt da ist</h2>{liste(wer)}</div>
<div><h2>So gehen wir vor</h2>{schritte(ablauf)}</div></div></div></section>
{extra}
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
        a("energie-check/", '<span class="tag">Passend dazu</span><h3>Energie-Check</h3><p>Bei anhaltender Erschöpfung ohne klaren Befund.</p><span class="more">Zum Energie-Check →</span>', "card"),
        extra=f"""<section id="check-up"><div class="wrap"><div class="split wide">
<div><span class="eyebrow">Ganzheitlicher Gesundheits-Check-up</span><h2>Einmal gründlich durchchecken</h2>
<p>Für alle, die es genau wissen wollen: Beim Gesundheits-Check-up verbinden wir die internistische Untersuchung mit einer breiten Labor- und Funktionsdiagnostik. Was genau dazugehört, stimmen wir im Erstgespräch auf Sie ab.</p>
{liste(["Ganzkörperuntersuchung und ausführliche Anamnese", "Labordiagnostik", "Ultraschall der Bauchorgane und Nieren", "Ruhe-EKG", "Sauerstoffsättigung und Lungenfunktion", "Nahrungsmittelunverträglichkeiten", "HRV-Messung (Stress und vegetatives Nervensystem)", "Urin, Stuhl und weitere Untersuchungen nach Bedarf"])}</div>
<div class="box" style="align-self:center"><h3>Voraussichtliche Kosten</h3><p>Nach GOÄ, je nach Umfang. Sie bekommen vorher einen schriftlichen Kostenvoranschlag.</p>{book('Check-up anfragen')}<p class="small muted" style="margin:14px 0 0">Gesund und neugierig auf Ihre Werte? Dann passt auch der {a('longevity/check/', 'Longevity-Check')}.</p></div>
</div></div></section>""")


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


def darm():
    return schwerpunkt("Schwerpunkt · UMI Medizin", "Darm und Verdauung: Mikrobiom verstehen",
        "Blähungen, wechselnder Stuhlgang, ein Bauch, der nicht zur Ruhe kommt, oder Lebensmittel, die Sie plötzlich nicht mehr vertragen: Der Darm meldet sich oft leise, aber hartnäckig. Wir klären gründlich ab, sehen uns Ihr Mikrobiom an und machen daraus einen Plan.",
        ["Sie haben seit Längerem Verdauungsbeschwerden ohne klare Erklärung", "Sie vermuten, dass Sie bestimmte Lebensmittel nicht vertragen",
         "Sie möchten wissen, wie es um Ihre Darmflora steht", "Sie haben schon einiges ausprobiert und suchen einen Plan, der zu Ihren Werten passt"],
        [("Erstgespräch", " Beschwerden, Ernährung, Medikamente, Vorbefunde, körperliche Untersuchung."),
         ("Diagnostik", " Mikrobiom-Analyse aus dem Stuhl, Tests auf Nahrungsmittelunverträglichkeiten, Labor nach Bedarf, Ultraschall des Bauches."),
         ("Befundgespräch", " Wir erklären die Ergebnisse verständlich und schlagen einen Plan mit Kostenvoranschlag vor."),
         ("Begleitung", " Darmaufbau und Mikrobiom-Management, Ernährung und Nährstoffe, mit Kontrolle nach einigen Monaten.")],
        [("Was zeigt eine Mikrobiom-Analyse?", "Welche Bakterien in Ihrem Darm leben und in welchem Verhältnis, dazu Hinweise auf Entzündung und die Barrierefunktion der Darmschleimhaut. Was das für Sie bedeutet, besprechen wir im Befundgespräch."),
         ("Muss ich dafür zur Darmspiegelung?", "Nein. Die Mikrobiom-Analyse wird aus einer Stuhlprobe gemacht, die Sie zu Hause nehmen. Ob zusätzlich eine Darmspiegelung sinnvoll ist, klären wir mit Ihnen und Ihrer Hausärztin oder Ihrem Hausarzt."),
         ("Verkaufen Sie Präparate?", "Nein. Wenn Präparate sinnvoll sind, sagen wir Ihnen, welche und in welcher Dosis. Kaufen können Sie sie, wo Sie möchten.")],
        a("labordiagnostik/#erweitertediagnostik", '<span class="tag">Diagnostik</span><h3>Mikrobiom und mehr</h3><p>Alle Laborbausteine im Überblick.</p><span class="more">Zur Diagnostik →</span>', "card"),
        extra=f"""<section id="begleitung"><div class="wrap"><div class="grid g3">
<div class="card"><span class="tag">Messen</span><h3>Mikrobiom-Analyse</h3><p>Darmflora, Gleichgewicht der Bakterien, Entzündung und Barrierefunktion, aus einer Stuhlprobe.</p></div>
<div class="card"><span class="tag">Klären</span><h3>Unverträglichkeiten</h3><p>Gezielte Tests auf Nahrungsmittelunverträglichkeiten, dazu bei Bedarf Histamin und Mastzellen.</p></div>
<div class="card"><span class="tag">Begleiten</span><h3>Darmaufbau</h3><p>Mikrobiom-Management, Ernährung und funktionelle Nährstofftherapie, abgestimmt auf Ihre Befunde.</p></div>
</div></div></section>""")


# ------------------------------------------------------------ Apherese (Dach)

STOFFE = [
    # (Name, Unterzeile, Woher, Was man weiß, Was gemessen wurde)
    ("Blutfette", "LDL-Cholesterin, Lipoprotein(a)",
     "Teils aus der Ernährung. Lipoprotein(a) ist vor allem erblich bedingt.",
     "Erhöhte Werte gelten als anerkannter Risikofaktor für Gefäßverengungen und Herz-Kreislauf-Erkrankungen.",
     "LDL-Cholesterin, Triglyceride und Lipoprotein(a) waren nach der Behandlung deutlich niedriger."),
    ("Fibrinogen", "Gerinnungseiweiß",
     "Ein körpereigenes Eiweiß, wichtig für die Blutgerinnung.",
     "Hohe Werte machen das Blut zähflüssiger und werden mit Durchblutungsstörungen und einem höheren Herz-Kreislauf-Risiko in Verbindung gebracht.",
     "Fibrinogen war nach der Behandlung deutlich niedriger."),
    ("Entzündungs­botenstoffe", "z. B. Interleukine, CRP",
     "Der Körper bildet sie selbst, wenn das Immunsystem aktiv ist.",
     "Bleiben sie dauerhaft leicht erhöht, spricht die Forschung von einer stillen Entzündung. Sie wird mit anhaltender Erschöpfung, Gelenk- und Muskelbeschwerden in Verbindung gebracht.",
     "Interleukin-6 und CRP waren nach der Behandlung deutlich niedriger."),
    ("Autoantikörper", "fehlgeleitete Antikörper",
     "Das Immunsystem bildet Antikörper, die sich gegen körpereigene Strukturen richten.",
     "Autoantikörper spielen bei Autoimmunerkrankungen eine Rolle. Einige werden mit Beschwerden des Nervensystems, des Kreislaufs und mit Erschöpfung in Verbindung gebracht.",
     "Bestimmte Autoantikörper waren nach der Behandlung niedriger."),
    ("Umweltstoffe", "PFAS, Mikroplastik, Schwermetalle",
     "Aus Verpackungen, beschichteten Pfannen, Kleidung, Wasser, Luft und Nahrung. Viele baut der Körper nur sehr langsam ab.",
     "Jeder Mensch trägt heute Spuren davon im Blut. Welche in welcher Menge eine Rolle für die Gesundheit spielen, wird intensiv erforscht.",
     "PFAS im Plasma waren in ersten kleinen Studien niedriger. Im Filtrat fanden sich Hinweise auf Mikroplastik."),
]

FRAGEN = [
    "Ihre Blutfette oder Ihr Lipoprotein(a) sind erhöht, obwohl Sie auf Ernährung und Bewegung achten?",
    "Ihre Entzündungswerte sind immer wieder leicht erhöht, ohne dass ein klarer Grund gefunden wurde?",
    "Sie fühlen sich seit Langem erschöpft, und die üblichen Untersuchungen haben keine Erklärung gebracht?",
    "Sie leben mit einer Autoimmunerkrankung und suchen eine Ergänzung zu Ihrer bisherigen Behandlung?",
    "Sie waren beruflich oder privat Umweltstoffen ausgesetzt, zum Beispiel Lösungsmitteln, Metallen oder PFAS?",
    "Sie reagieren auf Duftstoffe, Chemikalien oder Ausdünstungen empfindlicher als andere?",
    "Sie haben anhaltende Gelenk- oder Muskelbeschwerden, die mit Entzündungen zusammenhängen könnten?",
    "Sie haben Missempfindungen wie Kribbeln oder Taubheit in Händen und Füßen, bei denen Antikörper oder Umweltstoffe eine Rolle spielen könnten?",
]

VERFAHREN = [
    ("INUSpherese®", "Doppelfiltration des Plasmas, hält große Eiweiße, Fette und daran Gebundenes zurück", "ja"),
    ("H.E.L.P.-Apherese", "fällt LDL-Cholesterin, Lipoprotein(a) und Fibrinogen mit Heparin aus dem Plasma", "Off-Label-Anwendung, nur nach ärztlicher Prüfung · {HELP_LINK}"),
    ("Lipidapherese", "Sammelbegriff für Verfahren, die vor allem Blutfette senken", "nein"),
    ("Immunadsorption", "bindet gezielt Antikörper an eine Säule", "nein"),
    ("Plasmaaustausch", "Plasma wird verworfen und durch eine Lösung ersetzt", "nein"),
    ("Dialyse", "ersetzt die Nierenfunktion, filtert kleine, harnpflichtige Stoffe", "nein"),
]


def apherese():
    fh, fld = faq([
        ("Ist das eine Dialyse?", "Nein. Die Dialyse ersetzt die Nierenfunktion und filtert kleine Stoffe. Die INUSpherese® filtert gezielt große Moleküle aus dem Plasma."),
        ("Bekomme ich fremdes Plasma?", "Nein. Ihr eigenes Plasma wird gefiltert und zurückgeführt, eine Ersatzlösung ist nicht nötig."),
        ("Tut das weh und ist es gut verträglich?", "Spürbar ist vor allem der Einstich in der Armbeuge, die Behandlung selbst ist schmerzarm. Wie bei jeder Behandlung am Blutkreislauf kann es zu Nebenwirkungen wie Kreislaufschwäche oder Blutergüssen kommen. Darüber klären wir Sie vorher ausführlich auf."),
        ("Wie viele Behandlungen brauche ich?", "Das hängt von Ihren Werten und Zielen ab. Meist beginnen wir mit zwei Behandlungen innerhalb von fünf Tagen, mit mindestens einem Tag Pause dazwischen."),
        ("Was kostet die INUSpherese®?", f"Eine Behandlung voraussichtlich {price('apherese_sitzung', 'ab')}, zwei Behandlungen inklusive Vorgesprächen, Untersuchungen, Überwachung und begleitenden Infusionen voraussichtlich {price('apherese_programm')}. Was Sie nicht benötigen, wird nicht berechnet. Sie bekommen vorher einen schriftlichen Kostenvoranschlag."),
        ("Zahlt das meine Krankenkasse?", "In der Regel nicht, die INUSpherese® ist bei uns eine Selbstzahlerleistung. Private Versicherungen erstatten in Einzelfällen. Wir beraten Sie dazu."),
    ])
    proc = {"@context": "https://schema.org", "@type": "MedicalTherapy", "name": "INUSpherese",
            "alternateName": ["Doppelfiltrations-Plasmapherese", "Apherese"],
            "description": "Ambulante Filtration des eigenen Blutplasmas mit Doppelmembranfiltern bei UMI Stuttgart, mit Eluat-Analyse."}

    t1 = "".join(f"""<div class="stoff"><span class="nr">{i}</span><h3>{n}</h3><p class="sub">{s}</p>
<p><b>Woher:</b> {w}</p><p><b>Was man weiß:</b> {k}</p></div>""" for i, (n, s, w, k, m) in enumerate(STOFFE, 1))
    t2 = "".join(f"""<div class="stoff filter"><span class="nr">{i}</span><h3>{n}</h3><p class="sub">{s}</p><p>{m}</p></div>""" for i, (n, s, w, k, m) in enumerate(STOFFE, 1))
    fr = "".join(f'<li>{q}</li>' for q in FRAGEN)
    vt = "".join(f'<tr><td><b>{n}</b></td><td style="white-space:normal;font-weight:400">{k}</td><td style="white-space:normal">{u.replace('{HELP_LINK}', a('medizin/help-apherese/', 'Mehr zur H.E.L.P.-Apherese'))}</td></tr>' for n, k, u in VERFAHREN)
    anmeldung = f"mailto:{C.MAIL}?subject=Anmeldung%20Info-Abend%20INUSpherese%209.12."

    body = f"""{hero('Apherese in Stuttgart · INUSpherese-Zentrum', 'INUSpherese®-Zentrum Stuttgart<span class="h1-sub">Blutplasma filtern, Belastungsstoffe reduzieren</span>',
    'Bei der INUSpherese® wird Ihr Blutplasma außerhalb des Körpers durch einen feinen Spezialfilter geleitet und wieder zurückgeführt. Der Filter hält große Eiweiße, Fette und daran gebundene Stoffe zurück. Was im Filter bleibt, lässt sich im Labor untersuchen.',
    book('Erstgespräch vereinbaren') + a('#info-abend', 'Info-Abend am 9. Dezember', 'btn ghost'), 'dach',
    '<ul class="pills"><li>Ihr eigenes Plasma, ohne Ersatzlösung</li><li>Ambulant, etwa 2 bis 3 Stunden</li><li>Wichtige Eiweiße und Elektrolyte bleiben erhalten</li></ul>')}

<section class="tight bg-dark"><div class="wrap"><p class="claim">Seit 2023 zertifizierter INUS-Partner. Einziges INUSpherese-Zentrum im Raum Stuttgart, in enger Zusammenarbeit mit dem INUS Medical Center in Cham, wo das Verfahren entwickelt wurde.</p></div></section>

<section class="bg-white" id="im-blut"><div class="wrap">
<span class="eyebrow">Teil 1</span><h2>Was sich im Blut ansammeln kann</h2>
<p class="lead">Unser Blut transportiert nicht nur Nährstoffe und Sauerstoff. Mit der Zeit können sich darin auch Stoffe anreichern, die wir über Nahrung, Wasser, Luft und Alltagsprodukte aufnehmen oder die der Körper selbst bildet. Ein Überblick:</p>
<div class="stoffe">{t1}</div>
<p class="small muted" style="margin-top:20px">Ob und wie stark solche Stoffe bei Ihnen eine Rolle spielen, lässt sich nur im Einzelfall beurteilen. Ein Teil davon lässt sich im Blut messen.</p>
</div></section>

<section id="filter"><div class="wrap">
<span class="eyebrow">Teil 2</span><h2>Was die INUSpherese® aus dem Plasma filtert</h2>
<div class="split"><div><p>Viele Stoffe im Blut schwimmen nicht frei, sondern sind an große Eiweiße und Fette gebunden. Genau hier setzt der Filter an. Er lässt kleine Bestandteile wie Wasser, Salze und die meisten Nährstoffe durch und hält größere Moleküle zurück, und mit ihnen vieles, was daran gebunden ist.</p>
<p>Anders als beim Plasmaaustausch verlieren Sie dabei keine nennenswerten Mengen an Elektrolyten oder lebenswichtigen Eiweißen.</p></div>
<div class="svg-schema">{schema_svg()}</div></div>
<h3 style="margin-top:36px">In Studien gemessen</h3>
<div class="stoffe">{t2}</div>
<div class="box" style="margin-top:20px"><h3>Was der Filter außerdem zurückhalten kann</h3>
<p>Der Filter kann auch weitere Stoffe zurückhalten, wenn sie an große Eiweiße oder Fette gebunden sind:</p>
{liste(['Chemikalien wie Pestizide und organische Lösemittel', 'Schwermetalle', 'Immunkomplexe, Allergene und Stoffwechselprodukte'])}
<p class="small muted" style="margin:0">Dazu gibt es bisher nur Herstellerangaben und einzelne Fallberichte, noch keine größeren Studien. Ob und welche dieser Stoffe in Ihrem Fall im Filter bleiben, kann die Eluat-Analyse zeigen.</p></div>
<div class="note" style="margin-top:24px"><b>Zur Studienlage:</b> Studien zeigen, dass diese Werte direkt nach der Behandlung deutlich niedriger sind. Ob und wie sich das auf einzelne Beschwerden auswirkt, ist in großen kontrollierten Studien noch nicht untersucht.</div>
</div></section>

<section class="bg-dark" id="eluat"><div class="wrap"><div class="split">
<div><span class="eyebrow" style="color:var(--euca)">Eluat-Analyse</span><h2 style="color:var(--shell)">Ihre Werte vorher. Ihre Werte nachher. Und was dazwischen im Filter geblieben ist.</h2></div>
<div><p>Was der Filter zurückhält, kann ein Labor untersuchen. So sehen Sie schwarz auf weiß, was aus Ihrem Plasma gefiltert wurde. Die Ergebnisse dokumentieren wir, damit wir den Verlauf vergleichen und weitere Behandlungen gezielt planen können.</p></div>
</div></div></section>

<section class="bg-white" id="fuer-wen"><div class="wrap"><div class="split wide">
<div><span class="eyebrow">Teil 3</span><h2>Erkennen Sie sich wieder?</h2>
<p>Die INUSpherese® ist keine Behandlung für jeden und ersetzt keine notwendige Therapie. Sie kann aber ergänzend in Frage kommen. Vielleicht trifft einer dieser Punkte auf Sie zu:</p>
<ul class="fragen">{fr}</ul>
<p style="margin-top:18px"><b>Ob die INUSpherese® für Sie infrage kommt, klären wir im Erstgespräch.</b></p></div>
<div class="box" style="align-self:center"><h3>Sie müssen das nicht selbst einschätzen.</h3><p>Im Erstgespräch sehen wir uns Ihre Vorgeschichte und Ihre Laborwerte an und sagen Ihnen offen, ob die INUSpherese® für Sie in Frage kommt oder ob etwas anderes besser passt.</p>
<div class="btns">{book('Erstgespräch vereinbaren')}</div>
<p class="small muted" style="margin:14px 0 0">Andere Beschwerden? Sprechen Sie uns trotzdem an: {tel()}</p></div>
</div></div></section>

<section id="ablauf"><div class="wrap"><div class="split">
<div><h2>So läuft es ab</h2>{schritte([
    ('Erstgespräch', ' Vorgeschichte, Beschwerden, Ziele und mögliche Gegenanzeigen. Die ärztliche Aufklärung findet mindestens 24 Stunden vor der ersten Behandlung statt, bei weiter Anreise auch telefonisch.'),
    ('Labor vorher', ' Wir messen die Werte, auf die es in Ihrem Fall ankommt.'),
    ('Zwei Behandlungen', ' Sie liegen bequem, über beide Armbeugen wird je ein Zugang gelegt. Etwa 2 bis 3 Stunden, unser Team ist die ganze Zeit bei Ihnen. Meist zwei Behandlungen innerhalb von fünf Tagen, mit mindestens einem Tag Pause dazwischen.'),
    ('Auswertung', ' Werte vorher und nachher im Vergleich, auf Wunsch mit Eluat-Analyse.'),
])}</div>
<div class="box"><h3>Was dazugehört</h3>{liste([
    'Ausführliche Anamnese vor dem ersten Termin',
    'Körperliche Untersuchung und Arztgespräch vor jeder Behandlung',
    'Überwachung von Kreislauf und Vitalwerten während der Behandlung',
    'Begleitende Infusionen, wenn ärztlich sinnvoll oder auf Wunsch',
    'Auf Wunsch Analyse des Eluats in einem externen Labor',
    'Nachgespräch',
])}
<p class="price-line" style="margin:16px 0 0"><b>Eine Behandlung voraussichtlich {price('apherese_sitzung', 'ab')}</b> · nach GOÄ, mit Kostenvoranschlag</p>
<p class="small" style="margin:12px 0 0">Als festes Paket: {a('medizin/apherese-programm/', 'Apherese-Programm')} · Für Gesunde: {a('longevity/apherese-reset/', 'Apherese Reset')}</p></div>
</div></div></section>

<section class="bg-white" id="verfahren"><div class="wrap">
<h2>INUSpherese, H.E.L.P. und andere Verfahren</h2>
<p style="max-width:760px">Apherese ist der Oberbegriff für Verfahren, bei denen Blut außerhalb des Körpers behandelt und wieder zurückgeführt wird. Sie unterscheiden sich darin, was sie aus dem Blut filtern. Welches für Sie in Frage kommt, klären wir im Gespräch.</p>
<div class="table-wrap"><table class="price-table"><tr><th>Verfahren</th><th>Kurz erklärt</th><th>Bei UMI</th></tr>{vt}</table></div>
</div></section>

<section id="team"><div class="wrap"><div class="split wide">
<div><h2>Unser Team und Ihre Sicherheit</h2>
<p>Ihre INUSpherese® betreut unsere Ärztin <b>Namrata Kafle</b>, Ärztin für Innere Medizin, gemeinsam mit zwei erfahrenen Pflegefachkräften. <b>Michaela Gusic</b> leitet unser INUSpherese-Zentrum und bringt über 25 Jahre Erfahrung aus der Dialyse mit, zuletzt als Leitung der Dialysestation am Klinikum Stuttgart. <b>Evelyn Gentsch</b> ist examinierte Kinderkrankenschwester mit langjähriger Erfahrung in der Kinderdialyse am Universitätsklinikum Tübingen.</p>
<p>Gemeinsam begleiten sie Sie vom Vorgespräch bis zur Auswertung.</p></div>
<div class="team-row">{''.join(f'<img src="{a_img(f)}" alt="{n}" width="480" height="720">' for f, n in [('team-namrata-kafle.jpg', 'Namrata Kafle'), ('team-michaela-gusic.jpg', 'Michaela Gusic'), ('team-evelyn-gentsch.jpg', 'Evelyn Gentsch')])}</div>
</div></div></section>

<section class="bg-soft" id="info-abend"><div class="wrap"><div class="banner" style="padding:0">
<div><span class="eyebrow">Kostenloser Info-Abend</span><h2>Mittwoch, 9. Dezember 2026, 17:30 Uhr</h2>
<p>Lernen Sie uns kennen: Wir erklären, wie die INUSpherese® funktioniert, was im Labor gemessen wird und für wen sie in Frage kommen könnte. Etwa 45 Minuten Vortrag, danach 30 Minuten für Ihre Fragen.</p>
<div class="btns"><a class="btn" href="{anmeldung}">Zum Info-Abend anmelden</a>{tel('btn ghost', 'Anmelden per Telefon')}</div></div>
<div class="box"><h3>Programm</h3>{liste(['Vorstellung Praxis und Team', 'Was ist Umweltmedizin?', 'Was sich im Blut ansammeln kann', 'So funktioniert die INUSpherese®', 'Was ergänzend möglich ist'])}</div>
</div></div></section>
{fh}
<section class="tight"><div class="wrap"><div class="hint"><p><b>Ob die INUSpherese® zu Ihnen passt, entscheiden wir gemeinsam,</b> nach einem ärztlichen Gespräch und mit Blick auf Ihre Werte.</p>{book('Erstgespräch vereinbaren', 'btn')}</div></div></section>"""
    return body, [fld, proc]


def help_apherese():
    fh, fld = faq([
        ("Was ist der Unterschied zur INUSpherese®?", "Beide Verfahren behandeln das Blutplasma außerhalb des Körpers. Die INUSpherese® filtert nach Molekülgröße. Bei der H.E.L.P.-Apherese werden bestimmte Bestandteile mit Heparin und einem sauren Puffer ausgefällt und dann abgefiltert. Sie ist vor allem auf Blutfette und Fibrinogen ausgerichtet."),
        ("Was bedeutet „außerhalb der Zulassung“?", "Ein Verfahren wird für einen Zweck eingesetzt, für den es nicht ausdrücklich zugelassen ist. Das ist in der Medizin erlaubt, setzt aber eine sorgfältige ärztliche Prüfung im Einzelfall und eine ausführliche Aufklärung voraus. Darüber sprechen wir offen mit Ihnen."),
        ("Wie lange dauert eine Behandlung?", "Etwa zwei bis drei Stunden. Sie liegen bequem, unser Team überwacht Kreislauf und Werte die ganze Zeit."),
        ("Ist die Behandlung gut verträglich?", "Wie bei jeder Behandlung am Blutkreislauf kann es zu Nebenwirkungen kommen, zum Beispiel Kreislaufschwäche oder Blutergüsse. Weil Heparin eingesetzt wird, prüfen wir vorher auch die Blutgerinnung. Über alle Risiken klären wir Sie vorher ausführlich auf."),
        ("Was kostet die H.E.L.P.-Apherese?", f"Eine Behandlung voraussichtlich {price('help_sitzung', 'ab')}. Die genauen Kosten stehen in Ihrem schriftlichen Kostenvoranschlag. Die Off-Label-Anwendung erstatten Versicherungen in der Regel nicht."),
    ])
    proc = {"@context": "https://schema.org", "@type": "MedicalTherapy", "name": "H.E.L.P.-Apherese",
            "alternateName": "Heparin-induzierte extrakorporale LDL-Präzipitation",
            "description": "Apherese-Verfahren, bei UMI Stuttgart als Off-Label-Anwendung nach ärztlicher Prüfung."}
    werte = [("LDL-Cholesterin", "das „schlechte“ Cholesterin"), ("Lipoprotein(a)", "ein vor allem erblich bedingtes Blutfett"),
             ("Fibrinogen", "ein Gerinnungseiweiß"), ("Triglyceride", "Neutralfette im Blut"), ("CRP", "ein Entzündungswert")]
    wk = "".join(f'<div class="stoff filter"><span class="nr">{i}</span><h3>{n}</h3><p class="sub">{d}</p></div>' for i, (n, d) in enumerate(werte, 1))
    body = f"""{hero('Apherese · UMI Medizin', 'H.E.L.P.-Apherese in Stuttgart<span class="h1-sub">Off-Label-Anwendung, nur nach ärztlicher Prüfung</span>',
    'Die H.E.L.P.-Apherese ist ein seit über 30 Jahren etabliertes Apherese-Verfahren. Ihr Blutplasma wird außerhalb des Körpers behandelt: Bestimmte Blutfette und Eiweiße werden ausgefällt und abgefiltert, danach bekommen Sie Ihr Plasma zurück.',
    book('Arztgespräch vereinbaren') + a('inuspherese-zentrum-stuttgart/#verfahren', 'Vergleich der Verfahren', 'btn ghost'), 'med',
    '<ul class="pills"><li>Ihr eigenes Plasma, ohne Ersatzlösung</li><li>Ambulant, etwa 2 bis 3 Stunden</li><li>Nur nach ärztlicher Prüfung</li></ul>')}

<section class="bg-white" id="verfahren"><div class="wrap"><div class="split">
<div><span class="eyebrow">So funktioniert es</span><h2>Ausfällen statt nur filtern</h2>
<p>Das Blut wird zunächst in Blutzellen und Plasma getrennt. Dem Plasma werden Heparin und ein saurer Puffer zugesetzt. Dadurch ändert sich der pH-Wert, und bestimmte Bestandteile wie LDL-Cholesterin und Fibrinogen fallen aus. Ein Filter hält sie zurück.</p>
<p>Anschließend wird das Plasma wieder neutralisiert, mit Ihren Blutzellen zusammengeführt und über die andere Armvene zurückgegeben.</p></div>
<div class="svg-schema">{schema_svg()}</div></div></div></section>

<section id="werte"><div class="wrap">
<span class="eyebrow">Was ausgefällt wird</span><h2>Welche Bestandteile das Verfahren erfasst</h2>
<div class="stoffe">{wk}</div>
<div class="note" style="font-size:17px;margin-top:28px"><b>Nur als Off-Label-Anwendung:</b> Wir setzen die H.E.L.P.-Apherese ausschließlich im Einzelfall außerhalb der Zulassung ein. Ob das für Sie infrage kommt und welche Risiken es gibt, besprechen wir ausführlich im Arztgespräch.</div>
</div></section>

<section class="bg-white" id="ablauf"><div class="wrap"><div class="split">
<div><h2>So läuft es ab</h2>{schritte([
    ('Arztgespräch', ' Vorgeschichte, Laborwerte, Gegenanzeigen. Wir prüfen, ob die H.E.L.P.-Apherese für Sie infrage kommt, und klären Sie ausführlich auf.'),
    ('Labor vorher', ' Blutfette, Fibrinogen, Entzündungswerte und Gerinnung.'),
    ('Behandlung', ' Im Liegen, etwa 2 bis 3 Stunden, mit ständiger Überwachung durch unser Pflegeteam.'),
    ('Auswertung', ' Werte vorher und nachher im Vergleich, und die Frage, ob weitere Behandlungen sinnvoll sind.'),
])}</div>
<div class="box"><h3>Kosten</h3><p>Eine Behandlung voraussichtlich <b>{price('help_sitzung', 'ab')}</b>, nach GOÄ. Vor Beginn erhalten Sie einen schriftlichen Kostenvoranschlag.</p>
<p>Ob Ihre private Krankenversicherung oder Beihilfe erstattet, hängt von Ihrem Tarif und vom Anlass ab. Die Off-Label-Anwendung erstatten Versicherungen in der Regel nicht.</p>
<p style="margin:0">{a('kosten/', 'Mehr zu Kosten und Erstattung')}</p></div>
</div></div></section>
{team_mini(['kafle', 'gusic', 'gentsch'])}
{fh}
<section class="tight"><div class="wrap"><div class="hint"><p><b>Ob die H.E.L.P.-Apherese zu Ihnen passt, entscheiden wir gemeinsam,</b> nach einem ärztlichen Gespräch und mit Blick auf Ihre Werte. Telefon {tel()}</p>{book('Arztgespräch vereinbaren', 'btn')}</div></div></section>"""
    return body, [fld, proc]


# ------------------------------------------------------------ Pakete

def apherese_programm():
    return paket(
        eyebrow="Paket · UMI Medizin", line="med",
        h1="Apherese-Programm",
        lead="Für Menschen mit anhaltenden Beschwerden, bei denen eine Apherese sinnvoll sein kann. Das Programm bündelt Vorgespräch, Diagnostik, zwei Sitzungen INUSpherese, Eluat-Analyse und Nachgespräch in einem festen Ablauf.",
        preis_html=price("apherese_programm"),
        enthalten=["Beratungs- und Vorgespräch mit der Ärztin", "Diagnostik vor der Behandlung", "2 Sitzungen INUSpherese",
                   "Eluat-Analyse der abgefilterten Bestandteile", "Begleitende Infusionen nach ärztlicher Empfehlung", "Nachgespräch mit Befunden",
                   "Hilfe beim Erstattungsantrag an PKV oder Beihilfe"],
        ablauf=[("Vorgespräch", " Telefon, Video oder in der Praxis. Wir prüfen, ob die Apherese für Sie passt."),
                ("Diagnostik", " Labor und Untersuchung, danach Kostenvoranschlag."),
                ("Zwei Sitzungen", " Je etwa zwei bis drei Stunden, innerhalb von fünf Tagen, mit mindestens einem Tag Pause dazwischen."),
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
        ("basisdiagnostik", "Basisdiagnostik", [
            ("Immunstatus", "Immunglobuline IgG, IgA, IgM, IL-6, optional Lymphozytenprofil, Th1/Th2-Balance und NK-Zellen"),
            ("Entzündungsstatus", "hsCRP, IL-6, optional TNF-α, Lipidperoxidation und Nitrotyrosin"),
            ("Belastungsscreening", "oxidativer Stress, Glutathion, Q10, optional Schwermetalle und Mitochondrienfunktion"),
            ("Organscreening", "Leber, Niere, Schilddrüse"),
            ("Dunkelfeldmikroskopie", "Betrachtung eines frischen Blutstropfens unter dem Mikroskop")]),
        ("erweitertediagnostik", "Erweiterte Diagnostik", [
            ("Mikrobiom-Analyse", "Darmflora, Gleichgewicht der Bakterien, Entzündung und Barrierefunktion"),
            ("Nahrungsmittelunverträglichkeiten", "gezielte Tests, abgestimmt auf Ihre Beschwerden"),
            ("Vitamine", "z. B. Vitamin D, B-Komplex, Folat, B12"),
            ("Mineralstoffe und Spurenelemente", "z. B. Magnesium, Zink, Selen"),
            ("Aminosäurenprofil", ""),
            ("Zellenergie", "oxidativer Stress und Mitochondrien, z. B. Glutathion, Q10, Laktat/Pyruvat"),
            ("Omega-3-Index", "Verhältnis der Fettsäuren im Blut (AA/EPA)"),
            ("Hormonstatus", "Hormonachsen, abgestimmt auf Ihre Fragestellung"),
            ("Neurostress-Profil", "Stresshormone und Botenstoffe"),
            ("Neuro- und Autoimmunprofile", "spezielle Antikörper- und Botenstoffprofile, z. B. bei anhaltender Erschöpfung nach Infektionen"),
            ("HRV- und VNS-Analyse", "Herzratenvariabilität und vegetatives Nervensystem"),
            ("Erweitertes Labor", "Blutgerinnung, Hormonachsen, Histamin und Mastzellen")]),
        ("umwelt", "Umweltmedizin", [
            ("Schwermetalle", "z. B. Aluminium, Blei, Cadmium, Quecksilber, Arsen"),
            ("Umweltbelastungen", "z. B. Pestizide und ausgewählte PFAS"),
            ("Eluat-Analyse", "Analyse der abgefilterten Rückstände nach der INUSpherese®")]),
        ("untersuchungen", "Untersuchungen in der Praxis", [
            ("Körperliche Untersuchung", "mit ausführlicher Anamnese"), ("Ruhe-EKG", ""),
            ("Ultraschall", "Bauchorgane und Nieren"),
            ("Blutdruck und Kreislauf", "Blutdruckanalyse, Puls, Sauerstoffsättigung"),
            ("Herz-Lungen-Funktion", "Lungenfunktion und Pulsoxymetrie"),
            ("Urin und Stuhl", "je nach Fragestellung")]),
    ]
    html = ""
    for i, (anchor, h, items) in enumerate(blocks):
        cards = "".join(f'<div class="card"><h3>{n}</h3><p class="small">{d}</p></div>' for n, d in items)
        html += f'<section class="{"bg-white" if i % 2 == 0 else ""}" id="{anchor}"><div class="wrap"><h2>{h}</h2><div class="grid g3" style="margin-top:20px">{cards}</div></div></section>'
    fh, fld = faq([
        ("Kann ich einzelne Laborwerte bestellen?", "In der Medizin stellen wir die Diagnostik nach dem Gespräch zusammen, damit nur gemacht wird, was weiterhilft. Feste Pakete sind der Energie-Check und bei UMI Longevity der Longevity-Check."),
        ("Wer rechnet das Labor ab?", "Häufig rechnet das Fachlabor direkt mit Ihnen ab. Das steht vorab in Ihrem Kostenvoranschlag."),
    ])
    body = f"""{hero('Diagnostik · UMI Medizin', 'Labordiagnostik in Stuttgart: genau hinschauen',
    'Mehr als der Routine-Check: Viele Ursachen bleiben bei einer üblichen Untersuchung unentdeckt. Nach dem Erstgespräch wählt unsere Ärztin die Bausteine aus, die in Ihrem Fall weiterhelfen. Für eine Rundum-Untersuchung gibt es den ' + a('internistische-sprechstunde/#check-up', 'Gesundheits-Check-up') + '.',
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
    Page("darmgesundheit", "Darmgesundheit und Mikrobiom in Stuttgart · UMI Medizin",
         "Darm und Verdauung bei UMI Stuttgart: Mikrobiom-Analyse, Tests auf Nahrungsmittelunverträglichkeiten, Darmaufbau mit Plan. Erstgespräch online buchen.",
         darm, line="med", nav="med", crumbs=MED + [(None, "Darm und Verdauung")]),
    Page("sub-health-syndrom", "Ständig müde? Erschöpfung abklären in Stuttgart · UMI",
         "Erschöpfung und Energie: Ursachen finden, wenn Sie ständig müde sind und die Werte normal. Erstgespräch oder Energie-Check bei UMI Stuttgart.",
         subhealth, line="med", nav="med", crumbs=MED + [(None, "Erschöpfung und Energie")]),
    Page("long-covid-sprechstunde", "Beschwerden nach Infektionen · UMI Medizin Stuttgart",
         "Anhaltende Beschwerden nach Infektion oder Impfung: gründliche Abklärung und Begleitung in Stuttgart-Vaihingen. Vorgespräch auch per Video.",
         infektionen, line="med", nav="med", crumbs=MED + [(None, "Beschwerden nach Infektionen")]),
    Page("inuspherese-zentrum-stuttgart", "INUSpherese-Zentrum Stuttgart: Blutplasma filtern · UMI",
         "INUSpherese-Zentrum Stuttgart-Vaihingen: Blutplasma filtern und das Ergebnis im Labor sehen. Ablauf, Verfahren, Team, Info-Abend am 9.12. Erstgespräch online.",
         apherese, nav="aph", crumbs=[(None, "Apherese")]),
    Page("medizin/help-apherese", "H.E.L.P.-Apherese in Stuttgart · UMI Medizin",
         "H.E.L.P.-Apherese bei UMI Stuttgart: Off-Label-Anwendung nach ärztlicher Prüfung. Wie das Verfahren funktioniert, Ablauf, Kosten nach GOÄ.",
         help_apherese, line="med", nav="aph", crumbs=MED + [(None, "H.E.L.P.-Apherese")]),
    Page("medizin/apherese-programm", "Apherese-Programm Stuttgart · UMI Medizin",
         "Apherese-Programm bei UMI Stuttgart: Vorgespräch, Diagnostik, zwei Sitzungen INUSpherese, Eluat-Analyse. Voraussichtliche Kosten nach GOÄ.",
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
