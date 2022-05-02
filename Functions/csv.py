def example_csv():
	with open("data/datei.csv") as file:
		for line in file:
			data = line.strip().split(";")
			print(data)
			# in andere Form verpacken
			print(data[0] + ": " + data[1] + " / " + data[2])
			# Muenchen: 1800000 / MUC
			# Berlin: 3000000 / BER
			# Budapest: 2000000 / BUD

			# Wenn ich auf die dritte Spalte zugreifen möchte. 
			print(data[2])
			print(data)
			# MUC
			# ['Muenchen', '1800000'; 'MUC']
			# BER
			# ['Berlin', '3000000'; BER]
			# BUD
			# ['Budapest', '2000000', 'BUD']
			
			# Zeile München überspringen: Wenn in der dritten Spalte BUD oder BER steht, 
			# dann führen wir bitte diesen print Code aus.
			if data[2] == "BER" or data[2] == "BUD":
				print(data[2])
				print(data)

	# Nach Zahl filtern. String umwandeln in eine Zahl mit int().
	with open("data/datei.csv") as file:
		for line in file:
			data = line.strip().split(";")
			if int(data[1]) >= 2000000:
				print(data)	
	# ['Berlin', '3000000', 'BER']
	# ['Budapest', 2000000', 'BUD']

	# Zeilen überspringen wo Einwohnerzahl kleiner als 2000000 ist und wo Airport BUD heißt.
	with open("data/datei.csv") as file:
		for line in file:
			data = line.strip().split(";")

			if int(data[1]) < 2000000:
				continue
		
			if data[2] == "BUD":
				continue
		
			print(data)
