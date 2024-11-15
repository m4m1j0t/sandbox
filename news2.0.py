l, header, = int(input()), ''
for _ in range(0, n := int(input())):
    x = len(string := input())
    y = l - x
    if x <= l and y > 2:
        header += f'{string}\n'
        l -= x
    elif l == 0:
        pass
    else:
        z = l - 3
        header += f'{string[:z]}...'
        l = 0
print(header)