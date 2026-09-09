first = int(input("First num: "))
second = int(input("Second num: "))

first = first ^ second
second = first ^ second
first = first ^ second

print(f"After swapping: a = {first} , b = {second}")
