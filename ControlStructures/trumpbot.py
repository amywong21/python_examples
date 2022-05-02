# Wir können in Python mit der randint()Funktion zufällige Zahlen generieren. 
# Doch um auf diese Funktion zurückzugreifen, müssen wir erst das random-Modul einbinden.
# randint liefert zufällig Ganzzahlen aus einem Intervall, das wir der Funktion mitteilen müssen. 
# Die beiden Grenzen und alle ganzen Zahlen innerhalb des Intervalls können dabei Werte von randint sein.

def example_randint():
	import random
	print(random.randint(0, 4))
	
	# Listen mit den Begriffen für unsere Tweets anlegen.
	part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
	part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
	part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
	part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]
	
	# Wir können auch Listen von Listen erstellen!
	best_words = [part1, part2, part3, part4]
	print(best_words)
	print(best_words[0])
	
	# Zieh mir eine Zufallszahl r zwischen 0 und 6. Jedes Mal wenn es ausführe kommt dann immer ein anderer Tweet raus.  
	for part in best_words:
		r = random.randint(0, len(part) - 1)
		print(part[r])
	
	sentence = []
	for part in best_words:
		# Weil der erste gültige Index der Liste bei 0 liegt, 
		# ist der letze gültige Index der Liste len(part) - 1
		# 0, 1, 2, ...., len(part)-1 : Insgesamt len(part) viele Elemente
		i = random.randint(0, len(part) - 1) 
		sentence.append(part[i])
	
	print(" ".join(sentence) + "!")