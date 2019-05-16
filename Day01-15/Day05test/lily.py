

for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid **3 + high **3:
        print(num)

num1 = 2
num2 = 3

print(num1 * num1)
print(num1 ** num1)