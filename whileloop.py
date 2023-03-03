my_str = "Schifffahrtskapitänsmütze"

count = 0

for i in my_str:
    if i == 'f':
        count = count + 1

# for i in my_str = "for each character in the string "Schifffahrtskapitänsmütze" run this loop 
# once changing the variable i to be the particular character we are pointing at"

print(count)

print(my_str[0:6])

# up to BUT NOT INCLUDING 6 (and as always startin from zero!)

print(my_str[:6])

#same as [0:6]

print(my_str[6:55])

# will not throw an error weirdly enough

print(my_str[6:])
