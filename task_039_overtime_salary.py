w_hrs = float(input("Enter hours worked: "))
h_rate = float(input("Enter hourly rate: "))

base_hours = min(w_hrs, 40.0)
ot_hours = max(0.0, w_hrs - 40.0)
gross_salary = (base_hours * h_rate) + (ot_hours * h_rate * 1.5)

print(f"Total Salary: {gross_salary}")
