size, line = int(input()), []
for _ in range(int(input())):
    line.append(input())
for i in line:
    if size <= 3:
        pass
    elif len(i) < size - 3 or len(i) == size:
        print(i)
        size -= len(i)
    elif len(i) > size - 3:
        print(i[:size - 3] + '...')
        size -= len(i)
