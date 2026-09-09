def print_dual(step, boundary):
    if step > boundary:
        return
    print(step, end=" ")
    print_dual(step + 1, boundary)
    if step != boundary:
        print(step, end=" ")

limit_val = int(input("Enter N: "))
print_dual(1, limit_val)
print()
