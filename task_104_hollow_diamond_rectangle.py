half_dim = int(input("Enter half size (e.g. 4): "))

for i in range(half_dim):
    side = "*" * (half_dim - i)
    hole = " " * (2 * i)
    print(side + hole + side)

for i in range(half_dim - 1, -1, -1):
    side = "*" * (half_dim - i)
    hole = " " * (2 * i)
    print(side + hole + side)
