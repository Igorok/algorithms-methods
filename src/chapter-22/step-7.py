# 841645
def fib_digit(n):
    prev1 = 1
    prev2 = 1
    for i in range(n-2):
        tmp = prev2
        prev2 = (prev2 + prev1) % 10
        prev1 = tmp

    return prev2


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
