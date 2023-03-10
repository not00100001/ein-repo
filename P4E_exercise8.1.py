# Exercise  8.1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements.

def chop(input_list):
    input_list.remove(input_list[0])
    input_list.remove(input_list[-1])

#def chop(input_list):
#    del input_list[0]
#    del input_list[1]
# I found this sexy solution later
