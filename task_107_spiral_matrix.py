n_size = int(input("Enter size n (e.g. 4): "))

mat = [[0] * n_size for _ in range(n_size)]
t, b, l, r = 0, n_size - 1, 0, n_size - 1
counter = 1

while t <= b and l <= r:
    for col in range(l, r + 1):
        mat[t][col] = counter
        counter += 1
    t += 1

    for row in range(t, b + 1):
        mat[row][r] = counter
        counter += 1
    r -= 1

    if t <= b:
        for col in range(r, l - 1, -1):
            mat[b][col] = counter
            counter += 1
        b -= 1

    if l <= r:
        for row in range(b, t - 1, -1):
            mat[row][l] = counter
            counter += 1
        l += 1

for line in mat:
    print(" ".join(f"{val:3d}" for val in line) + " ")
