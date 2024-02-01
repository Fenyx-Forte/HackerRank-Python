def main() -> None:
    first_row = input().split()
    n = int(first_row[0])
    m = int(first_row[1])

    integers = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    hapiness = 0

    for integer in integers:
        if integer in set_a:
            hapiness += 1

        if integer in set_b:
            hapiness -= 1

    print(hapiness)


if __name__ == "__main__":
    main()
