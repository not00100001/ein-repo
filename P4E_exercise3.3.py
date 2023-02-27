# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.

# Enter Hours: 20 
# Enter Rate: nine 
# Error, please enter numeric input

# Enter Hours: forty  
# Error, please enter numeric input

try:
    hour_input = float(input("How many hours? "))
except:
    print("Error, please enter numeric input")
    hour_input = float(input("How many hours? "))

try:
    rate_input = float(input("What is the rate? "))
except:
    print("Error, please enter numeric input")
    rate_input = float(input("What is the rate? "))

if hour_input <= 40:
    pay = hour_input * rate_input

elif hour_input > 40:
    pay = (40 * rate_input) + ((hour_input - 40) * (rate_input * 1.5))

else:
    print("Please don't ask the programmer why this is here.")

# python will not accept the multiplication if input is not converted from 'str' to 'int' or 'float'
# if converted to 'int' python will throw an error if user puts in float 

print(round(pay, 2))

# round function -> round(number, digits)
