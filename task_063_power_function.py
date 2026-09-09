base_val = float(input("Enter base x: "))
exp_val = int(input("Enter exponent n: "))

out_pow = 1.0
count_exp = abs(exp_val)
for _ in range(count_exp):
    out_pow *= base_val

if exp_val < 0:
    out_pow = 1.0 / out_pow

print(f"{base_val}^{exp_val} = {out_pow}")
