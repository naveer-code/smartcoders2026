num = int(input("Enter a number: "))

print(f"Divisors of {num}:")
d = 1
while d <= num:
    if num % d == 0:
        print(d, end=" ")
    d += 1
print()
