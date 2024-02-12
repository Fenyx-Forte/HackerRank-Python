def main() -> None:
    n = int(input())
    integers = [*map(int, input().split())]
    condition1 = all([integer > 0 for integer in integers])

    if condition1:
        condition2 = any([str(integer) == str(integer)[::-1] for integer in integers])
        print(condition2)

    else:
        print(False)


if __name__ == "__main__":
    main()
