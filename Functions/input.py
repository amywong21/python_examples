def example_input_all():
	example_input_01()
	example_input_02()

def example_input_01():
	print("Hallo Welt")
	age = input("Bitte gebe dein Alter ein: ")
	print(age) # hier kann ich im ausgabe Fenster eine Zahl eingeben, dass dann ausgegeben wird

	# Das Alter von Personen eingeben und zusammen zählen lassen.
	print("Hallo Welt")
	age1 = input("Bitte gebe das Alter von Person A ein: ")
	age2 = input("Bitte gebe das Alter von Person B ein: ")
	print(age1)
	print(age2)

	print("Person a + Person B")
	print(int(age1) + int(age2))
	print(float(age1) + float(age2))

def example_input_02():
	print("BMI - Rechner")
	weight = float(input("Bitte geben Sie hier Ihr Gewicht in kg ein: "))
	height = float(input("Bitte geben Sie hier Ihre Körpergröße in Meter ein: "))

	print("BMI Formel = [Gewicht in kg] / [Körpergröße in m]^2")
	print("BMI = ", weight / height **2)

	# Alternative Schreibweise, um str in Kommazahlen umzuwandeln.
	print("BMI - Rechner")
	weight_str = input("Bitte geben Sie hier Ihr Gewicht in kg ein: ")
	height_str = input("Bitte geben Sie hier Ihre Körpergröße in Meter ein: ")
	weight = float(weight_str)
	height = float(height_str)
	bmi = weight/ height ** 2

	print("Der BMI ist: " + str(bmi))
	print("Der BMI ist: " + str(round(bmi, 1))) #auf erste Kommazahl aufrunden

	# Wenn ich die deutsche Kommaschreibweise erlauben möchte.
	print("BMI - Rechner")
	weight_str = input("Bitte geben Sie hier Ihr Gewicht in kg ein: ")
	height_str = input("Bitte geben Sie hier Ihre Körpergröße in Meter ein: ")
	weight = float(weight_str.replace(",", "."))
	height = float(height_str.replace(",", "."))
	bmi = weight/ height ** 2

	print("Der BMI ist: " + str(bmi))
	print("Der BMI ist: " + str(round(bmi, 1)))