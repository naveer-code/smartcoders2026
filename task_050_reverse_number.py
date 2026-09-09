target_int = int(input("Enter a number: "))

neg = target_int < 0
val = abs(target_int)
out_rev = 0

while val > 0:
    out_rev = (out_rev * 10) + (val % 10)
    val //= 10

if neg:
    out_rev = -out_rev

print(f"Reversed number: {out_rev}")
