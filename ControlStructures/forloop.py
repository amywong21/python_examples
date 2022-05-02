# Range beinhaltet immer die Startzahl und nie die Endzahl
#  Iteration über Liste ganzer Zahlen:
def example_for_loop():
	print("Example for i in range(0,10): ") 
	for i in range(0,10):
		print(i)
	
	# Iteration über Schlüssel eines Dictionaries
	print("Example iteration with key of dictionary:")
	d = dict((('alter',10),('geschlecht','m'),('wohnort', 'stuttgart')))
	for x in d:
		print((x),":  ",d[x])
	
	# range(0,10) konstruiert eine Liste, 
	# wenn ich die eckige Klammer verwende. 
	print("Example temporary list: ")
	print(range(3, 10)[5])
	
	# Echte Liste:
	print("Example real list:")
	list = (5, 8, 10)
	for i in list:
		print(i)
	
	# Mit Schlüsselwort continue kann man einen Eintrag 
	# in einer Schleife überspringen. 
	# Wenn i == 3 dann spring zur nächsten Schleifenwiederholung.
	print("Example for loop with continue: ")
	for i in range(0, 10):
		if i == 3:
			# continue springt zur nächsten
			# Schleifenwiederholung
			continue
		print(i)
	
	# Mit Schlüsselwort break wird die Schleife bei einem Eintrag abgebrochen.
	# Wenn i == 3 brich die Schleife ab und führe diese nicht aus.
	print("Example for loop with break: ")
	for i in range(0, 10):
		if i == 3:
			break
		print(i)
	
	# nach dem break sprint das program zur nächsten 
	# Zeile nach der Schleife. Hier hin:
	print("Schleife zuende")
	
	# Ob Summe der Liste größer als 10 ist. 
	liste = [4, 6, 7, 2, 4, 6, 7]
	
	s = 0
	# Für jedes Element aus meiner Liste
	for element in liste:
		# Addiere s und element und
		# speichere Ergebnis wiederum in s
		s = s + element
	
	print(s)
	
	# Wenn ich es aufsummiere und es ist größer als 10, dann Schleife abbrechen.
	liste = [4, 6, 7, 2, 4, 6, 7]
	
	s = 0 
	for element in liste:
		s = s + element
		if s > 10:
			break
		
	print(s)