age = int(input("Enter age: "))

if age < 13:
    cat = "Child"
elif 13 <= age <= 19:
    cat = "Teenager"
elif 20 <= age < 60:
    cat = "Adult"
else:
    cat = "Senior"

print(cat)
