size = int(input())
lines = []

for _ in range(int(input())):
    lines.append(input())

for line in lines:
    if size <= 3:
        pass
    elif size - len(line) > 3 or size == len(line):
        print(line)
    elif size - len(line) <= 3:
        print(line[:size - 3] + '...')
    size -= len(line)