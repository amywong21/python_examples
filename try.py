
import os

print(__file__)
print(os.path.dirname(__file__))

path = os.path.join(os.path.dirname(__file__), "data", "names")

print(os.listdir(path))

files = os.listdir(path)

count = 0

for file in files:
	with open(os.path.join(path, file), "r", encoding="utf-8") as file:
		for line in file:
			names = line.split(" ")
			if names[0] == "Max":
				count = count + 1
				print(str(file) + ": " + line)

print(count)
