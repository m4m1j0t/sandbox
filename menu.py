menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
numbers = []
number = int(input())
if number <= 5:
    numbers += list(range(number))
else:
    while number != 0:
        if number >= 5:
            numbers += list(range(5))
            number -= 5
        else:
            numbers += list(range(number))
            break
for i in numbers:
    print(menu[i])