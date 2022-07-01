
def example_string_all():
	example_string_01()
	example_string_02()
	example_string_03()

def example_string_01():
	# Das Wort in Großbuchstaben ausgeben.
	w = "Hallo"
	print(w.upper())
	print("Hallo".upper())

	# Das Wort in Kleinbuchstaben ausgeben.
	w = "Hallo"
	print(w.lower())
	print("Hallo".lower())

	# Nach Zeichen prüfen.
	sentence = "Ist das Wetter heute gut?"
	if sentence[-1] == "?" :
		print("Der Satz endet mit einem Fragezeichen")

def example_string_02():
	# alternativ .endswith("") Funktion
	sentence = "Ist das Wetter heute gut?"
	if sentence.endswith("?"):
		print("Der Satz endet mit einem Fragezeichen")

	# Ob mit einem bestimmten Wort beginnt
	sentence = "Ist das Wetter heute gut???"

	if sentence.endswith("???"):
		print("Der Satz endet mit einem Fragezeichen")

	if sentence.startswith("Ist"):
		print("Der Satz beginnt mit einem 'ist'")

def example_string_03():
	# Leerzeichen entfernen
	word = " Hallo."
	print(word.strip(" "))

	# Leerzeichen und Punkt entfernen
	word = " Hallo."
	print(word.strip(" ."))

	# Kann bestimmen von welcher Seite ein Zeichen entfernt werden soll
	word = "_Hallo._"
	print(word.strip("_.")) # alle Unterstriche und Punkte werden entfernt
	print(word.lstrip("_")) # Unterstrich auf der linken Seite wird entfernt
	print(word.rstrip("_")) # Unterstrich auf der rechten Seite wird entfernt

	# Satzzeichen am Ende entfernen
	word = "_Hallo._"
	print(word.strip("_.")) # alle Unterstriche und Punkte werden entfernt
	print(word.lstrip("_")) # Unterstrich auf der linken Seite wird entfernt
	print(word.rstrip("_")) # Unterstrich auf der rechten Seite wird entfernt

	sentence = "Ist das Wetter heute,und morgen gut???"
	print(sentence.rstrip("!?.,"))

	# Herausfinden an welcher Stelle das Komma steht. 
	# Wenn ein Zeichen nicht zu finden ist, dann kommt -1 raus.
	sentence = "Ist das Wetter heute, und morgen gut???"
	print(sentence.find(","))
	print(sentence.find("!"))

	# Wenn ich in einem String ein Zeichen durch ein anderes Zeichen 
	# ersetzen will. Komma durch ein Semikolon ersetzen. 
	sentence = "Ist das Wetter heute, und morgen gut????"
	print(sentence.replace(",", ";"))
	print(sentence.replace("u", "ü"))
	print(sentence.replace("und", "oder"))

	s = "Morgen werde ich so richtig produktiv sein"
	print(s.replace("Morgen", "Heute"))

	n = 5
	print ("ich habe XXX Hunde".replace("XXX", str(n)))
	print("Ich habe {0} Hunde".format(n))
	# Wenn ich Index benutze ist es Reihenfolge abhängig.

	print("Ich habe {0} {1} {0}".format(5, "Katzen"))
	print("Ich habe {1} {0}x".format(5, "Katzen"))
	print("Pi hat den Wert: {0}".format(3.141529))
	print("Pi hat den Wert: {0:.3f}".format(3.141529)) # .3f = drei Nachkommastellen
	print("Ich habe {number:.3f} {animal}".format(number = 5, animal = "Hunde"))
	print("Ich habe {number:f} {animal}".format(number = 5, animal = "Hunde"))

	# Wenn ich die Parameter benenne, dann ist die Reihenfolge egal.
	print("Ich habe {number} {animal}".format(animal = "Hunde", number = 5))

	# string.strip() Funktion
	s = " ... ein Gedanke... "
	print(s.strip(" ."))
example_string_all()