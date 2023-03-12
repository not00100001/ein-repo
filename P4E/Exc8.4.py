
# Exercise  8.4: Download a copy of the file from www.py4e.com/code3/romeo.txt

# Write a program to open the file romeo.txt and read it line by line. For each
# line, split the line into a list of words using the split function.

# For each word, check to see if the word is already in a list. If the word is
# not in the list, add it to the list.

# When the program completes, sort and print the resulting words in alphabetical
# order.


fname = "/home/m4/PythonTutorials/P4E/romeo.txt"

fhand = open(fname)

final_list = list()

for line in fhand:
    split_line = line.split()    # could be shortened by saying >for i in line.split()<
    for i in split_line:
        if i not in final_list:
            final_list.append(i)

print(sorted(final_list))
            
