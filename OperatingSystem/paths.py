import os

def example_paths():
	example_paths_01()
	example_paths_02()
	example_paths_03()

def example_paths_01():
	# Ohne absolutem Pfad, sondern mit relativem Pfad. Vorteil, dann kann ich die Dateien verschieben 
	# und finde die Datei trotzdem. Hier benutze ich join, um Plattform unabhängig zu sein:
	# Das Trennzeichen zwischen Ordner ist auf Windows ein \ und auf Linux, Mac ein /.

	print(__file__)
	print(os.path.dirname(__file__))
	# ".." heißt einen Ebene nach oben vom aktuellem path
	path = os.path.join(os.path.dirname(__file__), "..", "data", "schreiben.txt")
	with open(path, "r") as file:
		for line in file:
			print(line)

	print(os.listdir("."))


def example_paths_02():
	folder = os.path.join(os.path.dirname(__file__), "..", "data")
	print(os.path.dirname(__file__))
	print(folder)

	for file in os.listdir(folder):
		file_path = os.path.join(folder, file)
		if os.path.isdir(file_path):
			print(file + " ist ein Ordner")
		else:
			print(file + " ist eine Datei")

def example_paths_03():
	print(__file__)
	print(os.path.dirname(__file__))

	path = os.path.join(os.path.dirname(__file__), "data", "names")

	print(os.listdir(path))

	files = os.listdir(path)

	count = 0

	for file in files:
		with open(os.path.join(path, file), "r", encoding="utf-8") as file:
			for line in file:
				names = line.split(" ")
				if names[0] == "Max":
					count = count + 1
					print(str(file) + ": " + line)

	print(count)

example_paths()
