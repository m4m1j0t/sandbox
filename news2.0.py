x = int(input())
header_length = x
header = ""
for _ in range(0, int(input())):
    string = input()
    if len(string) < x:
        header += f"{string}\n"
        x -= len(string)
        header_length += 1
    elif len(string) == x:
        header += f"{string}\n"
        x = 0   
    else:
        header += f"{string}\n"
        x = 0
if header_length == len(header) or header_length > len(header):
    print(header)
else:
    print(f'{header[:header_length - 3]}... {header_length}')
