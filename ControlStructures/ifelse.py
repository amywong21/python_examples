
# Die Bedingungen werden meist unter Verwendung von Operatoren formuliert:
# Arithmetische Vergleichsoperatoren: ==, !=, <, <=, >, >=
# Logische Operatoren: and, or, not.
# Boolean ist ein Datentyp. Ist kein String oder eine Zahl, 
# sondern kann True oder False sein.
def example_boolean():
	print("6 < 5:" + str(6 < 5))
	print("5 < 6:" + str(5 < 6))

	b = False
	print(b)

	result = 5 < 6
	if result:
		print("5 ist kleiner als 6'")

	print("5 < 6:" + str(5 < 6))
	print("5 > 6:" + str(5 > 6))
	print("6 > 5:" + str(6 > 5))

	print("5 < 5:" + str(5 < 5))
	print("5 <= 5:" + str(5 <= 5))

	print("5 > 5:" + str(5 > 5))
	print("5 >= 5:" + str(5 >= 5))

	age = 25
	print(age < 30)

	age = 25
	print(age < 30)

	age = 25
	above_30 = age >= 30
	print(above_30)

	age = 25
	above_20 = age >= 20
	print(above_20)

	if above_20:
		print("if-Abfrage wurde ausgeführt")

	# "or" ist erfüllt, wenn entweder rechts oder links ein True steht
	# "and" ist erfüllt, wenn beide Seiten True sind.
	# Sobald auf einer Seite von and eine Lüge steht ist das Ergebnis auch eine Lüge. 
	print("True and True:" + str(True and True)) # True
	print("True and False:" + str(True and False)) # False
	print("False and True:" + str(False and True)) # False
	print("False and False:" + str(False and False)) # False

	print("True or True:" + str(True or True)) # True
	print("True or False:" + str(True or False)) # True
	print("False or True:" + str(False or True)) # True
	print("False or False:" + str(False or False)) # False

# Fallunterscheidung mit if-then-else Bedingung 
def example_if_else():
	print("Running example_if_else from module ifelse")
	currency = "€"

	if currency == "$":
		print("US-Dollar")
	elif currency == "¥":
		print("Japanischer Yen")
	elif currency == "€":
		print("Euro")
	elif currency == "฿":
		print("Thai Baht")
	else: 
		print("sonstige Währung")

	country = "US"
	age = 20

	if (country == "US" and age >= 21) or (country != "US" and age >= 18):
		print("Diese Person darf Alkohol trinken")
	# False or False, also wird es nicht ausgedruckt

	# Ungleichoperator
	print("Ungleichoperator: ")
	word = " Hallo"
	print(word != "Hallo")
	print(word != "Welt")

	# if-Verknüpfung
def example_if_Verknüpfung():
	print("if-Verknüpfung: ")
	age = 35
	if age >= 30 and age <= 39:
		print("Diese Person ist in Ihren 30-ern")

	age = 45 
	if age < 30 or age >= 40:
		print("Diese Person ist nicht in Ihren 30-ern")

	# Kompakte Schreibweise 
	wort ='start'
	if wort =='start':
		x ='los'
	else:
		x ='halt'
	print(x)

	wort ='start'
	x = ('los' if wort =='start' else 'halt')
	print(x)