#!/usr/bin/env python3

# Accept input for the numerical grade as a float
num_grade = float(input("Please input the numerical grade. Press enter when done. "))

# if logic to comparing the numerical score and returning the corresponding letter grade
if num_grade >= 90:
     print("Congratulations over achiever! You got an A!")
elif num_grade >= 80:
    print("Good job! You got a B!")
elif num_grade >= 70:
    print("Mediocre. You got a C!")
else:
    print("FAIL! Better luck next time.")

