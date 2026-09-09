numbers = []

while True:
    entry = float(input("Enter a number (-1 to stop): "))
    if entry == -1:
        break
    numbers.append(entry)

if numbers:
    print(f"Count: {len(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers)}")
else:
    print("No numbers were entered.")
