result = ''
numbers = input().split()
expo = int(input())
for number in numbers:
    result += f'{int(number) ** expo} '
print(result.rstrip())