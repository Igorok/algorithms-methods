'''
По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано число 1 <= n <= 100 отрезков. Каждая из последующих n строк содержит по два числа 0 <= l <= r <= 10^9, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6

Sample Output 1:
1
3

Sample Input 2:
4
4 7
1 3
2 5
5 6

Sample Output 2:
2
3 6
'''

# [(4, 7), (1, 3), (2, 5), (5, 6)]
# [(1, 3), (2, 5), (4, 7), (5, 6)]
# [(1, 3), (2, 5), (5, 6), (4, 7)]
# [(4, 7), (5, 6), (2, 5), (1, 3)]

import sys


def calculate(n, data):
    data = sorted(data, key=lambda row: row[1])
    points = []
    last = data[0][1]
    for v in data:
        if v[0] <= last <= v[1]:
            continue
        else:
            points.append(last)
            last = v[1]
    points.append(last)

    print(len(points))
    print(' '.join((str(v) for v in points)))


def main():
    n = 0
    data = []
    for line in sys.stdin:
        nums = tuple((int(v) for v in line.split()))
        if (n == 0):
            n = nums[0]
            continue
        data.append(nums)
        if (len(data) == n):
            return calculate(n, data)


if __name__ == "__main__":
    main()
