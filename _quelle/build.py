#!/usr/bin/env python3
"""
UMI Stuttgart – Seiten erzeugen.

Aufruf aus dem Hauptordner:
  python3 _quelle/build.py          Vorschau (noindex, robots gesperrt)
  python3 _quelle/build.py --live   für die Veröffentlichung auf umi-stuttgart.de

Inhalte: _quelle/seiten*.py · Preise, Links, Kontakt: _quelle/config.py
Rahmen (Kopf, Fuß, Hilfen): _quelle/rahmen.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rahmen  # noqa: E402

rahmen.main()
