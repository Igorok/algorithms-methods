'''
Задача на программирование: двоичный поиск

В первой строке даны целое число 1 <= n <= 10^5 и массив A[1 ... n] из n различных натуральных чисел, не превышающих 10^9, в порядке возрастания, во второй — целое число 1 <= k <= 10^5 и k натуральных чисел b[1], ..., b[k], не превышающих 10^9. Для каждого i от 1 до k необходимо вывести индекс 1 <= j <= n, для которого A[j] = b[i], или -1, если такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
'''

'''
1 2 3 4 5
0 5 - 1
0 2
0 1
0
0 5 - 5
3 5
4
0 5 - 10
3 5
5 5
'''




import sys
def bSearch(array, num):
    start, end = 0, len(array)
    while start < end:
        middle = (start + end) // 2
        if array[middle] == num:
            return middle
        elif array[middle] > num:
            end = middle
        elif array[middle] < num:
            start = middle + 1
    return -1


def calculate(data, numbers):
    for n in numbers:
        id = bSearch(data, n)
        print((-1 if id == -1 else id + 1), end=' ')


def main():
    data = ()
    dataLen = None
    numbers = ()
    numbersLen = None
    for line in sys.stdin:
        if dataLen is None:
            dataLen, *data = tuple(int(v) for v in line.split(' '))
        elif numbersLen is None:
            numbersLen, *numbers = tuple(int(v) for v in line.split(' '))
            return calculate(data, numbers)


if __name__ == "__main__":
    main()
