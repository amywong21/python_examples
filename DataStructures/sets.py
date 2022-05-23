# Python set is like a dictionary, an unordered collection of keys, held without any values.
# The set type is mutable, the contents can be changed using methods like  add() and remove().
# Sets do not contain duplicates, every element in a Python set can have only one occurrence 
# in that particular set, no multiple occurrences are allowed.

def examples_sets():
	set_num = set("Hello World!")
	print(set_num)

	# Create a set from tuple
	set_directions = set(('East','West','North','South'))
	print(set_directions)

	# Create a set from list
	set_directions = set(['East','West','North','South'])
	print(set_directions)

	# Add elements to set with add()
	set_colors = set({'Red','Blue','Green'})
	print(set_colors)
	set_colors.add('White')
	print(set_colors)

	#Remove elements from set.
	set_colors = set({'Red','Blue','Green'})
	print(set_colors)
	set_colors.remove('Blue')
	print(set_colors)

	#Set Length
	set_colors = set({'Red','Blue','Green'})
	print(len(set_colors))

	# Union of sets
	x = set({1,2,3,4,5})
	y = set({3,4,5,6,7})
	z = x.union(y)
	print(z)

	# Intersection of two sets x and y is another set of elements 
	# those are present in both sets x and y (common to both of them).
	# Using & operator
	x = set({1,2,3,4,5})
	y = set({3,4,5,6,7})
	z = x & y
	print(z)

	# Using intersection()
	x = set({1,2,3,4,5})
	y = set({3,4,5,6,7})
	z = x.intersection(y)
	print(z)

	# Difference of sets
	# Using - operator
	x = set({1,2,3,4,5})
	y = set({3,4,5,6,7})
	z = x-y
	print(z)

	# Using difference()
	x = set({1,2,3,4,5})
	y = set({3,4,5,6,7})
	z = x.difference(y)
	print(z)

	# Symmetric Difference of Sets
	# Symmetric difference of the sets is the set of elements those 
	# are not common to both the sets. The symmetric_difference() method using.
	x = set({1,2,3,4,5})
	y = set({3,4,5,6,7})
	z = x.symmetric_difference(y)
	print(z)
