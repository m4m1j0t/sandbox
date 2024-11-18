size, line = int(input()), []
for _ in range(int(input())):
    line.append(input())
for i in line:
    if size < 3:
        pass
    elif size - len(i) >= 3 or size == len(i):
        print(i)
    elif size - len(i) < 3:
        print(i[:size - 3] + '...')
    size -= len(i)