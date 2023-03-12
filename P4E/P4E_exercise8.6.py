
# Exercise 6: Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum
# numbers after the loop completes.
# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

num_list = list()

while True:
    
    num_input = input("Enter your number: ")
    if num_input == "done":
        break
    float(num_input)
    num_list.append(num_input)

max_list = max(num_list)
min_list = min(num_list)

print(f"Maximum: {max_list} \nMinimum: {min_list}")

# Apparently you can't have two sets of quotation marks inside one print statement
# At least min_list wouldn't get interpreted if I did
