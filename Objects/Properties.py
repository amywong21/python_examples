def example_private_properties():
	# Private dictionary erstellen. Äußerer Code arbeitet nur mit den Methoden.
	class Phonebook():

		def __init__(self):
			self.__entries = {}

		def add(self, name, phone_number):
			self.__entries[name] = phone_number

		def get(self, name):
			if name in self.__entries:
				return self.__entries[name]
			else:
				return None

	book = Phonebook()
	book.add("Mustermann", "+4912345678")
	book.add("Müller", "+49123456789")

	print(book.get("Mustermann2"))
	print(book.get("Müller"))
	
	# Aktuelles Semester vom Studenten darf nicht größer als 9 sein. 
	# Kann aber immer noch die Eingenschaft von außen überschreiten. 
	# Damit verletze ich diese Bedingung.
	class Student():
		def __init__(self, firstname, lastname):
			self.firstname = firstname
			self.lastname = lastname
			# variablen mit _ am Anfang sind ein Hinweis,
			# dass diese Variable nicht von außen geändert werden soll
			# nicht benutzen, lieber richtig privat machen
			self._term = 1

		def increase_term(self):
			if self._term >= 9:
				return	
			self._term = self._term + 1

		def name(self):
			print(self.firstname + " " + self.lastname + " (Semester: " + str(self._term) + ")")

	erik = Student("Erik", "Mustermann")
	erik.increase_term()
	erik._term = 100
	erik.name()

	# Eine andere Möglichkeit wäre, dass ich dieser Eigenschaft zwei Unterstriche gebe __. 
	# Zwei Unterstriche bedeutet, dass diese Eigenschaft eine private Eigenschaft ist 
	# und ich von außen nicht zugreifen darf.
	class Student():

		def __init__(self, firstname, lastname):
			self.firstname = firstname
			self.lastname = lastname
			# Variable ist richtig privat
			# Am besten alle Daten einer Klasse privat machen
			self.__term = 1

		def increase_term(self):
			if self.__term >= 9:
				return	
			self.__term = self.__term + 1

		def name(self):
			print(self.firstname + " " + self.lastname + " (Semester: " + str(self.__term) + ")")

	erik = Student("Erik", "Mustermann")
	erik.increase_term()
	# Leider keine Fehlermeldung
	# Aber zumindest werden keine internen Daten modifiziert
	erik.__term = 100
	erik.name()

	# Und lässt sich nicht auslesen. 
	class Student():

		def __init__(self, firstname, lastname):
			self.firstname = firstname
			self.lastname = lastname
			self.__term = 1

		def increase_term(self):
			if self.__term >= 9:
				return	
			self.__term = self.__term + 1

		def name(self):
			print(self.firstname + " " + self.lastname + " (Semester: " + str(self.__term) + ")")

	erik = Student("Erik", "Mustermann")
	erik.increase_term()

	# Gut: Richtige Fehlermeldung
	#print(erik.__term)

	erik.name()

	# Wenn ich das Semester auslesen möchte.
	class Student():

		def __init__(self, firstname, lastname):
			self.firstname = firstname
			self.lastname = lastname
			self.__term = 1

		def increase_term(self):
			if self.__term >= 9:
				return	
			self.__term = self.__term + 1

		def get_term(self):
			return self.__term

		def name(self):
			print(self.firstname + " " + self.lastname + " (Semester: " + str(self.__term) + ")")

	erik = Student("Erik", "Mustermann")
	erik.increase_term()

	print(erik.get_term())

	erik.name()

	# Bin nicht nur in der Lage Eigenschaften auf privat zustellen. 
	# Sondern auch Methoden. Damit sorge ich für Datenkapselung.
	class Student():

		def __init__(self, firstname, lastname):
			self.firstname = firstname
			self.lastname = lastname
			self.__term = 1

		def increase_term(self):
			if self.__term >= 9:
				return	
			self.__term = self.__term + 1

		def get_term(self):
			return self.__term

		def name(self):
			print(self.firstname + " " + self.lastname + " (Semester: " + str(self.__term) + ")")

		def __do_something(self):
			print("doSomething")

	erik = Student("Erik", "Mustermann")
	erik.increase_term()
	erik.name()

	# Ordentlicher Fehler, weil die Methode privat ist
	#erik.__do_something()

	# Wenn davor self. steht kann ich es auffrufen. 
	# Aber von außen nicht mehr.
	class Student():

		def __init__(self, firstname, lastname):
			self.firstname = firstname
			self.lastname = lastname
			self.__term = 1

			self.__do_something()

		def increase_term(self):
			if self.__term >= 9:
				return	
			self.__term = self.__term + 1

		def get_term(self):
			return self.__term

		def name(self):
			print(self.firstname + " " + self.lastname + " (Semester: " + str(self.__term) + ")")

		def __do_something(self):
			print("doSomething")

	erik = Student("Erik", "Mustermann")
	erik.increase_term()
	erik.name()
