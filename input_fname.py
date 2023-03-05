fname = input("Enter the filename please: ")

try:
    fhand = open(fname)
except:
    print(f"The file {fname} cannot be opened")
    quit()

# if we don't specify 'quit' a traceback will follow
# because fhand will be used later in the code

count = 0

for line in fhand:
    if line.startswith("From:"):
        count = count + 1
        print(line.rstrip())
print(f"There are {count} lines starting with \"From:\" ")

# r.strip() is added to remove the invisible \n character
# which follows every mail address

# notice the \ escape characters to print "From:"
