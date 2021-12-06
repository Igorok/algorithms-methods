'''
Задача на программирование: сортировка подсчётом 
Первая строка содержит число 1 <= n <= 10^4, вторая — n натуральных чисел, не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих чисел.
Sample Input:
5
2 3 9 2 9

Sample Output:
2 2 3 9 9
'''

import sys

def sort(nums):
    grouped = [0] * 11
    for v in nums:
        grouped[v] += 1

    last = 0
    for i in range(11):
        if grouped[i] != 0:
            for j in range(last, last + grouped[i]):
                # nums[j] = i
                print(i, end=' ')
            last = last + grouped[i]

def main():
    countNums = None
    nums = []
    for line in sys.stdin:
        if countNums == None:
            countNums = int(line)
        else:
            nums = list(int(v) for v in line.split(' '))
            return sort(nums)


if __name__ == "__main__":
    main()
