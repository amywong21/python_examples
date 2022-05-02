def examples_lists():
	# Iterating through a list
	str = ['h','e','l','l','o']
	for i in str:
		print(i)

	# Get every other item, starting with the first.
	str = [1,2,3,4,5,6,7,8,9,10]
	print(str[::2])

	# Get every other item, starting with the second.
	str = [1,2,3,4,5,6,7,8,9,10]
	print(str[1::2])

	# Reverse items 
	str = [1,2,3,4,5,6,7,8,9,10]
	print(str[::-1])

	# The reverse() method in list reverse the elements of the list in place.
	str = ['h','e','l','l','o']
	str.reverse()
	print(str)

	# list length
	numbers = ['one','two','three','four','five']
	list_len = len(numbers)
	print(list_len)

	# List sort() method that performs an in-place sorting.
	str = ['h','e','l','l','o']
	str.sort()
	print(str)

	str = ['h','e','l','l','o']
	str.sort(reverse=True) # reverse sorting
	print(str)

	# Appending items and list inside a list
	# append() method adds its argument as a single element to the end of a list,
	# the length of the list itself will increase by one.
	numbers = ['one','two','three','four','five']
	numbers.append('six')
	print(numbers)

	num1 =[1,2,3]
	num2 = [4,5,6]
	num1.append(num2)
	print(num1)

	list1 = ['a', 'b', 'c']
	list1.append(['d', 'e'])
	print (list1)
	# ['a', 'b', 'c', ['d', 'e']]

	# Extend() method extends the list by adding all items of a list (passed as an argument) to the end.
	# extend() method iterates over its argument adding each element to the list, extending the list. 
	# The length of the list will increase by however many elements were in the iterable argument.
	list = ['a', 'b', 'c']
	list.extend(['d', 'e'])
	print (list)
	# ['a', 'b', 'c', 'd', 'e']

	# Concatenating lists using '+' operator
	num1 = [1, 2, 3]
	num2 = [4, 5, 6]
	num3 = num1 + num2
	print(num3)

	# Repeating a list using '*' operator
	num1 =['hi']
	num = num1 * 4
	print(num)

	# Inserting elements into a list
	num1 =[1,2,4]
	num1.insert(2,3) #inserts an element into the third position
	print(num1)

	num1 =[1,2,3,4,6]
	num1.insert(-1,5) #inserts an element into the second from last position of the list (negative indices start from the end of the list)
	print(num1)

	# Remove elements from list
	numbers = ['one','two','three','four','five']
	numbers.remove('three')
	print(numbers)

	# Remove duplicates from a Python List. The common approach to get a unique collection of items
	# is to use a dictionary. A Python dictionary is a mapping of unique keys to values.
	# So, converting Python list to dictionary will automatically remove any duplicates 
	# because dictionaries cannot have duplicate keys.
	numList = [1,2,3,1,4,2,5,3]
	dict1 = dict.fromkeys(numList)
	numList = dict1.keys()
	print(numList)

	# list.clear() remove all items from the list.
	numbers = ['one','two','three','four','five']
	print(numbers)
	numbers.clear()
	print(numbers)

	# List.count(x) return the number of times x appears in the list.
	str = ['h','e','l','l','o']
	cnt = str.count('l')
	print(cnt)

	# Accessing list values
	a_list = [1, 2, 3, 4]
	num1 = a_list[0]
	num2 = a_list[3]
	print(num1)
	print(num2)

	d_list = [1,2,'three','four']
	num = d_list[1]
	str = d_list[2]
	print(num)
	print(str)

	# List index() method returned the index of the first matching item.
	str = ['h','e','l','l','o']
	ind = str.index('l') # from start 'l' is in 2nd position
	print(ind)

	str = ['h','e','l','l','o']
	ind = str.index('l',3) # start searching from 3rd position
	print(ind)

	# Slice elements based on a start and stop(end but not include it).
	str = ['h','e','l','l','o']
	lsc = str[1:4]
	print(lsc)

	str = ['h','e','l','l','o']
	lsc = str[:3] # slice first three elements
	print(lsc)

	str = ['h','e','l','l','o']
	lsc = str[3:] # slice from 4th element, Python starts its lists at 0 rather than 1.
	print(lsc)

	# Test if element exists in list
	str = ['h','e','l','l','o']
	print('e' in str) 
	# True

	str = ['h','e','l','l','o']
	print('e' not in str)
	# False

	# Create new list with dynamic values
	dList = [3 ** i for i in range(5)]
	print(dList)

	# zip() function
	# To loop over two or more sequences at the same time,
	# the entries can be paired with the zip() function.
	numbers = [1,2,3,4,5]
	alpla = ['a','b','c','d','e']
	for num, alp in zip(numbers,alpla):
		print(num, alp)