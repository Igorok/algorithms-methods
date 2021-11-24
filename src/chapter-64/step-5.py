'''
Задача на программирование: число инверсий

Первая строка содержит число 1 <= n <= 10^5, вторая — массив A[1 ... n], содержащий натуральные числа, не превосходящие 10^9. Необходимо посчитать число пар индексов 1 <= i <= j <= n, для которых A[i] > A[j]. (Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)

Sample Input:
5
2 3 9 2 9
Sample Output:
2

7
7 6 5 4 3 2 1
21

5
1 2 3 5 4
1

6
1 3 4 5 6 2
4
'''

import sys


def mergeSortRec(array):
    if len(array) == 1:
        return array, 0

    middle = len(array) // 2
    left, li = mergeSortRec(array[:middle])
    right, ri = mergeSortRec(array[middle:])

    inversion = li + ri

    concated = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            concated.append(left[i])
            i += 1
        else:
            concated.append(right[j])
            j += 1
            inversion += len(left) - i

    while i < len(left):
        concated.append(left[i])
        i += 1

    while j < len(right):
        concated.append(right[j])
        j += 1

    return concated, inversion


def mergeSort(array=[]):
    while len(array) > 1:
        left = array.pop(0)
        right = array.pop(0)
        concated = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                concated.append(left[i])
                i += 1
            else:
                concated.append(right[j])
                j += 1

        while i < len(left):
            concated.append(left[i])
            i += 1

        while j < len(right):
            concated.append(right[j])
            j += 1

        array.append(concated)

    return array[0]


def calculate(array=[]):
    try:
        array, inversion = mergeSortRec(array)
        # array = mergeSort(list([v, ] for v in array))
        print(inversion)
    except Exception as e:
        print('e', e)


def main():
    array = []
    arrayLen = None
    for line in sys.stdin:
        if arrayLen is None:
            arrayLen = int(line)
        else:
            array = list(int(v) for v in line.split(' '))
            return calculate(array)


if __name__ == "__main__":
    main()
