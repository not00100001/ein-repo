celsius = input("Convert this from Celsius to Fahrenheit, please: ")

fahrenheit = float(celsius) * 1.8 + 32

# if unconverted python throws an error because the input is a str. If converted to int it will only
# run if user inputs an int. We therefore convert to float.

fahrenheit = round(fahrenheit, 2)

print(f"{celsius} degree Celsius is {fahrenheit} degree Fahrenheit")

