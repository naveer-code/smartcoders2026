n_bound = int(input("Enter N: "))

evens = [x for x in range(1, n_bound + 1) if x % 2 == 0]
odds = [x for x in range(1, n_bound + 1) if x % 2 != 0]

print(f"Sum of even numbers: {sum(evens)}")
print(f"Sum of odd numbers: {sum(odds)}")
