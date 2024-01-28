cube = lambda x: x**3


def fibonacci(n: int) -> list[int]:
    list_fibonacci: list[int] = []
    a = 0
    b = 1
    for _ in range(n):
        list_fibonacci.append(a)
        c = a + b
        a = b
        b = c

    return list_fibonacci


def main() -> None:
    n = int(input())
    print(list(map(cube, fibonacci(n))))


if __name__ == "__main__":
    main()
