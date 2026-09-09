def is_str_palindrome(txt):
    if len(txt) <= 1:
        return True
    if txt[0] != txt[-1]:
        return False
    return is_str_palindrome(txt[1:-1])

word = input("Enter a string: ")
print("Palindrome" if is_str_palindrome(word) else "Not a palindrome")
