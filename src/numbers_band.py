number = int(input())
band = range(2, 11)
answer = 0
for i in band:
    result = 0
    string = ''
    x = number
    while x != 0:
        y = x % i
        x = x // i
        string += f'{y}'
        result += y
    if result > answer:
        answer = result
        best_band = i
print(best_band)