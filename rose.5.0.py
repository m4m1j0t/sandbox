string, answer = input().lower().replace(' ', ''), 'YES'
while len(string) > 1:
    if string[0] == string[-1]:
        string = string[1:-1]
    else:
        answer = 'NO'
        break
print(answer)