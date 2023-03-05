fname = input("Please enter the path to the file: ")

try:
    fhandle = open(fname)
except:
    print("That file could not be opened.")
    quit()

for line in fhandle:
    print(line.upper())
