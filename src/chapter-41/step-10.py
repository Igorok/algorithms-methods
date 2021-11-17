'''
Задача на программирование: непрерывный рюкзак
Первая строка содержит количество предметов 1 <= n <= 10^3 и вместимость рюкзака 0 <= W <= 2 * 10^6. Каждая из следующих n строк задаёт стоимость 0 <= c[i] <= 2 * 10^6 и объём 0 <= w[i] <= 2 * 10^6 предмета (n, W, c[i], w[i] — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:

3 50
60 20
100 50
120 30
Sample Output:

180.000
'''

import sys


class Product:
    def __init__(self, data):
        self.cost = data[0]
        self.weight = data[1]
        self.costByKilo = data[0] / data[1]


def calculate(n, W, data):
    if W == 0:
        print('0.000')
        return

    totalWeight = 0
    totalCost = 0
    data = sorted(data, key=lambda prod: prod.costByKilo, reverse=True)
    for product in data:
        if (totalWeight + product.weight <= W):
            totalWeight += product.weight
            totalCost += product.cost
        elif (totalWeight + product.weight > W) and (totalWeight < W):
            diffWeight = W - totalWeight
            diffCost = diffWeight * product.costByKilo
            totalWeight += diffWeight
            totalCost += diffCost

        if totalWeight == W:
            break

    print('{:10.3f}'.format(totalCost))


def main():
    n = 0
    W = 0
    data = []
    for line in sys.stdin:
        nums = tuple((int(v) for v in line.split()))
        if (n == 0):
            n = nums[0]
            W = nums[1]
            continue
        data.append(Product(nums))
        if (len(data) == n):
            return calculate(n, W, data)


if __name__ == "__main__":
    main()
