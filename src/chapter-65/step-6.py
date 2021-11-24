'''
Задача на программирование: точки и отрезки
В первой строке задано два целых числа 1 <= n <= 50000 и 1 <= m <= 50000 — количество отрезков и точек на прямой, соответственно. Следующие n строк содержат по два целых числа a[i] и b[i] (a[i] <= b[i]) — координаты концов отрезков. Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю. Точка считается принадлежащей отрезку, если она находится внутри него или на границе. Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

Sample Input:
2 3
0 5
7 10
1 6 11
Sample Output:
1 0 0

https://www.youtube.com/watch?v=QN9hnmAgmOc
'''

import sys


def calculate(sections, points):
    print(sections, points)
    arr = [1, 2, 8, 5, 8, 3, 6, 4, 5, 1, 1, 4, 5, 6, 7, 8]


def main():
    countSection = None
    countPoint = None
    sections = []
    points = []
    i = 0
    for line in sys.stdin:
        if countSection == None:
            countSection, countPoint = list(int(v) for v in line.split(' '))
        elif i < countSection:
            sections.append(list(int(v) for v in line.split(' ')))
            i += 1
        else:
            points = list(int(v) for v in line.split(' '))
            return calculate(sections, points)


if __name__ == "__main__":
    main()
