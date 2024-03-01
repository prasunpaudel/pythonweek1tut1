'''
Write a program that asks the user to input length and breadth of a rectangle.
Then the program should calculate to area and perimeter of the rectangle and
print them out. Area = lxb; Perimeter = 2(l+b)
'''
# Get the length of the rectangle from the user
length = float(input("Enter the length of the rectangle: "))
# Get the breadth of the rectangle from the user
breadth = float(input("Enter the breadth of the rectangle: "))


# Print the data type of the length
print("the data type of length is: " + str(type(length)))
# Print the data type of the breadth
print("the data type of breadth is: " + str(type(breadth)))



# Print the area of the rectangle
print("The area of the rectangle is: " + str(length*breadth))


# Print the perimeter of the rectangle
print("The perimeter of the rectangle is: " + str(2*(length+breadth)))