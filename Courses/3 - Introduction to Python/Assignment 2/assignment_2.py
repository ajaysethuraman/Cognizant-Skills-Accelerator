# -*- coding: utf-8 -*-
"""Assignment 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qSK_90bhfIA9tdP8ZuhTVG_R9OHNtpiR

# **Explore Loops in Python**
## By Ajay Sethuraman
## **Introduction**
Loops are a fundamental concept in programming that allow us to execute repetitive tasks efficiently. In this assignment, we will explore both for and while loops to solve three practical problems: a countdown timer, a multiplication table, and factorial calculation.

**Task 1:**
* Ask the user for a starting number.
* Use a while loop to decrement the number until it reaches 1.
* Print the countdown numbers in a single line followed by "Blast off! 🚀".
"""

# Asking the user for a starting number
start = int(input("Enter the starting number: "))

# Countdown loop
while start > 0:
    print(start, end=" ")  # Print on the same line
    start -= 1  # Decrease the number by 1

# Print final message
print("Blast off!🚀")

"""**Task 2:**
* Ask the user for a number.
* Use a for loop to iterate through numbers 1 to 10.
* Multiply the input number by each iteration value and print the result.
"""

# Asking the user for a number
num = int(input("Enter a number: "))

# Generating the multiplication table using a for loop
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

"""**Task 3:**
* Ask the user for a number.
* Initialize a variable (factorial = 1) to store the result.
* Use a for loop to multiply numbers from 1 to the given number.
* Print the result in a formatted message.
"""

# Asking the user for a number
num = int(input("Enter a number: "))

# Initializing factorial value
factorial = 1

# Calculating factorial using a for loop
for i in range(1, num + 1):
    factorial *= i  # Multiply and update factorial

# Printing the result
print(f"The factorial of {num} is {factorial}.")

"""## **Conclusion**
This assignment demonstrated the power of loops in Python.

* I used a while loop for the countdown timer.
* I used a for loop to generate a multiplication table.
* I also used a for loop to compute the factorial of a number.

These tasks help build a strong understanding of iterative structures and how they can be used to solve real-world problems efficiently.
"""