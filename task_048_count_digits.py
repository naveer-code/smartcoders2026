inp_num = abs(int(input("Enter a number: ")))

total_digits = len(str(inp_num)) if inp_num != 0 else 1
print(f"Number of digits: {total_digits}")
