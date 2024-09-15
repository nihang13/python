'''
In python, we can take user input directly by using input() function.
This function gives a return value as string/characters hence to pass that into a variable.

Syntax:
variable = input()
But input function returns the value as string. Hence we have to typecast them whenever
required to another datatype.

variable = int(input())
variable = float(input())

We can also display a text using input function. This will make input() function take user
input and display a message as well.
'''
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
print(int(a)+int(b))
print(f"The sum is: {a+b}")