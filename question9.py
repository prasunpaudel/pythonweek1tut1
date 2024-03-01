'''
Write a program that asks the user to enter two numbers a and b. Then
write code to swap the values of a and b, and print them out.
'''

# Get the first number from the user
a = int(input("Enter the first number: "))
# Get the second number from the user
b = int(input("Enter the second number: "))


# Print the data type of the first number
print("the data type of a is: " + str(type(a)))
# Print the data type of the second number
print("the data type of b is: " + str(type(b)))


# Print the value of a and b before swapping
print("The value of a before swapping is: " + str(a))
print("The value of b before swapping is: " + str(b))


# Swap the values of a and b
# temp = a
# a = b
# b = temp
# or
a, b = b, a


# Print the value of a and b after swapping
print("The value of a after swapping is: " + str(a))
print("The value of b after swapping is: " + str(b))