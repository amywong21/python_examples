def examples_dictionaries():
	examples_dictionaries_01()
	examples_dictionaries_02()
	examples_dictionaries_03()
	examples_dictionaries_04()

def examples_dictionaries_01():
	# Creating an empty dict
	print("Creating an empty dict")
	directions = {}
	print(directions)

	# Contents of a dict can be written as a series of key:value pairs within braces { }
	print("Contents of a dict can be written as a series of key:value pairs within braces { }")
	directions = {}
	directions[1]="East"
	directions[2]="West"
	directions[3]="North"
	directions[4]="South"
	print(directions)
	# {1: 'East', 2: 'West', 3: 'North', 4: 'South'}

	# Accessing Values from Dictionary
	print("Accessing Values from Dictionary")
	directions = {}
	directions[1]="East"
	directions[2]="West"
	directions[3]="North"
	directions[4]="South"
	print(directions[1])
	print(directions[4])

	# Sort a dictionary by key
	print("Sort a dictionary by key")
	import operator
	x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
	sorted_x = sorted(x.items(), key=operator.itemgetter(0))
	print(sorted_x)

	# Sort a dictionary by value
	print("Sort a dictionary by value")
	import operator
	x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
	sorted_x = sorted(x.items(), key=operator.itemgetter(1))
	print(sorted_x)

	# Remove values from Dictionaries
	print("Remove values from Dictionaries")
	directions = {}
	directions[1]="East"
	directions[2]="West"
	directions[3]="North"
	directions[4]="South"
	del directions[2]
	print(directions)

	# clear() method of Dictionary remove all entries in dictionary
	print("clear() method of Dictionary remove all entries in dictionary")
	directions = {}
	directions[1]="East"
	directions[2]="West"
	directions[3]="North"
	directions[4]="South"
	directions.clear()
	print(directions)

	# Updating dict. contents
	print("Updating dict. contents")
	students = {}
	students['ID']=1001
	students['Name']="John"
	students['Age']=22
	print (students)
	students['Age'] = 23 # update age
	students['Country'] = 'USA' # add new entry
	print(students)

	# Retrieve whole Dictionary entries
	print("Retrieve whole Dictionary entries")
	directions = {}
	directions[1]="East"
	directions[2]="West"
	directions[3]="North"
	directions[4]="South"
	for key, value in directions.items():
		print(key, value)
	
	# Retrieve Keys and Values in a List
	print("Retrieve Keys and Values in a List")
	directions = {}
	directions[1]="East"
	directions[2]="West"
	directions[3]="North"
	directions[4]="South"
	keys = list(directions.keys())
	print(keys)
	vals = list(directions.values())
	print(vals)

	# Arbitrary key and value
	print("Create dictionaries from arbitrary key and value expression")
	arb_dictionary = {i: i**2 for i in (10, 20, 30)}
	print(arb_dictionary)

	# Copying a Dictionary with copy()
	print("Copying a Dictionary with copy()")
	directions = {}
	directions[1]="East"
	directions[2]="West"
	directions[3]="North"
	directions[4]="South"
	dir1 = directions.copy()
	print(dir1)

	# Merging dictionaries
	# The update() method of Dictionary is to merge the keys and values 
	# of one dictionary into another, overwriting values of the same key.
	print("Merging Dictionaries")
	dict1 = {1:'a',2:'b',3:'c'}
	dict2 = {4:'d',5:'e'}
	dict1.update(dict2)
	print(dict1)

	# To delete entire dictionary, you can use "del" command.
	print("To delete entire dictionary, you can use del command.")
	directions = {}
	directions[1]="East"
	directions[2]="West"
	directions[3]="North"
	directions[4]="South"
	del directions
	# throws an UnboundLocalError, since directions is deleted before
	#print(directions)

# Default dicts
from collections import defaultdict

def generateDefaultValue():
	print("generateDefaultValue() wurde aufgerufen!")
	return 0

def examples_dictionaries_02():
	d = defaultdict(generateDefaultValue)
	print(d)
	d["existiertNicht23432535"]
	print(d)
	d["existiertNicht23432535"] = 1
	print(d)

	d = defaultdict(generateDefaultValue)
	print(d)
	d["existiertNicht"] = d["existiertNicht"] + 5
	print(d)

def examples_dictionaries_03():
	# int() ist eine Methode die die default Ganzzahl 0 liefert
	n = int()
	print(n)

	p = defaultdict(int)
	print(p)
	words = ["Hallo", "Hallo", "Welt"]

	for word in words:
		p[word] = p[word] + 1
		print(p)

# Macht das gleiche wie examples_dictionaries_03, nur klassischer
def examples_dictionaries_04():
	# Leeres Dictionary
	p = {}
	print(p)
	words = ["Hallo", "Hallo", "Welt"]

	for word in words:
		if word in p:
			# Ohne defaultdict gibt der Zugriff p[word] einen KeyError, 
			# da es diesen Key noch nicht gibt
			p[word] = p[word] + 1
		else:
			p[word] = 1
		print(p)

#examples_dictionaries_01()
#examples_dictionaries_02()
#examples_dictionaries_03()
#examples_dictionaries_04()