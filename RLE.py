string = list(input())
while len(string) > 0:
    run, count = string[0], 0
    for i in string:
        if i == run:
            count += 1
        else:
            break
    string = string[count:]
    print(run, count)