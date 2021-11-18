'''
Задача на программирование: декодирование Хаффмана

Восстановите строку по её коду и беспрефиксному коду символов.

В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв, встречающихся в строке, и размер получившейся закодированной строки, соответственно. В следующих k строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого. Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке хотя бы один раз. Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка имеет минимальный возможный размер.

В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита. Гарантируется, что длина правильного ответа не превосходит 10^4 символов.

Sample Input 1:
1 1
a: 0
0
Sample Output 1:
a

Sample Input 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
Sample Output 2:
abacabad
'''

import sys


def calculate(codeStr, charList):
    decodedStr = ''
    while len(codeStr) > 0:
        char = ''
        for v in charList:
            if (codeStr.startswith(v['code'])):
                char = v['char']
                codeStr = codeStr[len(v['code']):]
                break

        decodedStr += char

    print(decodedStr)


def main():
    charLen = 0
    charList = []
    codeLen = 0
    codeStr = ''
    i = 0
    for line in sys.stdin:
        if i == 0:
            charLen, codeLen = tuple(int(v) for v in line.split(' '))
        elif i <= charLen:
            char, code = line.split(' ')
            char, code = char[:-1], code.strip()
            charList.append({
                'char': char, 'code': code
            })
        else:
            codeStr = line.strip()
            return calculate(codeStr, charList)
        i += 1


if __name__ == "__main__":
    main()
