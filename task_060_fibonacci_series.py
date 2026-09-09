count = int(input("Enter number of terms N: "))

fib_list = []
a, b = 0, 1
for _ in range(count):
    fib_list.append(str(a))
    a, b = b, a + b

print(" ".join(fib_list) + (" " if fib_list else ""))
