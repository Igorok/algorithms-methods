# 10 2
def fib_mod(n, m):
    prev1 = prev2 = 1
    for i in range(n-2):
        prev1, prev2 = prev2, (prev2 + prev1) % m

    return prev2


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
