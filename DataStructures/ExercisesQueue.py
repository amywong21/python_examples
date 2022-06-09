# Ermittle den 5.-häufigsten Vornamen, der in den USA vergeben wurde. 
# Lese dazu die ../data/names.csv - Datei ein. Verwende dazu zuerst 
# ein Dictionary, mit dem du die Häufigkeit der vornamen zählst, und 
# anschließend eine PriorityQueue verwendest, um die Top 5 Vornamen zu ermitteln.

# Die Namen können in der Datei mehrfach vorkommen mit unterschiedliche Counts. 
# Wahrscheinlich die Zählung der Namen aus den einzelnen Städten.
import csv

names = {}

with open('../data/names.csv', newline='') as csvfile:
	namereader = csv.reader(csvfile, delimiter=',', quotechar='"')
	counter = 0
	for line in namereader:
		if counter != 0:
			number = int(line[5])
			name = line[1]
			
			if name in names:
				names[name] = names[name] + number
			else:
				names[name] = number
		counter = counter + 1

import queue

pq = queue.PriorityQueue()

for name, number in names.items():
	pq.put((-number, name))
	
for i in range(0, 50):
	print(pq.get())
  
  
# Alternative Lösung
import csv
import queue

nameDictionary = {}

with open('../data/names.csv', newline='') as file:
	namereader = csv.reader(file, delimiter=',', quotechar='"')
	counter = 0
	
	for row in namereader:
		if counter == 0:
			counter = counter + 1
		else:
			#print(row)
			name = row[1]
			count = int(row[5])

			#print("looping:", name, " ", count)
			if name in nameDictionary:
				nameDictionary[name] = nameDictionary[name] + count
			else:
				nameDictionary[name] = count

			
pq = queue.PriorityQueue()

for name, count in nameDictionary.items():
	pq.put((-count, name))
	
for i in range(0, 50):
	print(pq.get())
 
 
# Wenn ich Spalte count nicht habe und die Vornamen zähle. 
# Zähle hier nicht vie oft der Name pro Zählung vorkam, sondern 
# zähle die Zählungen bei denen der Name min. einmal vorkam. 
import csv
import queue

nameDictionary = {}

with open('../data/names.csv', newline='') as file:
    namereader = csv.reader(file, delimiter=',', quotechar='"')
    counter = 0
    
    for row in namereader:
        if counter == 0:
            counter = counter + 1
        else:
            #print(row)
            name = row[1]

            if name in nameDictionary:
                nameDictionary[name] = nameDictionary[name] + 1
            else:
                nameDictionary[name] = 1

            
pq = queue.PriorityQueue()

for name, count in nameDictionary.items():
    pq.put((-count, name))
    
for i in range(0, 50):
    print(pq.get())