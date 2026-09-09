depth = int(input("Enter number of rows: "))

val = 1
for r in range(1, depth + 1):
    items = []
    for _ in range(r):
        items.append(str(val))
        val += 1
    print(" ".join(items) + " ")
