n = abs(int(input("Enter integer: ")))

bits_count = bin(n).count("1")
print(f"Number of set bits: {bits_count}")
