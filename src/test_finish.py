import pytest


class InputReader:
    def __init__(self):
        pass

    def read(self):
        return input()


class ListReader:
    def __init__(self, list):
        self.list = list
        self.index = -1

    def read(self):
        self.index += 1
        return self.list[self.index]


def most_frequent_char(reader):
    x = 0
    letters = ""
    strings = ""
    while (y := reader.read()) != "ФИНИШ":
        string = "".join(y.split())
        strings += string.lower()
        for i in strings:
            if strings.count(i) >= x and i not in letters:
                x = strings.count(i)
                letters += str(i)
    return min(letters, key=str.lower)


def test_most_frequent_char():
    # Положительные тесты
    r = ListReader(["привет", "мир", "ФИНИШ"])
    assert most_frequent_char(r) == "и"
    r = ListReader(["кот", "собака", "кот", "ФИНИШ"])
    assert most_frequent_char(r) == "к"
    r = ListReader(["яблоко", "груша", "яблоко", "ФИНИШ"])
    assert most_frequent_char(r) == "а"  # 'а' меньше по алфавиту

    # Тест с пробелами
    r = ListReader(["  а б в а б в    а б в  в  ", "ФИНИШ"])
    assert most_frequent_char(r) == "в"

    # Тест с символами разного регистра
    r = ListReader(["АаБбВв ", "ФИНИШ"])
    assert most_frequent_char(r) == "а"  # Игнорируем регистр

    # Отрицательные тесты
    r = ListReader(["ФИНИШ"])
    assert most_frequent_char(r) == ""  # Пустая строка без символов
    r = ListReader([" ", " ", " ", "ФИНИШ"])
    assert most_frequent_char(r) == ""  # Только пробелы


if __name__ == "__main__":
    print(most_frequent_char(InputReader()))
