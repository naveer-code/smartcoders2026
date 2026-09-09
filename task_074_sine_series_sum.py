import math

theta = float(input("Enter angle in radians x: "))
n_terms = int(input("Enter number of terms: "))

result = 0.0
for i in range(n_terms):
    pow_idx = 2 * i + 1
    term = (theta ** pow_idx) / math.factorial(pow_idx)
    result += term if (i % 2 == 0) else -term

print(f"Sum of series: {result}")
