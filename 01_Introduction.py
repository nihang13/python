'''
Python:
Python is a high-level, interpreted language lnown for its readability and versatility.
It supports multiple programming paradigms, including procedural, obeject-oriented, and functional programming.

Features:
- Easy to understand
- Open Source
- Portable (Linux/Windows/Mac)

Comments:
In Python, a comment is a piece of text in the code that is not executed by the interpreter.
Comments are used to explain the code, make it more understandable, or leave notes for future reference.
They are essential for writing readable and maintainable code, especially when collaborating with others or revisiting your own code after some time.

Types of Comments in Python:

i)Single-line Comment:
- Begins with a # symbol.
- Everything after the # on that line is ignored by the Python interpreter

ii)Multi-line Comment:
- Python doesn't have a dedicated syntax for multi-line comments, but you can use multiple single-line comments or a multi-line string.
- Multi-line strings are created using triple quotes , but these are typically used for docstrings rather than comments.

iii)Docstrings:
- Docstrings are a type of comment used to describe a module, function, class, or method.
- They are written using triple quotes and are placed right after the definition of a function, method, class, or module.

Syntax:
Set of rules that defines the structure of valid statements and expressions in the language.
In Python, f-strings (formatted string literals) provide a concise and readable way to include expressions inside string literals, using curly braces {}
Use the "print" function to print the line "Hello, World!".
'''

print("Hello, World")
print(f"Hello, World") #using fstring
'''
Indentation:
Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported,
but the standard indentation requires standard Python code to use four spaces. For example:
'''

x = 1
if x == 1:
    # indented four spaces or tab
    print("x is 1.")
