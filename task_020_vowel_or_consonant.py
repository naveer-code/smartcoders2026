letter = input("Enter character: ").lower()

vowel_list = ["a", "e", "i", "o", "u"]
if letter in vowel_list:
    print("Vowel")
elif letter.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")
