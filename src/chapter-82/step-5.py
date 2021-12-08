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
        self.countList = [1] * len(numList)
        self.max = 0

    def calculate(self):
        if len(self.numList) == 1:
            self.max = 1
            return

        for i in range(1, len(self.numList)):
            for j in reversed(range(i)):
                if j < 0:
                    break

                div = self.numList[i] % self.numList[j]
                if div == 0 and 1 + self.countList[j] > self.countList[i]:
                    self.countList[i] = 1 + self.countList[j]

            if self.countList[i] > self.max:
                self.max = self.countList[i]

    def getLen(self):
        print(self.max)


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
            return sequence.getLen()


if __name__ == "__main__":
    main()
