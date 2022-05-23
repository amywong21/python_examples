def example_exceptions():
	# ZeroDivisionError
	x = 0
	print(5 / x)

	# FilNotFoundError
	try:
		with open("datei.xyz", "r") as file:
			print(file)
	except FileNotFoundError:
		print("Die Datei konnte nicht geöffnet werden")

	# Many exceptions
	try:
		with open("datei.xyz", "r") as file:
			print(file)
		print(5 / 0)
	except ZeroDivisionError:
		print("Du darfst nicht durch 0 teilen")
	except FileNotFoundError:
		print("FileNotFoundError ist aufgetreten")

	# Eigene exceptions 
	def do_something():
		print(5 / 0)

	try:
		do_something()
	except ZeroDivisionError:
		print("Du darfst nicht durch 0 teilen")

	
	# Weitere eigene Exceptions 
	class InvalidEmailError(Exception):
		pass

	def send_mail(email, subject, content): 
		if not "@" in email:
			raise InvalidEmailError("email does not contain an @")

	try:
		send_mail("hallo", "Betreff", "Inhalt")
	except InvalidEmailError as exception:
		print(exception)

	# The finally block, if specified, will be executed 
	# regardless if the try block raises an error or not.
	try:
		print(x)
	except:
		print("Something went wrong")
	finally:
		print("The 'try except' is finished") 