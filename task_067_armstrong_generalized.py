raw_val = int(input("Enter a number: "))

raw_str = str(abs(raw_val))
p = len(raw_str)
calc = sum(int(c) ** p for c in raw_str)

if calc == raw_val:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
