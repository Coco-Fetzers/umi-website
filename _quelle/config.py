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
# z. B. "449 €" oder "ca. 1.900 €".
PREISE = {
    # UMI Medizin
    "apherese_programm": None,
    "apherese_sitzung": None,
    "help_sitzung": None,
    "energie_check": None,
    "kur_hyperthermie": None,
    "kur_oxyvenierung": None,
    "kur_farblaser": None,
    "hyperthermie_sitzung": None,
    "erstgespraech": None,
    # UMI Longevity
    "longevity_check": None,
    "nad_infusion": "349 €",
    "infusion_ab": "55 €",
    "darm_infusion": "109 €",
    "supplement_analyse": None,
    "apherese_reset": "ca. 5.400 €",
}

# Infusionsmenü (CoCo, 19.11.): ein Preis je Infusion, inkl. kurzem ärztlichem Gespräch.
# None = Platzhalter "… €". Auf der Website mit "ca.".
INFUSIONSPREISE = {
    "winter": "69 €", "winter_plus": "169 €", "myers": "139 €",
    "recharge": "79 €", "recharge_plus": "139 €", "recharge_premium": "169 €",
    "sport": "55 €", "sport_plus": "135 €", "night_out": None,
    "longevity": "139 €", "longevity_plus": "179 €", "longevity_premium": "219 €",
    "glow": "55 €", "glow_plus": "185 €", "mito": "109 €", "mito_plus": "239 €",
    "nad": "349 €",
}

# ------------------------------------------------------------ Weiterleitungen
# (alte Adresse, neue Adresse) – als 301 in .htaccess und als Weiterleitungsseite
WEITERLEITUNGEN = [
    ("leistungen", "medizin/"),
]
