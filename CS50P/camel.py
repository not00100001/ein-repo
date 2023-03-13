# In a file called camel.py, implement a program that
# prompts the user for the name of a variable in camel case
# and outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.

# GitHub Solution 1 : sexy as hell

# for i in str_convert:
#     if i.isupper():
#         new_str = "_" + i.lower()
#         i = new_str
#     print(i, end="")



# GitHub Solution 2 : still good

# for i in range(len(str_convert)):
#     if str_convert[i].isupper():
#         str_convert = str_convert[:i] + "_" + str_convert[i].lower() + str_convert[i+1:]

# print(str_convert)


# My terrible solution which only works if ONE uppercase is in str 
# because somehow it won't work to join the list within the iteration 

str_convert = input("Put in that string! ")

for i in range(len(str_convert)):
    if str_convert[i].isupper():
        up_letter = str_convert[i]
        str_list = str_convert.split(up_letter)
        str_list.insert(1, "_" + up_letter.lower())
        

print("".join(str_list))

# But I give up. I have failed. I can only copy other solutions now that I have seen them





