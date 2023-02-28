# Rewrite your pay computation with time-and-a-half for overtime and create a function called 
# computepay which takes two parameters ( hours and  rate).

# Enter Hours: 45
# Enter Rate: 10 

# Pay: 475.0

def computepay (h, r):
    
    if h <= 40:
        pay = h * r
        
    elif h > 40:
        pay = (40 * r) + ((h - 40) * (r * 1.5))

    else:
        print("Please don't ask the programmer why this is here.")
    
    print(round(pay, 2))

hour_input = float(input("How many hours? "))
rate_input = float(input("What is the rate? "))

computepay(hour_input, rate_input)


# python will not accept the multiplication if input is not converted from 'str' to 'int' or 'float'
# if converted to 'int' python will throw an error if user puts in float 

# round function -> round(number, digits)
