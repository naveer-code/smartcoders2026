n_limit = int(input("Enter N: "))

tot = 0
curr_fact = 1
for i in range(1, n_limit + 1):
    curr_fact *= i
    tot += curr_fact

print(f"Sum of factorials: {tot}")
