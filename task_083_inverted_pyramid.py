h = int(input("Enter number of rows: "))
for lvl in range(h, 0, -1):
    print(f"{' ' * (h - lvl)}{'*' * (2 * lvl - 1)}")
