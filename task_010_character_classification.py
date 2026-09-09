inp_ch = input("Enter a character: ")

if "A" <= inp_ch <= "Z":
    print("Uppercase letter")
elif "a" <= inp_ch <= "z":
    print("Lowercase letter")
elif "0" <= inp_ch <= "9":
    print("Digit")
else:
    print("Special character")
