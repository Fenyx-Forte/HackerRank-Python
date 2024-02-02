def main() -> None:
    set_a = set(map(int, input().split()))

    len_a = len(set_a)
    n = int(input())

    strict_superset = True
    for _ in range(n):
        new_set = set(map(int, input().split()))

        strict_superset = (
            strict_superset and (len(new_set) < len_a) and (new_set.issubset(set_a))
        )

    print(strict_superset)


if __name__ == "__main__":
    main()
