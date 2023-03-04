# Exercise 5: Take the following Python code that stores a string:`

# str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the colon 
# character and then use the float function to convert the extracted 
# string into a floating point number.

data_str = "X-DSPAM-Confidence:0.8475"

start_float = data_str.find(":")

end_float = data_str.find("5", start_float)

our_float = data_str[start_float+1 : end_float+1]

print(float(our_float))


