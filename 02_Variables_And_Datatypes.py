'''
VARIABLES:
A variable is the name given to a memory location in a program. For example:
a= 30 (ariables = container to store a value.) 
b= "Nihang" (keywords = reserved words in python)
c= 71.22  (identifiers = class/function/variable name)

RULES FOR CHOOSING AN IDENTIFIER
- A variable name can contain alphabets, digits, and underscores.
- A variable name can only start with an alphabet and underscores.
- A variable name cant start with a digit.
- No while space is allowed to be used inside a variable name.
Examples of a few variable names are: nihang, one8, seven, _seven etc.

DATA TYPES:
1. Numeric Types:
i) int: Represents whole numbers (positive, negative, or zero) without a fractional part.
Example: x = 10

ii) float: Represents floating-point numbers (numbers with a decimal point).
Example: y = 3.14

iii) complex: Represents complex numbers with a real and an imaginary part.
Example: z = 3 + 4j

2. Sequence Types:
i) str (String): Represents a sequence of characters enclosed in single, double, or triple quotes.
Example: name = "Alice"

ii) list: An ordered, mutable collection of items (which can be of different data types and allow duplicate).
Example: numbers = [1, 2, 3, "four"]

iii) tuple: An ordered, immutable collection of items (which can be of different data types).
(Datastructure, Immutable, ordered, allows duplicate, cannot add or remove)
Example: coordinates = (10.0, 20.0)

iv) range: Represents an immutable sequence of numbers, typically used in loops.
Example: range(5) generates numbers from 0 to 4.

3. Mapping Type:
i) dict (Dictionary): Represents a collection of key-value pairs, where each key is unique.
(dictionary=key value pair, mutable, doesnt allow duplicate)
Example: person = {"name": "Alice", "age": 30}

4. Set Types:
i) set: An unordered collection of unique items.
(data structure, mutable, doesnt allow duplicate value, unorder, sort)
Example: unique_numbers = {1, 2, 3, 3, 2} results in {1, 2, 3}

ii) frozenset: An immutable version of a set.
Example: frozen_set = frozenset([1, 2, 3])

5. Boolean Type:
i) bool: Represents one of two values: True or False.
Example: is_active = True

6. Binary Types:
i)bytes: Represents an immutable sequence of bytes.
Example: data = b'Hello'

ii) bytearray: Represents a mutable sequence of bytes.
Example: mutable_data = bytearray(5)

iii) memoryview: A memory view object allows you to access the internal data of an object that supports the buffer protocol.
Example: memory_view = memoryview(bytes(5))

7. None Type:
i) NoneType: Represents the absence of a value or a null value.
Example: result = None
'''

# Numeric Data Types:
x = 10 #integer
y = 3.14 #float
z = 3 + 4j #complex

#Sequence Data Types:
name = "Alice" #string
numbers = [1, 2, 3, "four"] #list
coordinates = (10.0, 20.0) #tuple
range(5) #range = generates numbers from 0 to 4.

#Mapping Data Type:
person = {"name": "Alice", "age": 30} #dictionary

#Set Data Types:
unique_numbers = {1, 2, 3, 3, 2} #list
frozen_set = frozenset([1, 2, 3]) #frozenset

#Boolean Data Type:
is_active = True #boolean

#Binary Data Types:
data = b'Hello' #bytes
mutable_data = bytearray(5) #bytesarray
memory_view = memoryview(bytes(5)) #memoryview
