numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
expo = int(input())
for number in numbers:
    print(number ** expo)