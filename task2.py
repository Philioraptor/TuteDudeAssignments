"""
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

"""

import math

def math_calc(num):
  sqrt_n = math.sqrt(num)
  log_n = math.log(num)
  sin_n = math.sin(num)
  return sqrt_n, log_n, sin_n
  
#please enter the number
number = float(input("Enter a Number:"))
               
#calling the function
sqrt_n, log_n, sin_n = math_calc(number)

print(f"the squareroot of {number} is: {sqrt_n} \n The log of {number} is: {log_n} \n The Sine of {number} is: {sin_n}")


  
