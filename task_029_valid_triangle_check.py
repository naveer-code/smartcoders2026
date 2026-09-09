s = [float(input(f"Enter side {i}: ")) for i in (1, 2, 3)]
s.sort()

if s[0] + s[1] > s[2]:
    print("Valid triangle")
else:
    print("Cannot form a valid triangle")
