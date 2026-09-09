m = float(input("Enter student marks (0-100): "))

if m >= 90:
    res_grade = "A"
elif m >= 80:
    res_grade = "B"
elif m >= 70:
    res_grade = "C"
elif m >= 60:
    res_grade = "D"
else:
    res_grade = "F"

print(f"Grade: {res_grade}")
