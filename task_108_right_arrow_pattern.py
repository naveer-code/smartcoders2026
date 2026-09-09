span = int(input("Enter max width (e.g. 4): "))

for i in range(1, span + 1):
    print("* " * i)

for i in range(span - 1, 0, -1):
    print("* " * i)
