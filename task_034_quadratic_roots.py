import cmath

qa = float(input("Enter coefficient a: "))
qb = float(input("Enter coefficient b: "))
qc = float(input("Enter coefficient c: "))

delta = (qb ** 2) - (4 * qa * qc)

if delta > 0:
    x1 = (-qb + (delta ** 0.5)) / (2 * qa)
    x2 = (-qb - (delta ** 0.5)) / (2 * qa)
    print(f"Real and distinct roots: {x1} and {x2}")
elif delta == 0:
    x = -qb / (2 * qa)
    print(f"Real and equal roots: {x}")
else:
    re = -qb / (2 * qa)
    im = (abs(delta) ** 0.5) / (2 * qa)
    print(f"Imaginary roots: {re} + {im}i and {re} - {im}i")
