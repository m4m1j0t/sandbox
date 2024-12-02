numbers, result = [], ''
for i in input().split( ):
    if i in ['+', '-', '*'] and len(numbers) >= 2:
        x, y = int(numbers[-2]), int(numbers[-1])
        if i == '+':
            result = x + y
        elif i == '-':
            result = x - y
        else:
            result = x * y
        if len(numbers) > 2:
            numbers = numbers[:-2]
            numbers.append(str(result))
        else:
            numbers = numbers[:-2]
            numbers.append(result)
    elif i not in ['+', '-', '*']:
        numbers.append(i)
    else:
        print('Типо ого...')
print(result)