
def example_sort_all():
	example_sort_01()
	example_sort_02()
	example_sort_03()
	example_sort_04()
	example_sort_05()
	
# Vervollständige die Funktion `shortest_word()`: Ihr sollen
# mehrere Strings übergeben werden (KEINE Liste von Strings!), von denen 
# sie den String mit den wenigsten Zeichen zurückliefert.
# Hinweis: Benutze variable Parameter (mit Sternchen `*` oder doppelten Sternche `**`)!
def shortest_word(*params):
	shortest_length = 0
	shortest_name = ""

	for name in params:
		if shortest_length == 0:
			shortest_length = len(name)
			shortest_name = name
		elif len(name) < shortest_length:
			shortest_length = len(name)
			shortest_name = name
	print(shortest_length)
	return shortest_name

def example_sort_01():	
	print(shortest_word("Max", "Moritz", "Monika", "Tim", "Jo"))


# Sortiere die Tupel in der Liste `tupels` aufsteigend nach ihrer Summe!
# Schreibe dazu zuerst eine normale Funktion und löse die Aufgabe
# anschließend nochmal mit einer lambda-Funktion.
def tupel_sum(tupel):
	return tupel[0] + tupel[1]

def example_sort_02():
	tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]
	tupels.sort(key=tupel_sum)
	print(tupels)
	tupelsum = tupel_sum(tupels[0])
	print(tupelsum)

# Sortiere die Liste `names` mit Namen nach dem Nachnamen. 
# Du kannst annehmen, dass alle Namen in der Liste nur einen Vornamen enthalten.
# Das Format der Namen ist immer "Vorname Nachname".
# Überlege dir dazu zuerst, wie du den Nachnamen ermittelst und schreibe dann die 
# entsprechende Funktion, die du der `.sort()`- Funktion übergibst.
# Schreibe dazu zuerst eine normale Funktion und löse die Aufgabe anschließend nochmal 
# mit einer lambda-Funktion.
def lastname(name):
	names = name.split(" ")
	return names[1]

def example_sort_03():
	names = ["Elif Else", "Sebastian Klarnamen", "Anna Boa", "Anton Adel", "Conny Coder", "Anne Wortmann", "Willy Cordes"]

	names.sort(key=lastname)
	print(names)

# Sortiere die Liste `sentences` absteigend nach der Anzahl der Wörter, 
# die ein Element aus `sentences` jeweils enthält. Du kannst annehmen,
# dass in den Sätzen alle Wörter ordnungsgemäß mit Leerzeichen voneinander getrennt sind. :-)
# Überlege dir dazu zuerst, wie du die Anzahl Wörter in einem Satz ermitteln kannst.
# Hinweis: Schreibe dazu zuerst eine normale Funktion und löse die Aufgabe anschließend nochmal
# mit einer lambda-Funktion.
def number_of_words(sentence):
	sentences = sentence.split(" ")
	return -len(sentences)

def example_sort_04():
	sentences = ["Sie liefen weiter den Strand entlang.", "Der Hund bellte laut.", "Er rutschte aus.", "Sie lachte."]

	sentences.sort(key=number_of_words)
	print(sentences)

# Verändere den folgenden Code so, dass die Liste l nicht mehr innerhalb 
# der Funktion make_row() überschrieben wird. 
# Die Liste, die make_row() ausgibt, soll also identisch mit der bisherigen sein. 
# l soll aber am Ende in seiner ursprünglichen Form ausgegeben werden.
def make_row(row):
	new_row = row[:]
	# oder: new_row = row.copy()
	# oder: new_row = [i for i in row]
	new_row[2] = "x"
	print(new_row)

def example_sort_05():
	l = ["o", "x", "o"]
	make_row(l)	
	print(l)