countries = dict()
country = input()
str_number = 0
while country != "СТОП":
    if country not in countries:
        countries[country] = [str_number]
    else:
        countries[country].append(str_number)
    str_number += 1
    country = input()
for country in countries:
    print(f"{country}: {countries[country]}")
