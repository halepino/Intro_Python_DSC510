# Temperature Program
# DSC 510
# Programming Assignment 6.1 Week 6
# Author: Holly Figueroa
# Date: 04/19/21


def main():
    # Create main loop to continue program when completed
    while True:
        print("Welcome!\nEnter temperatures to get max and min then 'q' to quit ")
        temps = []

        # Create second loop to gather temps
        while True:
            temp_data = input()

            # Create sentinel value to stop adding temps to list
            if temp_data in {"q", "Q"}:
                break

            # Add input to temps list/specify as numeric data only
            try:
                float(temp_data)
                print("here")
                temps.append(temp_data)
                continue

            # Capture other non-numeric entries and redirect input
            except ValueError:
                print("please enter a number or 'q' to finish")

        # Sort and print min and max values from temps list
        temps.sort()
        print("Minimum temp was", temps[0], "degrees", "\nMaximum temp was", temps[-1], "degrees")
        print("Total temps entered:", len(temps), "\n")
        continue


if __name__ == "__main__":
    # Run Script
    main()
