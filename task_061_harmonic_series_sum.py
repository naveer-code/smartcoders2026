n_val = int(input("Enter N: "))

h_sum = 0.0
for k in range(1, n_val + 1):
    h_sum += 1.0 / k

print(f"Sum of harmonic series: {round(h_sum, 4)}")
