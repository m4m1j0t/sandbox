menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
result = []
number = int(input())
if number <= 5:
    numbers = list(range(number))
    result += numbers
else:
    while number != 0:
        if number >= 5:
            numbers = list(range(5))
            number -= 5
            result += numbers
        else:
            numbers = list(range(number))
            result += numbers
            break
for i in result:
    print(menu[i])