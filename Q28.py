character = input("Enter a character: ").lower()
if len(character) == 1 and character.isalpha():
    if character in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Please enter one alphabet.")
