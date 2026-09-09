digits_str = str(abs(int(input("Enter a number: "))))

ans = 0
for d in digits_str:
    ans += int(d)

print(f"Sum of digits: {ans}")
