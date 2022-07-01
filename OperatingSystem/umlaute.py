import os

def example_umlaute():
	# Neuer Ordner erstellen mit mkdir
	#datadir = os.path.join(os.path.dirname(__file__), "..", "data", "new")
	#os.mkdir(datadir)

	# Öffne Datei mit UTF-8 encoding.
	filename = os.path.join(os.path.dirname(__file__), "..", "data", "umlaute.txt")
	# als UTF-8 betrachten
	with open(filename, "r", encoding="utf-8") as file:
		for line in file:
			print(line)

	# Neue Datei mit UTF-8 encoding im Ordner data erstellen
	# und was rein schreiben (siehe Bsp. im VSCode).
	filename_out = os.path.join(os.path.dirname(__file__), "..", "data", "umlaute_out.txt")

	with open(filename_out, "w", encoding="utf-8") as file:
		file.write("Müller")

example_umlaute()