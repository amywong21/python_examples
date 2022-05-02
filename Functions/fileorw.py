# Es gibt verschiedene Modi um Dateien zu öffnen.

# r - read
def example_read_all_lines():
	with open("data/sample.txt", "r") as f:
		for line in f:
			print(line)

def example_read_with_parameter():
	# Do not return the next line if the total number of returned bytes
	# are more than 10 when parameter is set to 10 bytes in readlines() .
	fOpen = open("data/sample.txt",'r')
	myList = fOpen.readlines(10)
	print(myList)

# The Python readlines() method takes a text file as input 
# and stores each line in the file as a separate element in a list.
def example_read_line_into_list():
	fOpen = open("data/sample.txt",'r')
	myList = fOpen.readlines()
	print(myList)
	fOpen.close()

# readlines() is not very efficient as it can result in MemoryError 
# because this function loads the entire file into memory, then iterates over it.	

def example_read_large_file():
	# The fileinput.input() call reads lines sequentially, 
	# but doesn't keep them in memory after they've been read, 
	# since file in Python is iterable.

	import fileinput
	for line in fileinput.input(['data/sample.txt']):
		print(line)
	fileinput.close()


def example_read_line_into_array():
	# Following program read the content of the file 
	# and add into an Array.
	myArray = []
	with open("data/sample.txt") as f:
		myArray = f.readlines()
	print(myArray)

	with open("data/my_file.txt", "r") as my_file:
		str = my_file.readlines()
		print(str)
	# ['This is first line\n', 'This is second line\n', 'This is third line\n', 'This is fourth line']

def example_split_lines():
# reading a text file and splitting it into single words in python
	with open("data/my_file.txt", "r") as my_file:
		for line in my_file:
			str = line.split()
			print(str)
# ['This', 'is', 'first', 'line']
# ['This', 'is', 'second', 'line']
# ['This', 'is', 'third', 'line']
# ['This', 'is', 'fourth', 'line']

# w - write
def example_write_file():
	file = open("schreiben.txt", "w")
	students = ["Max", "Monika", "Erik", "Franziska"]

	for student in students:
		file.write(student + "\n")

	file.close()

# Mehrere write Befehle ausführen.
	file = open("schreiben.txt", "w")

	file.write("asdfsdf")
	file.write("asdfsdf")

	file.close()

# a - append
# Daten werden nicht überschrieben sondern am Ende dran gehängt. 
# Mit jedem ausführen wird es dann dran gehängt.
def example_append_data():
	file = open("data/schreiben.txt", "a")
	students = ["Max", "Monika", "Erik", "Franziska"]

	for student in students:
		file.write(student + "\n")
	
	file.close()