def main() -> None:
    a = int(input())
    set_a = set(map(int, input().split()))

    n = int(input())
    for _ in range(n):
        first_line = input().split()
        command = first_line[0]
        len_set = int(first_line[1])

        second_line = input().split()
        set_mutation = set(map(int, second_line))

        set_a.__getattribute__(command)(set_mutation)

    print(sum(set_a))


if __name__ == "__main__":
    main()
