'''
Sample Input 1:

18 35
Sample Output 1:

1
Sample Input 2:

14159572 63967072
Sample Output 2:

4
'''


def gcd(a, b):
    if (a == 0 or b == 0):
        return max(a, b)

    while (a != 0):
        if a > b:
            a, b = a % b, b
        else:
            a, b = b % a, a

    return b


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
