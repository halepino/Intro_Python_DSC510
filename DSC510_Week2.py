# Program to calculate cable installation costs and print receipt
# DSC 510
# Programming Assignment 2.1 Week 2
# Author: Holly Figueroa
# Date: 03/24/21

# Create welcome message for user
print("Welcome!")

# Retrieve company name from user
company_name = input('Please enter company name: ')

# Request input for cable length and specify input as integer
cable_length = int(input('Enter foot length of cable for installation:'))

# Create variable for current price per foot of cable
foot_cost = 0.87

# Create variable for installation cost
install_cost = (cable_length * foot_cost)

# Print out installation costs in receipt format
# Receipt header including company name
print()
print('*********** RECEIPT ************')
print()
print('Billed to:', company_name)
print()

# Charge Details and Total
print('*********** CHARGES ************')
print()
print('Fiber Optic Cable Installation')  # Service provided
print('', 'Cable Length', cable_length, 'ft')  # Displays cable length
print('', 'Cost @', foot_cost, 'per ft = $', install_cost)  # Displays Cost Calculation
print()
print('********************************')
print()
print('Total Amount Due: $', install_cost)
