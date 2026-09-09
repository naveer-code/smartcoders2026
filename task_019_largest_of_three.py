vals = [float(input(f"Enter number {idx}: ")) for idx in (1, 2, 3)]

greatest = vals[0]
for item in vals[1:]:
    if item > greatest:
        greatest = item

print(f"Largest: {greatest}")
