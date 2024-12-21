def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


data = list(input().split())
result = [int(data[0])]
for i in data[1:]:
    if i.isdigit():
        result.append(int(i))
    elif i == "/":
        a = result.pop()
        result[-1] //= a
    elif i == "~":
        result[-1] = -result[-1]
    elif i == "#":
        result.append(result[-1])
    elif i == "!":
        result[-1] = factorial(result[-1])
    elif i == "@":
        result.append(result.pop(-3))
    else:
        a = result.pop()
        exec("result[-1] " + i + "= a")
print(result[0])