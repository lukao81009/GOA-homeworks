#              0     1    2    3    4
# products = ['text', 30, True, 11.5, [10, 23, 'Hello', False]]


# =================================================================


# basic way to add value in list

# products += ['new value']

# print(products)


# =================================================================

# change value in list

# products[0] = 'Sting'

# print(products)


# =================================================================


# display individual value from list
  
# print(products[4][3])


# =================================================================


# List Functions

# len() - returns the numbers of elements in the list

# len = leight - სიგრძე


# nums = [20, 13, 23, 56, 67, 99]

# print(len(nums))


# =================================================================
# append() - adds an element to the end of the list

# dataa =[10, False, '2000', 'x']

# dataa.append(True)

# print(dataa)


# =================================================================

# insert() - adds an element at the specified index (in the list)


# words = ['python', 'fun']

# words.insert(1, 'is')

# print(words)



# =================================================================

# extend() - adds multiple elements to the end of the list

# dataa = [1]

# dataa.extend([50, 'hello], 100])

# print(dataa)



# =================================================================

# index() - finds the first occurrence of a list item and returns its index.


# letters = ['a', 'b', 'c', 'd', 'e', 'f']

# print(letters.index('e'))
# print(letters.index('f'))

#         0        1       2         3
# name = ['Dato', 'Noka', 'Giorgi', 'Luka']

# y = name.index('Giorgi')
# print(y)

# =================================================================

# strr = ['name', 'last_name', 'age']
# print(max(strr))

# max() - output the maximum value
# min() - output the minimum value

# nums = [12, 24, 48, 64, 90]

# print(max(nums))
# print(min(nums))


# =================================================================

# count()- Returns a count of how many times an item occurs in the list

# nums = [10, 20, 23, 10, 23]

# print(nums.count(10)) 


# =================================================================


# list.remove()- Removes an item from the list


# nums = [10, 20, 23, 10, 23]

# nums.remove(10)
# print(nums)



# =================================================================

# list.reversed()- Removes all items from the list

# nums = [10, 20, 23, 23]

# nums.reverse()

# print(nums)

