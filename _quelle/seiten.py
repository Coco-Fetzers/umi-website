"""Alle Seiten der Website, gesammelt aus den Teilen."""
import seiten_dach

PAGES = list(seiten_dach.PAGES)

try:
    import seiten_medizin
    PAGES += seiten_medizin.PAGES
except ImportError:
    pass
try:
    import seiten_longevity
    PAGES += seiten_longevity.PAGES
except ImportError:
    pass
