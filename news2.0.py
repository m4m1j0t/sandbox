length = int(input())
header = ''
for _ in range(0, int(input())):
    string = input()
    if header < 3:
        pass
    elif len(string) <= length >= 3:
        header += f'{string}\n'
    else:
        header += f'{string[:lebgth - 3]}...'
    length -= len(string)
print(header)