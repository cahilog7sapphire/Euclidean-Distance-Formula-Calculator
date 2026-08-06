import math
## This part of the program asks you for the coordinates for the calculator.
x1 = float(input("Enter what would be the x1:"))
y1 = float(input("Enter what would be the y1:"))
x2 = float(input("Enter what would be the x2:"))
y2 = float(input("Enter what would be the y2:"))
## math.pow is used to square the difference of the two coordinates.
x_distance_squared = math.pow(x2 - x1, 2)
y_distance_squared = math.pow(y2- y1, 2)
## math.sqrt is the square of the sum of the x and y distance.
distance_answer = math.sqrt(x_distance_squared + y_distance_squared)
## the output will be rounded off by 2 decimal places.
print(f"The answer is {round(distance_answer, 2)}.")


"""
A library is a lot more efficient than typing the actual formulas, it makes everything
a lot more simple and acessible to type. They help you save time,
avoid writing code from scratch, and add complex features easily.
"""

""" 
