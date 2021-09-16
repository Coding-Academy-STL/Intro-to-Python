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
