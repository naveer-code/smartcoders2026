target_num = int(input("Enter a number: "))

div_sum = 0
for i in range(1, target_num):
    if target_num % i == 0:
        div_sum += i

if div_sum == target_num and target_num > 0:
    print("Perfect number")
else:
    print("Not a perfect number")
