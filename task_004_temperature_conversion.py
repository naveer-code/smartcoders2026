val = float(input("Enter temperature: "))
opt = input("Convert to (C/F): ").strip().upper()

if opt == "F":
    out = (val * 1.8) + 32
    print(f"Fahrenheit: {out}")
elif opt == "C":
    out = (val - 32) * (5.0 / 9.0)
    print(f"Celsius: {out}")
else:
    print("Invalid choice")
