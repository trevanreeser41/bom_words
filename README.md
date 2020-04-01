# Assignment: Book of Mormon Words

Create a new project and program three sorting algorithms:

1. Bubble Sort
2. Insertion Sort
3. Selection Sort

The grader will call your sort functions directly, so don't modify the signatures on these three functions. I suggest writing and testing these algorithms first--before doing anything with the Book of Mormon files.

Do not use the built-in sorting functions of your language, but you **can and should** use built-in data structures like `list`. You are not required to use the Array or LinkedList classes you programmed earlier in the course.

When reading and filtering the words from the data file, you can create new lists as needed. Once sorting starts, modify the list in place (don't create any new lists).


## File Analysis

Your assignment is to count the frequencies of each word used in the Book of Mormon. Follow this process:

1. Read `bom.txt` into a string.
2. Convert the entire string to lowercase.
3. Split the string by any non-alpha character. Regular expressions are your friend here. A simple regular expression with `re.split(...)` will do this for you.
4. Using a list comprehension with a conditional (if), create a new list that contains only those words that are 5+ characters in length. All of the following will be skipped: "am", "", "i", "are", "pass".
5. Count the frequency of each word in the list, creating a WordData object for each unique word.  Round all percentages to three decimal places: 3.141592 => 3.142.  See the `collections.Counter` module is your friend here.  The percent for a given word is calculated as `count / length of list`, rounded to one decimal place.
6. Sort the list of WordData objects by highest percent using your Bubble Sort function. Sort the list in place (don't create a new list). Print the first 50 WordData objects in the list.
7. Sort the list of WordData objects by highest count using your Insertion Sort function. Sort the list in place (don't create a new list). Print the first 50 WordData objects in the list.
8. Sort the list of WordData objects by alpha order (a-z) using your Selection Sort function. Sort the list in place (don't create a new list). Print the first 50 WordData objects in the list.

See the 'output.txt' file for the exact output your program will print to the console.

## Unit Testing

A unit test file has been started in `test_sorters.py`. Create at least 5 other test methods in this file. Each sorting algorithm should have at least 2 unit tests. When finished, your unit tests should:

* Use one or more self.assert*() calls in each test_* function.
* Contain no print statements. Tests should run silently unless they fail.

Keep the filename as `test_sorters.py` so the grader can find it.


## Getting Help Online

Do *not* copy Python code from online sources. You can reference existing code online, but you need to code these algorithms yourself. If you follow an example online, you must understand the code you are writing. Don't just copy.


## Submitting the Assignment

Zip your files and submit to the Grader at https://caplearning.net/.
