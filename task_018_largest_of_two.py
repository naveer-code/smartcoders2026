first_num = float(input("Enter number 1: "))
second_num = float(input("Enter number 2: "))

if first_num > second_num:
    print(f"Largest: {first_num}")
elif second_num > first_num:
    print(f"Largest: {second_num}")
else:
    print("Both numbers are equal")
