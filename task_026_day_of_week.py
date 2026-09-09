d_idx = int(input("Enter day of week (1-7): "))

day_names = {
    1: "Monday", 2: "Tuesday", 3: "Wednesday",
    4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"
}

if d_idx in day_names:
    print(f"Day: {day_names[d_idx]}")
else:
    print("Invalid day number")
