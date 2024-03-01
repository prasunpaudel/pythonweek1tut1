'''
Write a simple program that asks to enter two numbers and prints out their
sum and difference. Write comments to describe your code.
'''

# Get the first number from the user
num1 =int(input("Enter the first number: "))
# Get the second number from the user
num2 = int(input("Enter the second number: "))


print("the data type of num1 is: " + str(type(num1)))
print("the data type of num2 is: " + str(type(num2)))

# Print the sum of the two numbers
print("The sum of the two numbers is: " + str(num1 + num2))
# Print the difference of the two numbers
print("The difference of the two numbers is: " + str(num1 - num2))