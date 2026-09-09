edge1 = float(input("Enter side 1: "))
edge2 = float(input("Enter side 2: "))
edge3 = float(input("Enter side 3: "))

unique_sides = len({edge1, edge2, edge3})
if unique_sides == 1:
    print("Equilateral triangle")
elif unique_sides == 2:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
