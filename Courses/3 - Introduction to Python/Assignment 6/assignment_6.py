# -*- coding: utf-8 -*-
"""Assignment 6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/108vEiGCUATSbvUP10uWpeNg70PnwxPs8

#**Assignment: Check your Knowledge on Errors**
##By Ajay Sethuraman
##**Introduction**
Errors and exceptions are integral components of programming in Python, ensuring the robustness and fault-tolerance of code. Understanding how to handle errors gracefully not only prevents program crashes but also provides users with informative feedback. This assignment focuses on writing Python code to handle exceptions and errors efficiently by using different exception types, along with the try...except...else...finally construct. Through the completion of the tasks, we will explore the handling of common Python errors such as ZeroDivisionError, ValueError, IndexError, KeyError, and TypeError.

**Task 1 - Understanding Python Exceptions**

In this task, the objective is to handle two common exceptions—ZeroDivisionError and ValueError—while attempting to divide 100 by a user-entered number.
"""

def handle_exceptions():
    try:
        num = float(input("Enter a number: "))
        result = 100 / num
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"100 divided by {num} is {result:.2f}")

handle_exceptions()

"""* ZeroDivisionError: This exception is raised when attempting to divide by zero. The code catches this exception and informs the user of the issue.
* ValueError: Raised when the input is not a valid number. The program catches this error and asks the user to enter a valid number.
* Else block: If no errors occur, it prints the division result.

**Task 2 - Types of Exceptions**

This task involves raising and handling three different exceptions: IndexError, KeyError, and TypeError. Each exception is handled within its respective try...except block.
"""

def raise_exceptions():
    # Handling IndexError
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # Handling KeyError
    try:
        my_dict = {"name": "John", "age": 30}
        print(my_dict["address"])
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # Handling TypeError
    try:
        result = "Hello" + 5
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

raise_exceptions()

"""* IndexError: The code tries to access an index that is out of the range of the list. The exception is caught, and the user is notified about the invalid index.
* KeyError: The code tries to access a dictionary key that does not exist. The exception is raised and handled, displaying a message about the missing key.
* TypeError: The code attempts to add a string and an integer, which is an unsupported operation, raising a TypeError.

**Task 3 - Using try...except...else...finally**

This task asks for the implementation of the try...except...else...finally construct to divide two numbers. The finally block will print a message regardless of whether an exception occurred or not.
"""

def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"The result is {result}.")
    finally:
        print("This block always executes.")

divide_numbers()

"""* Try block: Attempts to divide num1 by num2. If successful, it prints the result.
* Except block: Handles two exceptions:
* ZeroDivisionError: Occurs when dividing by zero.
* ValueError: Occurs when the input is not a valid number.
* Else block: If no exceptions are raised, the division result is printed.
* Finally block: This block always runs, regardless of whether an exception occurred or not. It is useful for cleanup actions or final statements.

## **Conclusion**
In this assignment, we successfully implemented Python code to handle common errors such as ZeroDivisionError, ValueError, IndexError, KeyError, and TypeError. By using the try...except...else...finally construct, we were able to handle these exceptions gracefully, ensuring the program doesn't crash unexpectedly. We also demonstrated how each exception occurs and how it can be handled using the appropriate error messages. This assignment emphasized the importance of writing error-resilient code that can guide users towards providing correct input while maintaining a seamless experience.
"""

