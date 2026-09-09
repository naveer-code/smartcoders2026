levels_count = int(input("Enter number of rows: "))

seq_val = 1
for r in range(1, levels_count + 1):
    for _ in range(r):
        print(seq_val, end=" ")
        seq_val += 1
    print()
