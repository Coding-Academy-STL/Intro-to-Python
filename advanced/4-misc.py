'''
INTRO TO
    ______  __________  ______  _   __
   / __ \ \/ /_  __/ / / / __ \/ | / /
  / /_/ /\  / / / / /_/ / / / /  |/ / 
 / ____/ / / / / / __  / /_/ / /|  /  
/_/     /_/ /_/ /_/ /_/\____/_/ |_/   
                                      
MISCELLANEOUS

TODO
'''

# Make sure you use activites 15-18
# itertools combinations/permutations, base conversion
# https://codingbat.com/python

from itertools import product

print(list(product('ab',range(3))))

print(int("3A", 16))

# file I/O



# Some bonus data types (https://www.w3schools.com/python/python_datatypes.asp):
complex1 = 1j
list1 = ["apple", "banana", "cherry"]
tuple1 = ("apple", "banana", "cherry")
set1 = {"apple", "banana", "cherry"}
range1 = range(6)
dict1 = {"name" : "John", "age" : 36}
bytes1 = b"Hello"
bytearray1 = bytearray(5)


print(type(complex1))
print(type(list1))
print(type(set1))
print(type(range1))
print(type(dict1))
print(type(bytes1))
print(type(bytearray1))

print(type(type(123)))
print(type(print))
print(type(None))


Practice
---
Practice finding the answers online

1. sort a list (search: 'python sort list')
2. get all unique elements of a list (search: 'python get unique elements of list')
3. convert base 16 string to base 10 (search: 'python convert base 16 to base 10')
4. convert string of numbers to list of integers (search: 'python string of integers to list of integers')


list1 = [4, -4, 3, 3, 6, 3, 6]

# Expected output 1: [-4, 3, 3, 3, 4, 6, 6]

# Expected output 2: {3, 4, -4, 6}

# Expected output 3: 145984783
base16 = "8B38D0F"


# Expected output 4: [58, 2, -31, 0, 2]
str1 = "58 2 -31 0 2"
