terms = int(input("Enter N: "))

res = 0
for idx in range(1, terms + 1):
    res += idx if (idx % 2 == 1) else -idx

print(f"Sum of alternating series: {res}")
