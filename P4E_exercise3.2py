# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10 

# Pay: 475.0

hour_input = float(input("How many hours? "))

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
