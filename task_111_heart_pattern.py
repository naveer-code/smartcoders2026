for row in range(6):
    row_chars = []
    for col in range(7):
        top_lobes = (row == 0 and col % 3 != 0)
        upper_sides = (row == 1 and col % 3 == 0)
        diag_left = (row - col == 2)
        diag_right = (row + col == 8)
        if top_lobes or upper_sides or diag_left or diag_right:
            row_chars.append("*")
        else:
            row_chars.append(" ")
    print(" ".join(row_chars) + " ")
