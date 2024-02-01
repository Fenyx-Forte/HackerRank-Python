def main() -> None:
    n = int(input())

    set_a = set(map(int, input().split()))

    m = int(input())

    set_b = set(map(int, input().split()))

    list_sym_dif = sorted(list(set_a.symmetric_difference(set_b)))

    print(*list_sym_dif, sep="\n")


if __name__ == "__main__":
    main()
