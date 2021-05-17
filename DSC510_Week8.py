# Program to calculate total words and word counts from file
# DSC 510
# Programming Assignment 8.1 Week 8
# Author: Holly Figueroa
# Date: 05/10/21

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
def pretty_print(wordcount_dic):
    word_count_list = []
    for key, val in wordcount_dic.items():
        word_count_list.append((val, key))

    # Arrange list from highest count to lowest
    word_count_list.sort(reverse=True)

    # Print header, words, and counts in a column style formatting
    print('{:15s} {}'.format("Word", "Count"))
    print()
    for val, key in word_count_list:
        print('{:15s}{}'.format(key, val))


def main():
    wordcount_dic = {}  # Create empty dictionary to carry into functions to be filled later
    with open('gettysburg.txt', 'r') as gba_file:
        for line in gba_file:
            process_line(line, wordcount_dic)
        print("Length of dictionary:", len(wordcount_dic))
        pretty_print(wordcount_dic)


if __name__ == "__main__":
    main()
