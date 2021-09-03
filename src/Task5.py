"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):

    n = int(input("Введите n:"))
    # list который задает последовательность Фибоначи длиной заданной пользователем
    data = [0, 1]
    i = 0
    while i < n - 2:
        data.append(data[i] + data[i + 1])
        i += 1
    print("Элемент порядок которого %i в числовой последовательносии Фибоначи: %i" % (n, data[-1]))


if __name__ == '__main__':
    n = 0
    fibonacci(n)
