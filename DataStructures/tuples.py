# A Tuple is a collection of immutable Python objects separated by commas. 
# Tuples are just like lists, but we cannot change the elements of a tuple once 
# it is assigned whereas in a list, elements can be changed. 
# The main difference being that tuple manipulation are faster than list because tuples are immutable. 
# Since they're immutable, they can be used as keys for a dictionary. Also, Tuples are used whenever 
# you want to return multiple results from a function.
def examples_tuples():
	# Create empty tuple
	a_tuple = () 
	print(a_tuple)

	# Tuple with values
	a_tuple = ('East','West','North','South')
	print(a_tuple)

	# Tuple with mixed datatypes
	a_tuple = (1, 2, 'sunday', 'monday', 3.14)
	print(a_tuple)

	# Accessing tuples
	a_tuple = (1,2,'sunday','monday',3.14)
	print(a_tuple[0])   # print 1st element
	print(a_tuple[1])   # print 2nd element
	print(a_tuple[-1])  # print last element
	print(a_tuple[-2])  # print 2nd last element

	# Loops and tuple
	a_tuple = ('East','West','North','South')
	for direction in a_tuple:
		print (direction)

	# Print with index number
	a_tuple = ('East','West','North','South')
	for i, direction in enumerate(a_tuple):
		print (i, " ", direction)

	# Concatenation of tuples
	a_tuple = ('East','West','North','South')
	b_tuple = (1,2,3,4,5)
	c_tuple = a_tuple + b_tuple
	print(c_tuple)

	# Tuple length
	a_tuple = ('East','West','North','South')
	i = len(a_tuple)
	print(i)

	# Slicing Python tuples based on start and stop
	a_tuple = ('East','West','North','South')
	slc = a_tuple[1:3]
	print(slc)
	# ('West', 'North')

	a_tuple = ('East','West','North','South')
	slc = a_tuple[:2] # slice first two elements
	print(slc)

	a_tuple = ('East','West','North','South')
	slc = a_tuple[2:]  # slice from 3rd element, Python starts its index at 0 rather than 1.
	print(slc)

	# Delete tuple elements
	# Tuples in Python are immutable. This means that once you have created a tuple, 
	# you can't change the elements contained within it. 
	# To explicitly remove an entire tuple, just use the del statement.
	a_tuple = ('East','West','North','South')
	del a_tuple
	# throws an UnboundLocalError, since a_tuple has been deleted
	#print(a_tuple)

	# Updating tuples
	# Since tuples are immutable, it cannot be changed once it has been assigned. 
	# But, if the element is itself a mutable datatype like list, its nested items can be changed.
	a_tuple = (1,2,3,4,[5,6])
	a_tuple[4][1]=12
	print(a_tuple)
	# (1, 2, 3, 4, [5, 12])

	# Tuples as return multiple values
	# Functions are always only return a single value, but by making that value a tuple,
	# we can effectively group together as many values as we like, and return them together.
	def multi():
		a=100
		b=200
		return (a,b)
	x,y = multi()
	print(x)
	print(y)

	# Nesting of tuples
	a_tuple = (1,2,3,4,5)
	b_tuple = ('a','b','c','d','3')
	c_tuple = (a_tuple,b_tuple)
	print(c_tuple)

	# Converting list to a tuple
	a_list = [1,2,3,4,5]
	a_tuple = tuple(a_list)
	print(a_tuple)

	# Repetition in tuples using * operator
	a_tuple = ('halo','world')
	a_tuple = a_tuple * 2
	print(a_tuple)

	# Tuple repetition Count
	a_tuple = ('h','e','l','l','o')
	cnt=a_tuple.count('l')
	print(cnt)

	# zip() function
	a_tuple = (1,2,3,4,5)
	b_tuple = ('a','b','c','d','e')
	for num, alp in zip(a_tuple,b_tuple):
		print(num, alp)
	
	# Tuple return min(), max() 
	a_tuple = (1,2,3,4,5)
	print(min(a_tuple))
	print(max(a_tuple))
