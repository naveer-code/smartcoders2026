p_val = float(input("Enter principal: "))
r_pct = float(input("Enter interest rate: "))
t_yrs = float(input("Enter time period: "))

interest = (p_val * r_pct * t_yrs) / 100.0
print(f"Simple Interest: {interest}")
