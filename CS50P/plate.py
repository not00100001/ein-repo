# In Massachusetts, home to Harvard University, it’s possible to request a vanity 
# license plate for your car, with your choice of letters and numbers instead of 
# random ones. Among the requirements, though, are:
    
#     “All vanity plates must start with at least two letters.”
#     “… vanity plates may contain a maximum of 6 characters (letters or numbers) 
#     and a minimum of 2 characters.”
#     “Numbers cannot be used in the middle of a plate; they must come at the end. 
#     For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be 
#     acceptable. The first number used cannot be a ‘0’.”
#     “No periods, spaces, or punctuation marks are allowed.”

# In plates.py, implement a program that prompts the user for a vanity plate and then
# output Valid if meets all of the requirements or Invalid if it does not. 
# Assume that any letters in the user’s input will be uppercase. 
# Structure your program per the below, wherein is_valid returns True 
# if s meets all requirements and False if it does not. Assume that s will be a str. 
# You’re welcome to implement additional functions for is_valid to call 
# (e.g., one function per requirement).

# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     ...


# main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

invalid_input = [" ", ".", "!", "?", ",", ":", ";"]

def is_valid(s):
    for i in s:
        if i in invalid_input:
            return False
    
    # Checks to see if forbidden characters in invalid_input are being used.

    split_zero = s.split("0")
    before_zero = split_zero[0]

    def has_numbers(has_num):
        return any(char.isdigit() for char in has_num)

    if len(split_zero) > 1: 
        if not has_numbers(before_zero):
            return False

    # Splits the input at every occurence of "0". Then makes before_zero the first
    # part of the split. Checks to see if the string was split at all with if len(split_zero) > 1)
    # because else Traceback occurs when s[1] is checked below. Then the split str is
    # given to def has_numbers which returns True if any char is a digit. If any char
    # is a digit it means the zero is not the first occurence in the plate and the program
    # can continue.

        if len(s) >= 2:
            if s[0].isalpha() and s[1].isalpha():
                if len(s) <= 6:
                    if s[-1].isdigit() or s[:].isalpha():
                        return True

     # Checks the rest of the requirements. The last if statement checks that the last char is a number
     # (as required) but also includes (with OR) input without any numbers at all, as such input is valid as well.            

            else:
                return False

main()

#nohelp
#proudofthisone
