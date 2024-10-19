class InputReader:
    def __init__(self):
        pass

    def read(self):
        return input()


def most_frequent_char(reader):
    x = 0
    letters = ""
    strings = ""
    while (y := reader.read()) != "ФИНИШ":
        strings += y.lower()
    string = "".join(strings.split())
    for i in string:
        if i in letters:
            pass
        else:
            if string.count(i) == x:
                letters += str(i)
            elif string.count(i) > x:
                letters = str(i)
                x = string.count(i)
    answer = "".join(sorted(letters))
    return answer[0]


if __name__ == "__main__":
    intput_reader = InputReader()
    res = most_frequent_char(intput_reader)
    print(res)


class ListReader:
    def __init__(self, list):
        self.list = list
        self.index = -1

    def read(self):
        self.index += 1
        return self.list[self.index]


def test_most_frequent_char():
    # Положительные тесты
    # 0, 1, 2
    r = ListReader(["привет", "мир", "ФИНИШ"])
    assert most_frequent_char(r) == "и"
    # r = ListReader(["кот", "собака", "кот", "ФИНИШ"])
    # assert most_frequent_char(r) == "к"
    # r = ListReader(["яблоко", "груша", "яблоко", "ФИНИШ"])
    # assert most_frequent_char(r) == "а"  # 'а' меньше по алфавиту

    # # Тест с пробелами
    # r = ListReader(["  а б в а б в    а б в  в  ", "ФИНИШ"])
    # assert most_frequent_char(r) == "в"

    # # Тест с символами разного регистра
    # r = ListReader(["АаБбВв ", "ФИНИШ"])
    # assert most_frequent_char(r) == "а"  # Игнорируем регистр

    # # Отрицательные тесты
    # r = ListReader(["ФИНИШ"])
    # assert most_frequent_char(r) == ""  # Пустая строка без символов
    # r = ListReader([" ", " ", " ", "ФИНИШ"])
    # assert most_frequent_char(r) == ""  # Только пробелы
