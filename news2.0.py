x = int(input())
header_length = x
header = ""
for _ in range(0, n := int(input())):
    string = input()
    if len(string) <= x:
        header += f"{string} \n"
        x -= len(string)
        header_length += 1
    else:
        header += f"{string} \n"
if header_length == len(header):
    print(header)
else:
    print(f'{header[:header_length - 3]}...')