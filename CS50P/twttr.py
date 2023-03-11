
# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, 
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts
# the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.z

remove_vowel = input("Input your string: ")

vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# couldn't find a more elegant solution for including both upper- and lowercase
# vowels. But I'm sure it's out there.

for i in remove_vowel:
    if i in vowel_list:
        remove_vowel = remove_vowel.replace(i, "")
print(remove_vowel)
