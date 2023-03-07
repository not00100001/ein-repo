fhand = open('/home/m4/PythonTutorials/P4E/mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        single_words = line.split()
        email = single_words[1]
        mail_split = email.split('@')
        print(mail_split[1])

# these two do the exact same thing

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From ") : continue 
    single_words = line.split()
    email = single_words[1]
    mail_split = email.split('@')
    print(mail_split[1])
