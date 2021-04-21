"""vowel Eater using -continue """

wordWithoutVovels = ""
userWord = input("enter the word ")  # Prompt the user to enter a word
userWord = userWord.upper()         # and assign it to the userWord variablec
for letter in userWord:
    if letter =="A":
        continue
    elif letter =="E":
        continue
    elif letter =="I":
        continue
    elif letter =="O":
        continue
    elif letter =="U":
        continue
    else:
       wordWithoutVovels =wordWithoutVovels  +letter
# Print the word assigned to wordWithoutVowels.
print(wordWithoutVovels )
