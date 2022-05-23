
# 1) Vervollständige die Klasse "FileReader" so, dass bei Aufruf der 
# lines() - Methode die Datei Zeile für Zeile eingelesen wird. 
# Die lines() - Methode soll dann eine Liste der Zeilen in der Datei zurückgeben.

class FileReader():
	def __init__(self, file):
		self.file_path = file
	
	def lines(self):  
		listoflines = []

		with open(self.file_path, "r") as file:
			for line in file:
				print(line)       
				listoflines.append(line.strip())
			# wenn ich kein return definiere, dann ist der return None. 
			return listoflines

# Wir speichern den konstruierten FileReader in der Variablen reader,
# damit wir ihn später unter diesem Namen benutzen können
reader = FileReader("./data/datei.csv")
# wenn reader.lines() keinen expliziten return hat,
# hat er einen impliziten return None
print(reader.lines())

# 2) Tabellenüberschrift weglassen
class FileReader():
	def __init__(self, file):
		self.file_path = file
	
	def lines(self):  
		listoflines = []
		counter = 0

		with open(self.file_path, "r") as file:
			for line in file:
				if counter == 0:
					counter = counter + 1
					continue
				
				print(line)       
				listoflines.append(line.strip())
			return listoflines

reader = FileReader("./data/datei.csv")
print(reader.lines())

# 3) Dateiverarbeitung einmal im Konstruktor machen, Ergebnisse mehrfach nutzen.
class FileReader():
	# Die große Arbeit wird einmal im Konstruktor geleistet
	def __init__(self, file):        
		self.listoflines = []
		counter = 0

		with open(file, "r") as file:
			for line in file:
				if counter == 0:
					counter = counter + 1
					continue
				
				print(line)       
				self.listoflines.append(line.strip())
		
	# Hier werden die Ergebnisse der großen Arbeit nur returned
	def lines(self):  
		return self.listoflines

reader = FileReader("./data/datei.csv")
# Ergebnisse mehrfach nutzen
print(reader.lines())
print(reader.lines())
print(reader.lines())

# 4)Erstelle die Klasse "CsvReader", sodass der "FileReader" erweitert wird. 
# Bei Aufruf der lines() soll die Datei als .csv-Datei eingelesen werden,
# sprich es soll eine mehrdimensionale Liste zurückgegeben werden.

# **Wichtig:** Überlass' das Einlesen der Datei dem "FileReader", und erweitere 
# die lines() - Methode im Csv-Reader um die Funktionalität, die benötigt wird, 
# damit die mehrdimensionale Liste zurückgegeben wird!
class FileReader():
	def __init__(self, file):
		self.file_path = file
	
	def lines(self):  
		listoflines = []

		with open(self.file_path, "r") as file:
			for line in file:
				print(line)       
				listoflines.append(line.strip())
			# wenn ich kein return definiere, dann ist der return None. 
			return listoflines
		
class CsvReader(FileReader):
	def __init__(self, file): # damit ich CsvReader("./data/datei.csv") später aufrufen kann
				# super() ruft die Klasse die in der Klammer steht auf
				# hier ist es FileReader
		super().__init__(file)
	
	def lines(self):  
		listoflists = []

		with open(self.file_path, "r") as file:
			for line in file:
				print(line)       
				listoflists.append(line.strip().split(","))
			return listoflists
		
reader = CsvReader("./data/datei.csv")
print(reader.lines())


# 5) Aufgabe 1: Modelliere einen Würfel
# Erstelle eine Klasse Cube, mit der du einen Würfel modellierst! 
# Die Würfel-Klasse soll als Eigenschaft die Länge einer Würfel-Seite besitzen. 
# Darüber hinaus soll die Klasse auch zwei Methoden haben: die Methode volume() 
# berechnet das Volumen und gibt es aus, die Methode surface() berechnet die 
# Oberfläche und gibt sie aus.

# Tastenkombi für Hochzahl: 5**2 = 5² (AltGr + Zahl oder Str + Alt + Zahl)

class Cube():
	def __init__(self, side):
		self.side = side
		
	def volume(self):
		print(self.side * self.side * self.side)
	
	def surface(self):
		print(self.side * self.side * 6)

a = Cube(3)
	
a.surface()
a.volume()

# Oder

class Cube():
	
	def __init__(self, side):
		self.side = side
		
	def surface(self):
		print(self.side ** 2 * 6)
		
	def volume(self):
		print(self.side ** 3)
		

# danach erzeugen wir eine Instanz deiner Cube-Klasse 
a = Cube(3)

# und testen die Methoden
a.surface()
a.volume()

# Cuboid
class Cuboid():
	def __init__(self, width, height, length):
		self.width = width
		self.height = height
		self.length = length

	def volume(self):
		print(self.width * self.height * self.length)

	def surface(self):
		print(self.width * self.height * 2 + self.length * self.height * 4)

a = Cuboid(3, 3, 5)
	
a.surface()
a.volume()

# 6) Modelliere eine Kugel
# Die Kugel-Klasse soll als Eigenschaft den Radius übergeben bekommen. 
# Zudem soll sie - ähnlich wie der Würfel - zwei Methoden haben: 
# `surface()` um den Oberflächeninhalt zu berechnen, `volume()` um das Volumen zu berechnen.

# Damit du diese Berechnungen durchführen kannst, benötigst du die Kreiszahl Pi. 
# Diese steht dir nach einem `import math` unter `math.pi` zur Verfügung 
# (was der `import` - Befehl genau macht, schauen wir uns noch später im Kurs an).
# Die Formeln für den Oberflächeninhalt / das Volumen einer Kugel darfst du im Internet nachgucken.
import math
print(math.pi)

import math

class Ball():
	def __init__(self, radius):
		self.radius = radius
		
	def surface(self):
		print(self.radius * self.radius * math.pi * 4)
		
	def volume(self):
		print(self.radius * self.radius * self.radius * math.pi * (4/3))


b = Ball(4)
b.surface()
b.volume()

# Oder
import math

class Ball():
	
	def __init__(self, radius):
		self.radius = radius
		
	def surface(self):
		print(4 * math.pi * self.radius ** 2)
		
	def volume(self):
		print(4 / 3 * math.pi * self.radius ** 3)
		
		
b = Ball(4)

# und testen die Methoden
b.surface()
b.volume()

# 7) Modelliere ein Konto
# a.) Erstelle die Konto-Klasse Account mit der Eigenschaft Kontostand credits!
# Diese Eigenschaft wird mit einem Startkapital initialisiert. 
# Die Methode display() soll den aktuellen Kontostand ausgeben.
class Account():
	def __init__(self, credits):
		self.balance = credits
	
	def display(self):
		print(self.balance)
		
Kunde111 = Account(500)
Kunde111.display()#

# Oder

class Account():
	
	def __init__(self, start):
		self.credits = start
		
	def display(self):
		print(self.credits)
		
Kunde111 = Account(500)
Kunde111.display()

# b) Ergänze die Klasse *Account* um zwei Methoden (`pay_in()` zum Einzahlen, 
# `withdraw()` zum Abheben), so dass du Geldbeträge einzahlen und abbuchen kannst, 
# und der Kontostand entsprechend angepasst wird.

# Du sollst nur Geld abheben können, so lange auch Geld auf dem Konto 
# ist. Ein Dispo-Kredit wird nicht gewährt. In dem Fall soll eine 
# Fehlermeldung ausgegeben werden, in der steht, wieviel Geld maximal 
# abgebucht werden kann.
class Account():

	def __init__(self, credits):
		self.balance = credits
	
	def display(self):
		print(self.balance)
		
	def pay_in(self, amount):
		self.balance = self.balance + amount
		
	def withdraw(self, amount):
		if self.balance - amount >= 0:
			self.balance = self.balance - amount
						# Kurzversion self.balance -= amount
		else:
			print("Du kannst nur noch " + str(self.balance) + "€ abheben!")
		
		
Kunde111 = Account(500)
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25)
Kunde111.display()
Kunde111.withdraw(600)

# Oder
class Account():
	
	# Ergänze hier deinen Code. Du darfst den Code aus a) 
	# natürlich hierhin übernehmen.
	
	def __init__(self, start):
		self.credits = start
		
	def display(self):
		print(self.credits)
		
	def pay_in(self, money):
		self.credits += money 
				# ist die Kurzversion für self.credits = self.credits + money
		
	def withdraw(self, money):
		if self.credits >= money:
			self.credits -= money
		else:
			print("Du kannst nur noch " + str(self.credits) + "€ abheben!")
		
Kunde111 = Account(500)
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25)
Kunde111.display()
Kunde111.withdraw(600)

#c.) Bislang ist das Konto noch ungeschützt - wir brauchen eine PIN! 
# Ergänze in der Klasse die Eigenschaft *pin*! So wie mit dem Startkapital 
# soll das Konto auch mit einer PIN initialisiert werden.

# Von nun an muss man beim Geldabheben nicht nur den Betrag, sondern 
# auch die PIN angeben: Nur wenn die PIN mit der des Kontos übereinstimmt,
# kann auch Geld abgebucht werden, ansonsten kommt es zu einer 
# Fehlermeldung!
class Account():
	# Ergänze hier deinen Code. Du darfst den Code aus b) 
	# natürlich hierhin übernehmen.
	
	def __init__(self, start, pin):
		self.credits = start
		self.pin = pin
		
	def display(self):
		print(self.credits)
		
	def pay_in(self, money):
		self.credits += money
		
	def withdraw(self, money, pin):
		if pin == self.pin:
			if self.credits > money:
				self.credits -= money
			else:
				print("Du kannst nur " + str(self.credits) + "€ abheben!")
		else:
			print("Falsche PIN! Konto gesperrt! Du bist verhaftet! Hände hoch!")
		
Kunde111 = Account(500, "1234")
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25, "1234")
Kunde111.display()
Kunde111.withdraw(600, "12345")

# Oder
class Account():
	
	def __init__(self, credits, real_pin):
		self.balance = credits
		self.real_pin = real_pin
		self.wrong_pin = "Falscher Pin"
	
	def display(self):
		print(self.balance)
		
	def pay_in(self, amount, try_pin):
		if self.real_pin == try_pin:
			self.balance = self.balance + amount
		else:
			print(self.wrong_pin)
		
	def withdraw(self, amount, try_pin):
		if self.real_pin == try_pin:
			if self.balance - amount > 0:
				self.balance = self.balance - amount
			else:
				print("Du kannst nur noch " + str(self.balance) + "€ abheben!")
		else:
			print(self.wrong_pin)
		
		
Kunde111 = Account(500, "1234")
Kunde111.display()
Kunde111.pay_in(40, "1234")
Kunde111.display()
Kunde111.pay_in(40, "234")
Kunde111.display()
Kunde111.withdraw(25, "3234")
Kunde111.display()
Kunde111.withdraw(600, "12345")
Kunde111.withdraw(25, "1234")
Kunde111.display()

# 8) Modelliere einen Zug
# a.) Jetzt wirst du Zugobjekte bauen! Erstelle die Klasse Train, 
# die mit den Eigenschaften route und position initialisiert wird! Bei route handelt es 
# sich um eine Liste mit den Haltebahnhöfen des Zuges. position 
# steht für den Index des Bahnhofs aus der Liste, an dem sich der Zug 
# gerade befindet bzw. von dem er zuletzt abgefahren ist (wo genau sich 
# der Zug auf der Strecke zwischen zwei Bahnhöfen befindet, interessiert 
# uns hier nicht). Mit der Methode show_station() soll der Name dieses Bahnhofs ausgegeben werden.
class Train():
	
	def __init__(self, route, start):
		self.route = route
		self.position = start
		
	def show_station(self):
		print(self.route[self.position])
	

orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()

# Erweitertes Beispiel
class Train():
		def __init__(self, route, position):
			self.stations = route
			self.position = position
			
		def show_station(self):
			print(self.stations[self.position])
		
orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.show_station()

transsib = Train(["Moskau", "Irkutsk", "Baikalsee"], 2)
transsib.show_station()

# b.) Bisher sitzt ein Zug der Klasse Train noch in seinem Startbahnhof fest. 
# Ergänze nun zwei Methoden move() und move_back(),  mit denen man einen Zug 
# auf seiner Route zur nächsten bzw. zur vorherigen Station bewegen kann, 
# sofern es diese Station auf der Route gibt. Der Zug darf seine Route nicht verlassen!
class Train():
	
	# Ergänze hier deinen Code. Du darfst natürlich deinen Code aus
	# Teilaufgabe a) hierhin übernehmen.
	
	def __init__(self, route, start):
		self.route = route
		self.position = start
		
	def show_station(self):
		print(self.route[self.position])
		
	def move(self):
			#len(self.route) - 1 ist der letzte gültige Index einer Liste. 
			#Liste ist n Elemente lang und hat die Indizes 0 bis n-1.
		if self.position < len(self.route) - 1:   
			self.position += 1
		else:
			print("Endstation! Alle aussteigen!")
	
	def move_back(self):
		if self.position > 0:
			self.position -= 1
			
orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.show_station()
orientexpress.move()
orientexpress.move_back()
orientexpress.show_station()

# Erweitertes Beispiel
class Train():

	def __init__(self, route, position):
		self.stations = route
		self.position = position

	def show_station(self):
		print(self.stations[self.position])
		
	def move(self):
		if self.position == len(self.stations) - 1:
			print("Endstation! Alle aussteigen!")
		else:
			self.position = self.position + 1
			self.show_station()
	   
	def move_back(self):
		if self.position > 0:
			self.position = self.position - 1
		
			self.show_station()
		
orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.show_station()
orientexpress.move()
orientexpress.move()
orientexpress.move()
orientexpress.move()
orientexpress.move_back()
orientexpress.move_back()
orientexpress.move_back()
orientexpress.move_back()
orientexpress.move_back()

# c.) Die Route soll nachträglich bearbeitet werden können, 
# indem man mit einer Methode `bypass_station()` einen anzugebenden 
# Haltebahnhof von der Route entfernt. Der Zug soll dann sicherheitshalber 
# an den Start der Route versetzt werden, sofern er sich nicht schon dort befindet.
class Train():
	
	# Ergänze hier deinen Code. Du darfst natürlich deinen Code aus
	# Teilaufgabe b) hierhin übernehmen.
	
	def __init__(self, route, start):
		self.route = route
		self.position = start
		
	def show_station(self):
		print(self.route[self.position])
		
	def move(self):
		if self.position < len(self.route) - 1:
			self.position += 1
		else:
			print("Endstation! Alle aussteigen!")
		
	def move_back(self):
		if self.position > 0:
			self.position -= 1
			
	def bypass_station(self, station):
		if station in self.route:
			self.route.remove(station)
			self.position = 0
			
orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.bypass_station("Budapest")
orientexpress.move()
orientexpress.show_station()

# Erweitertes Beispiel
class Train():
	
	def __init__(self, route, position):
		self.stations = route
		self.position = position

	def show_station(self):
		print(self.stations[self.position])

	def move(self):
		if self.position == len(self.stations) - 1:
			print("Endstation! Alle aussteigen!")
		else:
			self.position = self.position + 1
			self.show_station()

	def move_back(self):
		if self.position > 0:
			self.position = self.position - 1
			self.show_station()

	def bypass_station(self, bypass_station):
		if bypass_station in self.stations:
			self.stations.remove(bypass_station)
			self.position = 0
			self.show_station()

orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.bypass_station("Budapest")
orientexpress.move()
