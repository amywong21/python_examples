def example_functions():
	def multi_print():
		print("Hallo Welt!")
		print("Hallo Welt!")
	multi_print()

	def multi_print2(name):
		print(name)
		print(name)

	multi_print2("HALLO")
	multi_print2("WELT?")

# len() Funktion
def example_len_functions():
	len("Hallo") # Gibt Anzahl einer Zeichenkette aus. 
	len(["Hallo", "Welt"]) # Wie viele Elemente in einer Liste ist.

# Mehrere Parameter in einer Funktion übergeben
def example_function_parameters():
	def multi_print(name, count):
		for i in range(0, count):
			print(name)
	multi_print("Hallo!", 5)

	def multi_print(name, count):
		for i in range(0, count):
			print(name)

	def weitere_funktion():
		multi_print("Hallo!", 3)
		multi_print("Welt!", 3)
	weitere_funktion()

	def findsum(x,y):
		z = x + y
		print("Sum of numbers are: ", z)
		findsum(10,20)
		findsum(4,2)

	# Default values for parameters
	def dispStatus(name,age=25):
		print("Name is :" ,name)
		print("Age is :" ,age)
	dispStatus("John")
	dispStatus("Doe")

def example_function_as_parameter():
	def sayHello(func):
		return "Hello " + func
	def sayName(name):
		return name
	print (sayHello(sayName("John")))

def example_functions_as_variables():
	def findSum(x,y):
		return x+y
	f1 = findSum(10,20)
	print(f1)
	f1 = findSum(40,20)
	print(f1)

# Funktionen mit Rückgabewert
def example_function_with_return():
	def maximum(a, b):
		if a < b:
			return b
		else:
			return a

	result = maximum(4,5)
	print(result)

def example_inner_function():
	def calc(x,y):
		def findSum(x,y):
			return x+y
		sum = findSum(x,y)
		print("Sum of ", x, " + ", y, " is ", sum)
	calc(10,20)

# Variable list as function
def example_variable_list_as_function():
	liste = [1, 2, 3]

	liste.append(4)
	print(liste)

# String zerlegen
def example_split():
	"Hallo, Welt".split(",")


