# -*- coding: utf-8 -*-
"""Project 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j6I2XLldzNBRqwB2V67rut-fmprElhbP

# **Eligible Elector**
## By Ajay Sethuraman
## **Introduction**
This project aims to build a simple Python program to check if a user is eligible to vote based on their age. The program will take the user’s age as input and then use conditional statements to determine whether they are old enough to vote. If they are not, the program will also tell them how many years are left until they are eligible. Additionally, we'll add input validation to handle potential errors, such as non-numeric or negative age inputs.
"""

# Asking the user to enter their age
age = int(input("How old are you? "))  # Convert input to integer

"""We use the input() function to take the user's age as input, and then we convert it into an integer using int(). This ensures that we can perform numerical operations on the input, such as checking if it's greater than or equal to 18."""

# Conditional statement to check eligibility
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    years_left = 18 - age  # Calculate how many years they need to wait
    print(f"Oops! You’re not eligible yet. But hey, only {years_left} more years to go!")

"""* The program uses an if statement to check if the user’s age is 18 or greater.
    * If the user is eligible to vote, the program displays a congratulatory message.
    * If the user is not eligible, it calculates how many more years they need to wait (by subtracting their age from 18) and informs them of how many years are left.
"""

# Function to check if input is valid
def get_valid_age():
    while True:
        try:
            # Asking for age input and converting it to integer
            age = int(input("How old are you? "))
            if age < 0:
                print("Oops! Age can't be negative. Please enter a valid age.")
            else:
                return age
        except ValueError:
            print("Oops! Please enter a valid number.")

# Get valid age from user
age = get_valid_age()

# Conditional statement to check eligibility
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    years_left = 18 - age  # Calculate how many years they need to wait
    print(f"Oops! You’re not eligible yet. But hey, only {years_left} more years to go!")

"""* The function get_valid_age() ensures the program keeps asking the user for input until they provide a valid, non-negative integer.
* It uses a try-except block to catch ValueError exceptions if the user enters something other than a number.
* It also checks if the entered age is negative, and if so, asks the user to enter a valid positive age.
* Once a valid age is entered, the program proceeds with the eligibility check.

## **Conclusion**
In this project, we built a simple Python program to check voter eligibility based on the user's age. We started by asking for the user's age and then used conditional statements to determine whether they were eligible to vote. We also added input validation to handle errors like negative or non-numeric inputs. By the end of this project, you have a fully functional program that checks voter eligibility and provides a friendly message to the user.

This project demonstrates how to use basic Python concepts such as input, conditionals, and loops to create a useful and interactive program.
"""