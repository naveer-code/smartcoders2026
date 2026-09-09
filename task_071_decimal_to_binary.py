dec = int(input("Enter decimal number: "))

if dec == 0:
    print("Binary: 0")
else:
    print(f"Binary: {bin(dec)[2:]}")
