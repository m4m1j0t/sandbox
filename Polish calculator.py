numbers, operations, result = [], [], ''
for i in input().split( ):
    if i in ['+', '-', '*']:
        operations.append(i)
    else:
        numbers.append(i)
    for j in operations:
        x, y = int(numbers[-2]), int(numbers[-1])
        if i == '+':
            result = x + y
        elif i == '-':
            result = x - y
        elif i == '*':
            result = x * y
        else:
            print('Что-то пошло не так...')
        if len(numbers) > 2:
            numbers = numbers[:-2]
            numbers.append(str(result))
        else:
            print(result)
            break