# Program to calculate cable installation costs and print receipt
# DSC 510
# Programming Assignment 4.1 Week 4
# Author: Holly Figueroa
# Date: 04/08/21


# Function added to compute installation cost
def calculate_cost(length, cost):
    install_cost = length * cost
    return install_cost


def main():
    # Create welcome message for user
    print("Welcome!")

    # Retrieve company name from user
    company_name = input('Please enter company name: ')

    # Request input for cable length and specify input as integer
    while True:
        try:
            cable_length = (input('Enter foot length of cable for installation:'))
            cable_length = int(cable_length)
            if cable_length > 0:
                break
            if cable_length <= 0:
                print("Please enter a positive value, greater than zero")
                continue
        except ValueError:
            print('Oops! Please enter a number (i.e, 25)')

    # Create variable for current price per foot of cable
    foot_cost = 0.87

    # Create pay in bulk discount structure
    if cable_length >= 500:
        foot_cost = foot_cost - 0.37
    elif 250 <= cable_length < 500:
        foot_cost = foot_cost - 0.17
    elif 100 <= cable_length < 250:
        foot_cost = foot_cost - 0.07

    install_cost = calculate_cost(cable_length, foot_cost)

    # Format install_cost to currency
    # Format foot_cost to currency
    foot_cost = "${:,.2f}".format(foot_cost)
    install_cost = "${:,.2f}".format(install_cost)

    # Print Receipt
    print()
    print('*********** RECEIPT ************')
    print()
    print('Billed to:', company_name)
    print()
    print('Fiber Optic Cable Installation')  # Service provided
    print('', 'Cable Length', cable_length, 'ft')  # Displays cable length
    print('', 'Cost @', foot_cost, 'per ft =', install_cost)  # Displays Cost Calculation
    print()
    print('Total Amount Due:', install_cost)
    print()
    print('********************************')


if __name__ == "__main__":
    # Run Script
    main()
