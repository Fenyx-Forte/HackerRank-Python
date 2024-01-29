import itertools


def main() -> None:
    list1 = [*map(int, input().split())]
    list2 = [*map(int, input().split())]
    print(*list(itertools.product(list1, list2)))


if __name__ == "__main__":
    main()
