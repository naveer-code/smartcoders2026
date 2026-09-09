n_fact = int(input("Enter N: "))

accum = 1
for k in range(2, n_fact + 1):
    accum *= k

print(f"Factorial of {n_fact}: {accum}")
