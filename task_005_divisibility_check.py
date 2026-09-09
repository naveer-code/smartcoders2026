val = int(input("Enter any integer: "))

div_3 = (val % 3 == 0)
div_5 = (val % 5 == 0)

if div_3 and div_5:
    print("Divisible by both 3 and 5")
elif div_3:
    print("Divisible by 3")
elif div_5:
    print("Divisible by 5")
else:
    print("Divisible by neither")
