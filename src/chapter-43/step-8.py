'''
Задача на программирование: очередь с приоритетами

Первая строка входа содержит число операций 1 <= n <= 10^5. Каждая из последующих n строк задают операцию одного из следующих двух типов:
Insert x, где 0 <= x <= 10^9 — целое число;
ExtractMax

Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:
200
500
'''

'''
        20
    30      40
  35  36  42  43

[20, 30, 40, 35, 36, 42, 43]
'''




import sys
class Heap:
    def __init__(self):
        self.heap = []
        pass

    def _moveTop(self, i):
        if i <= 0:
            return
        while self.heap[i] > self.heap[(i - 1) // 2] and i > 0:
            self.heap[i], self.heap[(
                i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def _moveBottom(self, i):
        while (i * 2 + 1) < len(self.heap):
            l = i * 2 + 1
            r = i * 2 + 2
            j = i
            if self.heap[l] > self.heap[j]:
                j = l
            if r < len(self.heap) and self.heap[r] > self.heap[j]:
                j = r
            if j == i:
                break

            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def insert(self, v):
        self.heap.append(v)
        self._moveTop(len(self.heap) - 1)

    def extractMax(self):
        if len(self.heap):
            if len(self.heap) == 1:
                return self.heap.pop(0)
            elif len(self.heap) > 1:
                self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
                v = self.heap.pop(-1)
                self._moveBottom(0)
                return v


def main():
    heap = Heap()
    commandLen = None
    for line in sys.stdin:
        if commandLen == None:
            commandLen = int(line)
        else:
            data = line.split(' ')
            command = data[0]
            if command == 'Insert':
                heap.insert(int(data[1]))
            else:
                print(heap.extractMax())


if __name__ == "__main__":
    main()
