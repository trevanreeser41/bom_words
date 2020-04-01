#!/usr/bin/env python3
from sorters import bubble_sort, insertion_sort, selection_sort
from collections import namedtuple, Counter
import re


# data for a single word
WordData = namedtuple("WordData", [ 'word', 'count', 'percent' ])

def get_data():
    '''Returns the list of WordData objects'''
    # Read `bom.txt` into a string.

    # Convert the entire string to lowercase.

    # Split the string by any non-alpha character. Regular expressions are your friend here.
    # A simple regular expression with `re.split(...)` will do this for you.
    with open('bom.txt', 'r') as file:
        data = file.read().lower()
    data = re.split('[^a-zA-Z]', data)
    # Using a list comprehension with a conditional (if), create a new list that contains only
    # those words that are 5+ alpha characters in length. All of the following will be
    # skipped: "am", "", "i", "are".
    data = [item for item in data if len(item) >= 5]
    # Count the frequency of each word in the list, creating a WordData object for each
    # unique word.  Round all percentages to three decimal places: 3.141592 => 3.142.
    # See the `collections.Counter` module is your friend here.  The percent for a given
    # word is calculated as `count / length of list`, rounded to one decimal place.
    outputData = []
    unique_data = Counter(data)
    for i in unique_data:
        outputData.append(WordData(i, unique_data[i], round(unique_data[i]/len(data)*100,3)))
    # return the list of WordData objects, which contains
    # a single object for each unique word
    return outputData



#######################
###   Main loop

def main():
    '''Main program'''
    # get the WordData list
    data = get_data()
    # Sort the list of WordData objects by highest percent using your Bubble Sort
    # function. Sort the list in place (don't create a new list). Print the first 50
    # WordData objects in the list.
    print()
    print('BY PERCENT:')
    bubble_sort(data, 2, descending=True)
    for wd in data[:50]:
        print(wd)

    # Sort the list of WordData objects by highest count using your Insertion Sort
    # function. Sort the list in place (don't create a new list). Print the first 50
    # WordData objects in the list.
    print()
    print('BY COUNT:')
    data = get_data()
    insertion_sort(data, 1, descending=True)
    for wd in data[:50]:
        print(wd)

    # Sort the list of WordData objects by alpha order (a-z) using your Selection Sort
    # function. Sort the list in place (don't create a new list). Print the first 50
    # WordData objects in the list.
    print()
    print('BY WORD:')
    data = get_data()
    selection_sort(data, 0, descending=True)
    for wd in data[:50]:
        print(wd)


if __name__ == '__main__':
    main()