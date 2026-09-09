def sum_sq_digits(number):
    s = 0
    while number > 0:
        d = number % 10
        s += d * d
        number //= 10
    return s

val_check = int(input("Enter a number: "))
seen_set = set()

while val_check != 1 and val_check not in seen_set:
    seen_set.add(val_check)
    val_check = sum_sq_digits(val_check)

print("Happy Number" if val_check == 1 else "Not a Happy Number")
