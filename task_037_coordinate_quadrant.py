cx = float(input("Enter x coordinate: "))
cy = float(input("Enter y coordinate: "))

if cx == 0 and cy == 0:
    print("Origin")
elif cx == 0:
    print("On Y-axis")
elif cy == 0:
    print("On X-axis")
elif cx > 0 and cy > 0:
    print("First Quadrant")
elif cx < 0 and cy > 0:
    print("Second Quadrant")
elif cx < 0 and cy < 0:
    print("Third Quadrant")
else:
    print("Fourth Quadrant")
