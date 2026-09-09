inp_val = int(input("Enter a number: "))

if inp_val < 0:
    print("Not a palindrome")
else:
    s_val = str(inp_val)
    print("Palindrome" if s_val == s_val[::-1] else "Not a palindrome")
