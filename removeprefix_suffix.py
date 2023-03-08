my_str = "Thereistechnicallynoprefixherebecauseitsallrandom"

new_str = my_str.removeprefix("Therei")
new_str2 = my_str.removesuffix("sallrandom")

print(new_str)
print(new_str2)

print("Works.")

# so obviously there is no "offical list of pre- and suffixes"
# which python refers to. It will just take off beginnings and ends
# of strings. I just had to make sure.
