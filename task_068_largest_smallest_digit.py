digits = [int(ch) for ch in str(abs(int(input("Enter a number: "))))]

hi = digits[0]
lo = digits[0]
for d in digits[1:]:
    if d > hi:
        hi = d
    if d < lo:
        lo = d

print(f"Largest digit: {hi}")
print(f"Smallest digit: {lo}")
