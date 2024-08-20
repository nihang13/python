'''1. Arithmetic Operators:
Perform basic mathematical operations.

i) Addition: +
a + b adds a and b.

ii) Subtraction: -
a - b subtracts b from a.

iii) Multiplication: *
a * b multiplies a and b.

iv) Division: /
a / b divides a by b (result is a float).

v) Modulus: %
a % b returns the remainder when a is divided by b.

vi) Exponentiation: **
a ** b raises a to the power of b.

vii) Floor Division: //
a // b divides a by b and returns the largest integer less than or equal to the result

2. Comparison (Relational) Operators:
Compare two values and return a boolean (True or False).

i) Equal to: ==
a == b is True if a equals b.

ii) Not equal to: !=
a != b is True if a does not equal b.

iii) Greater than: >
a > b is True if a is greater than b.

iv) Less than: <
a < b is True if a is less than b.

v) Greater than or equal to:>=
a >= b is True if a is greater than or equal to b.

vi) Less than or equal to: <=
a <= b is True if a is less than or equal to b.

3. Logical Operators:
Combine boolean expressions and return True or False.

i) Logical AND: and
a and b is True if both a and b are True.

ii) Logical OR: or
a or b is True if either a or b is True.

ii) Logical NOT: not
not a is True if a is False

4. Assignment Operators:
Assign values to variables.
=: Assign
x = 5 assigns the value 5 to x.

i) Add and assign: +=
x += 3 is equivalent to x = x + 3.

ii) Subtract and assign: -=
x -= 3 is equivalent to x = x - 3.

ii) Multiply and assign*=:
x *= 3 is equivalent to x = x * 3.

iv) Divide and assign: /=
x /= 3 is equivalent to x = x / 3.

v) Modulus and assign: %=
x %= 3 is equivalent to x = x % 3.

vi) Floor divide and assign: //=
x //= 3 is equivalent to x = x // 3.

vii) Exponentiate and assign: **=
x **= 3 is equivalent to x = x ** 3.

viii) Bitwise AND and assign: &= 
x &= 3 is equivalent to x = x & 3.

ix) Bitwise OR and assign: |= 
x |= 3 is equivalent to x = x | 3.

x) Bitwise XOR and assign: ^=
x ^= 3 is equivalent to x = x ^ 3.

xi) Right shift and assign: >>=
x >>= 3 is equivalent to x = x >> 3.

xii) Left shift and assign: <<=
x <<= 3 is equivalent to x = x << 3.

6. Identity Operators:
Compare the memory locations of two objects.
is: Returns True if both variables point to the same object.
is not: Returns True if both variables do not point to the same object.

7. Membership Operators
Test if a sequence contains an element.
in: Returns True if a value is found in the sequence.
not in: Returns True if a value is not found in the sequence

8. Ternary Operator: 
Also known as the conditional expression, it allows you to return a value based on a condition.
<expression1> if <condition> else <expression2>
Returns expression1 if condition is True, otherwise returns `expression

'''
a=2
b=3

# Arithmetic Operators:
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a%b)#Modulus
print(a**b) #Exponentiation
print(a//b)#Floor Division

# Comparison (Relational) Operators:
print(a==b) #Equal to
print(a!=b) #Not equal to
print(a>b) #Greater than
print(a<b) #Less than
print(a>=b) #Greater than or equal to
print(a<=b) #Less than or equal to

# Logical Operators:
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Assignment Operators:
c = 60  # 60 = 0011 1100 in binary
d = 13  # 13 = 0000 1101 in binary
print(c & d)  # 12 (0000 1100)
print(c | d)  # 61 (0011 1101)
print(c ^ d)  # 49 (0011 0001)
print(~c)     # -61 (inverts all bits)
print(c << 2) # 240 (1111 0000)
print(c>> 2) # 15 (0000 1111)

# Identity Operators:
d = [1, 2, 3]
e = d
f = [1, 2, 3]
print(d is e)  # memory location tracker    # True
print(d is f)  # exact value/ equilateral operator   # False
print(d is not f)  # True

# Membership Operators:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)       # True
print("grape" not in fruits)    # True

