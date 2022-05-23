def example_inheritance():
	class Person:
		def __init__(self, fname, lname):
			self.firstname = fname
			self.lastname = lname

		def printname(self):
			print(self.firstname, self.lastname)

	# Create a class named Student, which will inherit the properties
	# and methods from the Person class:
	class Student(Person):
		# Use the pass keyword when you do not want to add 
		# any other properties or methods to the class.
		pass 
	# Use the Student class to create an object,
	# and then execute the printname method:
	x = Student("Mike", "Olsen")
	x.printname()

	# So far we have created a child class that inherits the properties and methods from its parent.
	# We want to add the __init__() function to the child class (instead of the pass keyword).
	# The __init__() function is called automatically every time 
	# the class is being used to create a new object.

	class Person:
		def __init__(self, fname, lname):
			self.firstname = fname
			self.lastname = lname

		def printname(self):
			print(self.firstname, self.lastname)

	class Student(Person):
		def __init__(self, fname, lname):
			Person.__init__(self, fname, lname)
	
	x = Student("Mike", "Olsen")
	x.printname()

	# Now we have successfully added the __init__() function, 
	# and kept the inheritance of the parent class, 
	# and we are ready to add functionality in the __init__() function.
	# Python has a super() function that will make the child class inherit 
	# all the methods and properties from its parent:

	class Person:
		def __init__(self, fname, lname):
			self.firstname = fname
			self.lastname = lname

		def printname(self):
			print(self.firstname, self.lastname)

	class Student(Person):
		def __init__(self, fname, lname):
			super().__init__(fname, lname)

	x = Student("Mike", "Olsen")
	x.printname()

	# Add a property called graduationyear to the Student class:
	class Person:
		def __init__(self, fname, lname):
			self.firstname = fname
			self.lastname = lname

		def printname(self):
			print(self.firstname, self.lastname)

	class Student(Person):
		def __init__(self, fname, lname):
			super().__init__(fname, lname)
			self.graduationyear = 2019

	x = Student("Mike", "Olsen")
	print(x.graduationyear)
	
	# the year 2019 should be a variable, and passed into the 
	# Student class when creating student objects. 
	# To do so, add another parameter in the __init__() function:

	class Person:
		def __init__(self, fname, lname):
			self.firstname = fname
			self.lastname = lname

		def printname(self):
			print(self.firstname, self.lastname)

	class Student(Person):
		def __init__(self, fname, lname, year):
			super().__init__(fname, lname)
			self.graduationyear = year

	x = Student("Mike", "Olsen", 2019)
	print(x.graduationyear)

	# Add a method called welcome to the Student class:
	# If you add a method in the child class with the same name as a
	# function in the parent class, the inheritance of the parent method will be overridden.

	class Person:
		def __init__(self, fname, lname):
			self.firstname = fname
			self.lastname = lname

		def printname(self):
			print(self.firstname, self.lastname)

	class Student(Person):
		def __init__(self, fname, lname, year):
			super().__init__(fname, lname)
			self.graduationyear = year

		def welcome(self):
			print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

	x = Student("Mike", "Olsen", 2019)
	x.welcome()

	# Vererbung erlaubt es die Funktionen und Methoden nicht nochmal kopieren zu müssen aus class student. 
	# Sondern die Eigenschaften aus einer class zu vererben. Mit super() beziehe ich mich auf Student.
	class Student():
		def __init__(self, firstname, surname):
			self.firstname = firstname
			self.surname = surname

		def name(self):
			return self.firstname + " " + self.surname

	class WorkingStudent(Student):
		def __init__(self, firstname, surname, company):
			super().__init__(firstname, surname)
			self.company = company

		def name(self):
			return super().name() + " (" + self.company + ")"

	students = [
		WorkingStudent("Max", "Müller", "ABCDEF GmbH"),
		Student("Monika", "Mustermann"),
		Student("Erik", "Müller"),
		WorkingStudent("Franziska", "Mustermann", "XYZXYZ GmbH")
	]

	for student in students:
		print(student.name())