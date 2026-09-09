def recursive_vowels(s):
    if not s:
        return 0
    return int(s[0].lower() in "aeiou") + recursive_vowels(s[1:])

inp_str = input("Enter a string: ")
print(f"Number of vowels: {recursive_vowels(inp_str)}")
