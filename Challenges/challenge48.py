def main() -> None:
    t = int(input())

    set_a = None
    set_b = None
    for _ in range(t):
        len_a = int(input())
        set_a = set(map(int, input().split()))

        len_b = int(input())
        set_b = set(map(int, input().split()))

        print(set_a.issubset(set_b))


if __name__ == "__main__":
    main()
