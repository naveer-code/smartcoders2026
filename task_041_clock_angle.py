hrs = int(input("Enter hour (1-12): "))
mins = int(input("Enter minute (0-59): "))

pos_h = 0.5 * (60 * (hrs % 12) + mins)
pos_m = 6.0 * mins

delta_deg = abs(pos_h - pos_m)
res_angle = min(delta_deg, 360.0 - delta_deg)

print(f"Smaller angle: {res_angle} degrees")
