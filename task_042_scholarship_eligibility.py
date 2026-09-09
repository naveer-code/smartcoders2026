pct_marks = float(input("Enter marks percentage: "))
pct_attend = float(input("Enter attendance percentage: "))
fam_inc = float(input("Enter annual family income: "))

ok = (pct_marks >= 80) and (pct_attend >= 75) and (fam_inc <= 250000)
print("Eligible for Scholarship" if ok else "Not Eligible for Scholarship")
