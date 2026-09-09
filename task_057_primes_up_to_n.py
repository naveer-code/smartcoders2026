limit_p = int(input("Enter N: "))

print(f"Prime numbers up to {limit_p}:")
for num in range(2, limit_p + 1):
    ok = True
    d = 2
    while d * d <= num:
        if num % d == 0:
            ok = False
            break
        d += 1
    if ok:
        print(num, end=" ")
print()
