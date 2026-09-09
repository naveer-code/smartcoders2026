def recurse_digit_mult(val):
    if val < 10:
        return val
    return (val % 10) * recurse_digit_mult(val // 10)

in_num = abs(int(input("Enter a number: ")))
print(f"Product of digits: {recurse_digit_mult(in_num)}")
