numbers = list(map(int, input().split()))
a = numbers[0]
for b in numbers[1:]:
    while a != 0 and b != 0:
        a, b = b, a % b
print(a)