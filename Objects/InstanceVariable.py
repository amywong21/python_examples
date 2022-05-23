# difference between static and instance variable

def example_instance_variable():
	# Static variable, nicht zu empfehlen:
	class Car:
		price = "expensive"

	c = Car()
	print(c.price)

	# Lieber Instanzvariablen verwenden:
	class Car:
		def __init__(self):
			self.price = "expensive"

	c = Car()
	print(c.price)