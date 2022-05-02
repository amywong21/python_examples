# Python unterstützt sowohl for- als auch while-Schleifen.

# While-loop:
def example_continue_break_loop():
	counter = 0 
	print("continue_break_loop:")
	while counter < 10:
		#print(counter)
		counter = counter + 1
		if counter == 5:
			continue
		if counter == 9:
			break
		else:
			print(counter)

# Bei while-Schleife muss man aufpassen, dass man keine Endlosschleife 
# produziert wenn ich die Schleife nicht terminiere.
# Wenn ich von Anfang an weiß wie viele Zahlen ich durchzählen muss bzw.,
# dann nicht while-Schleife verwenden sondern die for-Schleife. 
# Sonst passiert es leicht, dass man eine Endlosschleife produziert.

# Endless loop:
#counter = 0 
#while counter < 10:
	#print(counter)

# Not an endless loop:
def example_count_up_loop():
	counter = 0
	
	print("count up loop:")
	while counter < 10:
		print(counter)
		# ohne counter zu erhöhen 
		# wird es eine Endlosschleife geben
		counter = counter + 1 

def example_count_down_loop():
	counter = 10

	print("count down loop:")
	while counter > 0:
		print(counter)
		# ohne counter zu erhöhen 
		# wird es eine Endlosschleife geben
		counter = counter - 2 