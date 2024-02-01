def main() -> None:
    n = int(input())

    set_country = set()

    for _ in range(n):
        set_country.add(input())

    print(len(set_country))


if __name__ == "__main__":
    main()
