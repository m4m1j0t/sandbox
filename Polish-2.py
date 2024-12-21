numbers = []


for i in (string := input().split()):

    if i in ['+', '-', '*', '/']:
        x, y = int(numbers[-2]), int(numbers[-1])
        if i == '+':
            result = x + y
        elif i == '-':
            result = x - y
        elif i == '/':
            result = x // y
        else:
            result = x * y
        numbers = numbers[:-2]
        numbers.append(result)

    elif i in ['~', '!']:
        if i == '~':
            result = -int(numbers[-1])
            numbers = numbers[:-1]
            numbers.append(result)
        else:
            a = 1
            for b in range(1, int(''.join(map(str, numbers))) + 1):
                a *= b
            numbers = numbers[:-1]
            numbers.append(a)

    elif i in ['#', '@']:
        if i == '#':
            x = numbers[-1]
            numbers.append(f' {x}')
        else:
            x, y, z = numbers[-1], numbers[-2], numbers[-3]
            numbers = numbers[:-3]
            numbers.append(f' {y}')
            numbers.append(f' {x}')
            numbers.append(f' {z}')
    else:
        numbers.append(i)

print(''.join(map(str, numbers)).lstrip())