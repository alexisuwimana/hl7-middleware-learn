# file: error_handling.py
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("That was not a number.")
