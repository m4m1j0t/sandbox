band = [2, 10]
number = int(input())
string = ''
for i in band:
    while number != 0:
        y = number % i
        number = number // i
        string += f'{y}'
    print(string[::-1])