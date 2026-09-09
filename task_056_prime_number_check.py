test_num = int(input("Enter a number: "))

def is_prime(val):
    if val <= 1:
        return False
    if val <= 3:
        return True
    if val % 2 == 0 or val % 3 == 0:
        return False
    i = 5
    while i * i <= val:
        if val % i == 0 or val % (i + 2) == 0:
            return False
        i += 6
    return True

print("Prime number" if is_prime(test_num) else "Not a prime number")
