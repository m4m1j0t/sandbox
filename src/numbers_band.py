number, band, answer = int(input()), range(2, 11), 0

for base in band:
    result, temp_number = 0, number
    while temp_number != 0:
        remainder, temp_number = temp_number % base, temp_number // base
        result += remainder
    if result > answer:
        answer, best_base = result, base

print(best_base)