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

'''


'''
def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = []
    right = []
    middle = []

    for k, v in enumerate(array):
        if (k == len(array) // 2) or v == pivot:
            middle.append(v)
        elif v < pivot:
            left.append(v)
        else:
            right.append(v)

    return quickSort(left) + middle + quickSort(right)


def calculate1(sections, points):
    startDict = {}
    sortedStarts = []
    cache = {}
    for v in sections:
        obj = {
            "s": v[0],
            "e": {},
            "sortedEnds": []
        }
        if v[0] in startDict:
            obj = startDict[v[0]]
        if not v[1] in obj["e"]:
            obj["e"][v[1]] = 0
            obj["sortedEnds"].append(v[1])
            obj["sortedEnds"] = sorted(obj["sortedEnds"])

        for k in obj["sortedEnds"]:
            if k > v[1]:
                break
            obj["e"][k] += 1

        startDict[v[0]] = obj

    sortedStarts = sorted(startDict.keys())

    for point in points:
        if point in cache:
            print(cache[point], end=' ')
            continue

        cache[point] = 0

        for start in sortedStarts:
            if point < start:
                continue
            if startDict[start]["sortedEnds"][-1] < start:
                continue

            for end in startDict[start]["sortedEnds"]:
                if point > end:
                    continue
                if point <= end:
                    cache[point] += startDict[start]["e"][end]
                    break

        print(cache[point], end=' ')



def getSections(array, point):
    if point < array[0][0] or point > array[-1][1]:
        return 0

    start = 0
    end = len(array)
    middle = 0

    while start < end:
        middle = (end + start) // 2
        if array[middle][0] <= point and array[middle][1] >= point:
            break
        elif array[middle][1] < point:
            start = middle + 1
        elif array[middle][0] > point:
            end = middle - 1

    if start == len(array):
        return 0
    middle = (end + start) // 2

    print(start, end, middle)

    if (array[middle][0] > point or array[middle][1] < point):
        return 0

    count = 1
    i = 1
    while (middle - i >= 0) and (array[middle - i][0] <= point and array[middle - i][1] >= point):
        i += 1
        count += 1

    j = 1
    while (middle + j < len(array)) and (array[middle + j][0] <= point and array[middle + j][1] >= point):
        j += 1
        count += 1

    return count


def calculate2(array, points):
    array = sorted(array, key=lambda v: (v[0]))

    cache = {}
    for p in points:
        if not p in cache:
            cache[p] = getSections(array, p)
        print(cache[p], end=' ')
'''




import sys
def getLengthStart(array, point):
    if array[0] > point:
        return 0
    if array[-1] <= point:
        len(array)

    start = 0
    end = len(array)
    middle = (start + end) // 2

    while start < end and start != middle:
        if array[middle] <= point:
            start = middle
        else:
            end = middle
        middle = (start + end) // 2

    return middle + 1


def getLengthEnd(array, point):
    if array[-1] < point:
        return len(array)
    if array[0] >= point:
        return 0

    start = 0
    end = len(array)
    middle = (end + start) // 2

    while start < end and middle != start:
        if array[middle] < point:
            start = middle
        elif array[middle] >= point:
            end = middle
        middle = (end + start) // 2

    return middle + 1


def calculate(array, points):
    cache = {}
    arr1 = sorted(list(v[0] for v in array))
    arr2 = sorted(list(v[1] for v in array))

    for p in points:
        if not p in cache:
            startLess = getLengthStart(arr1, p)
            endLess = getLengthEnd(arr2, p)
            cache[p] = startLess - endLess
        print(cache[p], end=' ')


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
