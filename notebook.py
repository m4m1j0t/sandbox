numbers = []
for i in input().split():
    numbers.append(i)
a = 1
for b in range(1, int(''.join(map(str, numbers))) + 1):
    a *= b
numbers = numbers[:-1]
numbers.append(a)
print(numbers)