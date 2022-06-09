import queue

def example_queue(): 
	q = queue.Queue()

	q.put("Hallo")
	q.put("Welt")
	q.put("Hallo")
	q.put("Mars")
	q.put("Pluto")

	print(q.get())
	print(q.get())
 
	# Solange es in der queue noch Elemente gibt, dann mit q.get holen.
	# Da noch 3 Elemente drinnen sind, werden diese ausgegeben.
	while not q.empty():
		element = q.get()
		print(element)
 
	# Priority queue:
	# Das ist eine Warteschlange, die die Einträge für uns automatisch sortiert.
 
	# Tupel in die q.put(Dringlichkeit, "Eintrag") Funktion packen. 
 	# Je höher die Dringlichkeit desto kleiner die Zahl. 
	# Die Reihenfolge der q.put() spielt dabei keine Rolle. 
	q = queue.PriorityQueue()

	q.put((10, "Hallo Welt"))
	q.put((15, "Mars"))
	q.put((5, "Wichtig"))

	q.get()
	q.get()

 	# weiteres Beispiel:
	text = "A A A A A B B B C C C C C D D D D D D D D"
	d = {}
	for word in text.split(" "):
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1
	print(d)
 
	# Problem nur, wenn es mehr Einträge gibt, wird es unübersichtlich.
	
	# Mit PriorityQueue können wir aufsteigend sortieren lassen. 
	# Mit print(pq.get()) werden die Daten autom. wieder sortiert. 
	text = "A A A A A B B B C C C C C D D D D D D D D"
	dictio = {}
	# Erst wird text.split(" ") ausgeführt
	# Ergebnis ist eine Liste mit jedem Buchstaben als String
	# Diese Liste gehen wir dann mit einer for Schleife durch
	for letter in text.split(" "):
		if letter in dictio:
			dictio[letter] = dictio[letter] + 1
		else:
			dictio[letter] = 1
	print(dictio)

	pq = queue.PriorityQueue()
	for letter, number in dictio.items():
		pq.put((number, letter))

	print(pq.get())
	print(pq.get())
	print(pq.get())
 
	# PriorityQueue sortiert immer aufsteigend. Wenn es absteigend sortiert werden 
	# soll ein Minus Zeichen vor pq.put((-number, word)) schreiben.
	text = "A A A A A B B B C C C C C D D D D D D D D"
	dictio = {}
	# Erst wird text.split(" ") ausgeführt
	# Ergebnis ist eine Liste mit jedem Buchstaben als String
	# Diese Liste gehen wir dann mit einer for Schleife durch
	for letter in text.split(" "):
		if letter in dictio:
			dictio[letter] = dictio[letter] + 1
		else:
			dictio[letter] = 1
	print(dictio)

	pq = queue.PriorityQueue()
	for letter, number in dictio.items():
		pq.put((-number, letter))

	print(pq.get())
	print(pq.get())
	print(pq.get())
	print(pq.get())