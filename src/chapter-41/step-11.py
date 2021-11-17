'''
Задача на программирование: различные слагаемые
По данному числу 1 <= n <= 10^9 найдите максимальное число k, для которого nn можно представить как сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:
4
Sample Output 1:
2
1 3

Sample Input 2:
6
Sample Output 2:
3
1 2 3
'''

import sys


def calculate(n):
    nums = []
    total = 0
    for i in range(1, n+1):
        diff = n - total - i

        if diff <= i and diff != 0:
            continue

        nums.append(i)
        total += i

        if total == n:
            break

    print(len(nums))
    print(' '.join(str(i) for i in nums))


def main():
    n = 0
    for line in sys.stdin:
        n = int(line)
        return calculate(n)


if __name__ == "__main__":
    main()
