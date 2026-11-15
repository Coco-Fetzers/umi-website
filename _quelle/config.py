"""
UMI Stuttgart – zentrale Angaben.

Hier stehen alle Werte, die sich ändern können: Preise, Links, Kontakt.
Nach einer Änderung einmal  python3 _quelle/build.py  ausführen.
"""

JAHR = 2026
DOMAIN = "https://umi-stuttgart.de"
# <base> für die 404-Seite: Vorschau auf GitHub Pages liegt im Unterordner /umi-website/
BASIS_VORSCHAU = "/umi-website/"
BASIS_LIVE = "/"

# ------------------------------------------------------------ Kontakt
NAME_LANG = "UMI Stuttgart – Umweltmedizinisches Institut"
STRASSE = "Schulze-Delitzsch-Str. 38"
PLZ = "70565"
ORT_LANG = "Stuttgart-Vaihingen"
TEL = "0711 40 79 50 02"
TEL_LINK = "+4971140795002"
TEL_INTL = "+49 711 40795002"
FAX = "0711 40 18 92 96"
MAIL = "info@umi-stuttgart.de"
MAIL_BEWERBUNG = "verwaltung@umi-stuttgart.de"
# PRÜFEN: Die heutige Seite nennt meist Mo–Fr 8:30–16:30, das Impressum Fr nur bis 12:00.
OEFFNUNGSZEITEN = "Montag bis Freitag, 8:30 bis 16:30 Uhr"
OEFFNUNGSZEITEN_LD = "Mo-Fr 08:30-16:30"
INSTAGRAM = "https://www.instagram.com/umistuttgart/"
FACEBOOK = "https://www.facebook.com/umistuttgart/"

# ------------------------------------------------------------ Buchung und Shop
# Ein Doctolib-Profil für alle Knöpfe (heute gibt es zwei). PRÜFEN, welches bleibt.
DOCTOLIB = "https://www.doctolib.de/privatpraxis/stuttgart/umi-stuttgart"
# Link zum Gutschein-Shop, sobald er eingerichtet ist. None = Knopf "in Kürze".
GUTSCHEIN_SHOP = None

# ------------------------------------------------------------ Preise
# None = Platzhalter "ab … €" auf der Website. Werte als Text eintragen,
# z. B. "449 €" oder "ca. 1.900 €". Vorschläge stehen im Kommentar.
PREISE = {
    # UMI Medizin
    "apherese_programm": None,   # Vorschlag 5.300 €
    "apherese_sitzung": None,    # Vorschlag ca. 2.258 € je Sitzung INUSpherese
    "help_sitzung": None,        # nach Kostenvoranschlag
    "energie_check": None,       # Vorschlag 690 €
    "kur_hyperthermie": None,    # Vorschlag ca. 1.900 € (6 Sitzungen)
    "kur_oxyvenierung": None,    # Vorschlag ca. 480 € (12 Sitzungen)
    "kur_farblaser": None,       # Vorschlag ca. 540 € (12 Sitzungen)
    "hyperthermie_sitzung": None,
    "erstgespraech": None,
    # UMI Longevity
    "longevity_check": None,     # Vorschlag 449 €
    "nad_infusion": None,        # Vorschlag ab ca. 199 € je Infusion
    "infusion_erste": None,      # Vorschlag ab 119 €
    "infusion_weitere": None,    # Vorschlag ab ca. 59 bis 69 €
    "supplement_analyse": None,  # Vorschlag 299 €
    "apherese_reset": None,      # Vorschlag ab ca. 5.400 €
}

# ------------------------------------------------------------ Weiterleitungen
# (alte Adresse, neue Adresse) – als 301 in .htaccess und als Weiterleitungsseite
WEITERLEITUNGEN = [
    ("leistungen", "medizin/"),
]
