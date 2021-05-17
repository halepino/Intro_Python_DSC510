# Program to calculate total words and word counts from file
# Sent output to newly created text file
# DSC 510
# Programming Assignment 9.1 Week 9
# Author: Holly Figueroa
# Date: 05/14/21

#     Your program must have a header.
#     Create a new function called process_file.
#     This function will perform the same operations as pretty_print from week 8
#     however it will print to a file instead of to the screen.
#     Modify your main method to print the length of the dictionary to the file as opposed to the screen.
#     This will require that you open the file twice. Once in main and once in process_file.
#     Prompt the user for the filename they wish to use to generate the report.
#     Use the filename specified by the user to write the file.
#     This will require you to pass the file as an additional parameter to your new process_file function.

import string


# Function to take words from each line of file
def process_line(line, wordcount_dic):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.strip()
            word = word.lower()
            word = word.strip(string.punctuation)
            add_word(word, wordcount_dic)


# Function to add values to every key word added to dictionary
def add_word(word, wordcount_dic):
    if word in wordcount_dic:
        wordcount_dic[word] += 1
    else:
        wordcount_dic[word] = 1


# Move dictionary items to list form including word and word counts
def process_file(wordcount_dic, new_file):
    word_count_list = []
    for key, val in wordcount_dic.items():
        word_count_list.append((val, key))

    # Arrange list from highest count to lowest
    word_count_list.sort(reverse=True)

    # Create output text file to view dictionary length, words, and their counts
    with open(new_file, "w") as x:

        # Print header, words, and counts in a column style formatting
        x.write("{}{}{:15s}{}".format("Length of Dictionary: ", len(wordcount_dic), "\nWORD", "COUNT\n"))
        for val, key in word_count_list:
            x.write("{:15s}{} \n".format(key, val))


def main():
    # Create try loop to prevent errors of file not being found
    try:
        with open('gettysburg.txt', 'r') as gba_file:
            wordcount_dic = {}  # Create empty dictionary to carry into functions to be filled later
            for line in gba_file:
                process_line(line, wordcount_dic)

            # Create loop to get user input for filename and re-loop if name is not appropriate(.txt)
            while True:  # create new text file to put output
                new_file = str(input("Please type a file name ending in '.txt' to create text file output >>> ") .lower() .strip())

                # Test if file name chosen is a text file
                if new_file.endswith(".txt") is True:
                    break
                else:
                    print("Please follow file naming conventions. You also must end your file name with '.txt'\n")
                    print("nay")
                    continue

            # Move output to new text file with function
            process_file(wordcount_dic, new_file)

    # Capture missing file errors and invalid file names
    except FileNotFoundError:
        print("File Not Found - you must have gettysburg.txt file stored locally to run")
    except OSError:
        print("Sorry, this file name is problematic")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
