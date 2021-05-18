# Chuck Norris Jokes Program
# Jokes from website json data
# Objective: Entertain the lesser mortals
# DSC 510
# Programming Assignment 10.1 Week 10
# Author: Holly Figueroa
# Date: 05/17/21

import requests
import json
import textwrap


# Make super cool image of Chuck Norris doing a roundhouse for printout
def kick_print():
    print("\n                  \  |   /")
    print("*********************  ****   PRESS 'K' TO GET YOUR  *****************************************************")
    print("****   *************   ****   ")
    print("***     **********   ******   ***    *****   *****   *********   ***    *****    ********        ***   ***")
    print("*****       ****   ********   ***    ****     ***   ***********  ***    ****   *****  *****      ***   ***")
    print("****         *   **********   ***  ****       ***   ***     ***  ***  ****    ****               ***   ***")
    print("****  **        **  *******   *******         ***   ***          *******        ********         ***   ***")
    print("*********    **************   ***  ****       ***   ***          ***  ****           ******      ***   ***")
    print("*********   ***************   ***    ***      ***   ***     ***  ***    ***             ****")
    print("*********   ***************   ***     ****    ***   ***********  ***     ****  *****   ****      ***   ***")
    print("**********  ***************   ***      ***** *****   *********   ***     *****   ********        ***   ***")
    print("*********   ***************   ")
    print("*******-----***************   PRESS 'Q' TO QUIT   ********************************************************")


def main():
    # Create main loop to allow for exiting program
    while True:
        # Greeting
        print("Welcome!")
        print("Do you get get a kick out of Chuck Norris jokes?")
        kick_print()

        # Create loop to allow user to continue jokes when selected
        while True:

            # Get input to direct user to another joke or to quit
            choice = input("ENTER HERE >>> ").strip().lower()

            # Capture unacceptable input
            if choice not in {"k", "q"}:
                print("\nWas that entry a joke?        ...maybe leave that to the program.")
                print("\nPress 'K' for more or 'Q' to quit")

            # Bring user (more) jokes
            if choice == 'k':

                # Try block to prevent errors/crashing due to api issues
                try:

                    # Request json data from website and load text
                    chuck = requests.get('https://api.chucknorris.io/jokes/random')
                    chuck.raise_for_status()
                    contents = json.loads(chuck.text)

                    # Pull joke only from page contents and format for printing
                    joke = (contents.get('value'))
                    print("\n")
                    print("*" * 106, "\n")
                    for line in textwrap.wrap(joke, width=100):
                        print("  ", line)
                    kick_print()

                except Exception as e:
                    print(e)
                continue

            # Allow user to quit
            if choice == 'q':
                print("\nChuck Norris never quits, but you can.\n...Goodbye")
                break
        break


if __name__ == "__main__":
    main()
