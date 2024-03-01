'''
Write a program that computes the value of the algebraic expression:
x^3 + 3x^2y + 3xy^2 + y^3
The program should ask the user to input the values of x and y. Write
comments to describe your code.
'''

# Get the value of x from the user
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print("the data type of x is: " + str(type(x)))
print("the data type of y is: " + str(type(y)))

print("The value of the algebraic expression is: " + str(x**3 + 3*x**2*y + 3*x*y**2 + y**3))