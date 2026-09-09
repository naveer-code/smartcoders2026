orig = int(input("Enter a 3-digit number: "))

digits = [int(ch) for ch in str(abs(orig))]
if len(digits) == 3 and sum(d ** 3 for d in digits) == orig:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
