size, line = int(input()), []
for _ in range(int(input())):
    line.append(input())
    for i in line:
        if len(i) < size - 3:
            print(i)
        elif len(i) == size:
            print(i)
        elif len(i) > size - 3:
            print(i[:size - 3] + '...')
