height = int(input("Enter number of rows: "))

for r in range(1, height + 1):
    if r == 1:
        print("*")
    elif r == height:
        print("*" * height)
    else:
        print("*" + " " * (r - 2) + "*")
