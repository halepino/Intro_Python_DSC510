# Program of multiple calculation functions
# DSC 510
# Programming Assignment 5.1 Week 5
# Author: Holly Figueroa
# Date: 04/12/21


# Function to add two values
def add2(x, y):
    result = x + y
    print("\n Answer = ", result, "\n")


# Function to subtract using only two values
def sub2(x, y):
    result = x - y
    print("\n Answer = ", result, "\n")


# Function to multiply two values
def mul2(x, y):
    result = x * y
    print("\n Answer = ", result, "\n")


# Function to divide 2 values
def div2(x, y):
    result = x / y
    print("\n Answer = ", result, "\n")


def calculateAverage():
    while True:
        try:
            number_count = int(input("How many numbers do you need to average?\n"))
            if number_count > 0:
                num_sum = 0
                for n in range(number_count):
                    numbers2ave = float(input("Enter a number to include:"))
                    num_sum += numbers2ave

                result = num_sum / number_count
                print("_______________________________")
                print("Total:", num_sum, "  Average:", result)
                print()
                break

        except ValueError:
            print("\nPlease enter an integer (i.e., 3,5,10)")
            continue


# Function to perform Operations
def performCalculation(x):
    while True:
        # Direct user to basic operation functions
        if x in {"+", "-", "*", "/"}:
            try:
                # Get 2 numbers for calculation from user
                x1 = float(input("Please enter first number you want to use: "))
                x2 = float(input("Please enter second number you want to use: "))

                # Call Add function when selected
                if x == "+":
                    add2(x1, x2)
                    break

                # Call Subtract function when selected
                if x == "-":
                    sub2(x1, x2)
                    break

                # Call Multiply function when selected
                if x == "*":
                    mul2(x1, x2)
                    break

                # Call Divide function when selected
                if x == "/":
                    if x2 != 0:
                        div2(x1, x2)
                        break
                    else:
                        print("\nYou cannot divide by zero")
            except ValueError:
                print("You must enter a numbers only\n")
                continue


def main():
    while True:
        # Direct User to choose one of a limited number of operations
        x = input("What would you like to do? \n"
                  "Add(+), Sub(-), Multiply(*), Divide(/), or get an Average (ave)?\n") .strip() .lower()

        # Redirect user input that doesn't match options
        if x not in {"+", "-", "*", "/", "ave"}:
            print("Sorry, that's not one of the options\n")
            continue

        # Send simple operators to function
        if x in {"+", "-", "*", "/"}:
            performCalculation(x)

        # Send Average to Averaging function
        if x == "ave":
            calculateAverage()


if __name__ == "__main__":
    # Run Script
    main()
