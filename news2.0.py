line = int(input())
n = int(input())
header = ''

for _ in range(n):
    string = input()
    x = len(string)
    if x <= line:
        header += f'{string}\n'
        line -= x
    else:
        if line < 3:
            header += f'{string[:line]}\n'
            line = 0
        else:
            header += f'{string[:line-3]}...\n'
            line = 0

print(header)