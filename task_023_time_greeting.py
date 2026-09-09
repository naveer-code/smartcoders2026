h = int(input("Enter hour (0-23): "))

if 5 <= h <= 11:
    print("Morning")
elif 12 <= h <= 16:
    print("Afternoon")
elif 17 <= h <= 20:
    print("Evening")
else:
    print("Night")
