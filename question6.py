'''
Write a program that asks the user to input the radius of a circle. The program
should calculate the area of the circle A = πr^2 and print it out
'''

# Get the radius from the user  
radius = float(input("Enter the radius of the circle: "))

# Print the data type of the radius
print("the data type of radius is: " + str(type(radius)))

# Print the area of the circle
print("The area of the circle is: " + str(3.14159*radius**2))