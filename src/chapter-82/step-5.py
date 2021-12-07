'''
Задача на программирование: наибольшая последовательнократная подпоследовательность
Дано целое число 1 <= n <= 10^3 и массив A[1 ... n] натуральных чисел, не превосходящих 2 * 10^9. Выведите максимальное 1 <= k <= n, для которого найдётся подпоследовательность 1 <= i[1] < i[2] < ... < i[k] <= n длины k, в которой каждый элемент делится на предыдущий (формально: для  всех 1 <= j < k, A[i[j]] | A[i[j+1]].

Sample Input:
4
3 6 7 12

Sample Output:
3
'''

import sys


class Sequence:
    def __init__(self, numList):
        self.numList = numList
        self.countList = [0] * len(numList)

    def calculate(self):
        pass

    def getMax(self):
        pass


def sequence(nums):
    countList = [0] * len(nums)

    print('nums', nums, countList)

    pass


def main():
    countNums = None
    nums = []
    for line in sys.stdin:
        if countNums == None:
            countNums = int(line)
        else:
            numList = list(int(v) for v in line.split(' '))
            sequence = Sequence(numList)
            sequence.calculate()
            return sequence.getMax()


if __name__ == "__main__":
    main()
