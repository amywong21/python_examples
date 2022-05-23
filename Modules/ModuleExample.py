# Modul erstellen
# hallo.py Datei erstellt
# welche Funktionen enthält:

def example_modules():
	print("")

# Modul importieren
import Modules.hallo as hallo
hallo.welt()
hallo.mars()

# Nur bestimmte Funktionen aus einem Modul importieren.
from Modules.hallo import welt, mars

welt()
mars()

# Alle Funktionen aus einer Datei importieren
from Modules.hallo import *

welt()
mars()