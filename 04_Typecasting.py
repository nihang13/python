# TYPECASTING:
'''
The conversion of one data type into other data type is known as type casting in python.
Python supports a wide variety of functions or methods like: int(), float(), str(), ord(),
tuple(), set(), list(), dict(), etc. for the type casting in python.

Two types of typecasting:
1. Explicit Conversion (Explicit type casting in python):
The conversion of one data type into another data type, done via developer or programmer's
intervention or manually as per the requirement, is known as explicit conversion.

2. Implicit Conversion (Implicit type casting in python):
Data type in python do not have the same level i.e ordering of data types is not the same in python.
Some of the data types have higher-order, and some have lower order. While performing any operations
on variables with different data types in python, one of the variable's data types will be changed to 
the higher data type. According to the level, one ldata type is converted into other by the python
interpreter itself (sutomatically). This is called, implicit typecasting in python
Python converts a smaller data type to a higher data type to prevent data loss.
'''

# Explicit Typecating:
a="15"
b=2
print(int(a)+b) #converts a into integer
print(type(int(a)+b))

# Implicit Typecasting:
# Converts integer(d) into float to prevent data loss.
c=1.9
d=8
print(c+d)
print(type(c+d))