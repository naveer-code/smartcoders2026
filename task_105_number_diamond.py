peak_val = int(input("Enter peak number (e.g. 4): "))

def render_row(curr, max_val):
    lead = "  " * (max_val - curr)
    left_side = [str(x) for x in range(1, curr + 1)]
    right_side = [str(x) for x in range(curr - 1, 0, -1)]
    print(lead + " ".join(left_side + right_side) + " ")

for k in range(1, peak_val + 1):
    render_row(k, peak_val)

for k in range(peak_val - 1, 0, -1):
    render_row(k, peak_val)
