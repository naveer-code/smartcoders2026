target_val = int(input("Enter number: "))
k_bit = int(input("Enter bit position K (0-indexed): "))

mask = 1 << k_bit
if target_val & mask:
    print(f"Bit {k_bit} is SET")
else:
    print(f"Bit {k_bit} is NOT SET")
