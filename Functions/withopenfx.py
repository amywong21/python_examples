# Mit file.close Datei schließen.
file = open("data/lesen.txt", "r")

for line in file:
	print(line)

file.close()

# Mit with open() muss ich mich um das Schließen der Datei nicht kümmern.
def example_withopen():
	with open("data/lesen.txt", "r") as file:
		for line in file:
			print(line)

	# Um einen Zeilenumbruch einzufügen, muss ich ein Steuerzeichen \n verwenden.
	# Ein Steuerzeichen verändert den Textfluss.
	print("HAL\nLO")
	print("WELT")
	
	# Überprüfen ob Steuerzeichen da ist. Gib mir das letzte Zeichen und überprüfe ob das ein Steuerzeichen ist. 
	file = open("data/lesen.txt", "r")
	for line in file:
		# Erklärung für folgende Zeile
		# line = "Hallo Welt 123!!!"\n" 
		
		# line[-1] gibt uns das letzte Element einer Liste
		print(line[-1] == "\n")
	
	# Steuerzeichen oder Leerzeichen entfernen mit .strip()
	file = open("data/lesen.txt", "r")
	for line in file:
		print(line.strip())

	# Gib mir die ersten 5 Zeilen aus.
	with open("data/names.csv", "r")as file:
		counter = 0 
		for line in file:
			counter = counter + 1
			print(line)
	
			if counter >= 4:
				break	