x = 0
letters = ""
strings = ""
while (y := input()) != "ФИНИШ":
    string = "".join(y.split())
    strings += string.lower()
    for i in strings:
        if strings.count(i) >= x and i not in letters:
            x = strings.count(i)
            letters += str(i)
print(min(letters, key=str.lower))
