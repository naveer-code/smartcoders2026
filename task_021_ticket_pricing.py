years = int(input("Enter age: "))

if years < 5:
    res = "Ticket: Free"
elif years <= 12:
    res = "Ticket: $10 (Child)"
elif years <= 60:
    res = "Ticket: $20 (Adult)"
else:
    res = "Ticket: $15 (Senior)"

print(res)
