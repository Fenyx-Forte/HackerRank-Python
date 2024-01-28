def print_design_pattern(n: int, m: int) -> None:
    center = ".|."
    welcome = "-WELCOME-"
    group1 = "---"
    group2 = ".|."

    const1 = int((n - 1) / 2)

    for i in range(n):
        if i < const1:
            print(
                group1 * (const1 - i),
                group2 * i,
                center,
                group2 * i,
                group1 * (const1 - i),
                sep="",
            )

        elif i == const1:
            print(group1 * (const1 - 1), welcome, group1 * (const1 - 1), sep="")

        else:
            print(
                group1 * (i - const1),
                group2 * (2 * const1 - i),
                center,
                group2 * (2 * const1 - i),
                group1 * (i - const1),
                sep="",
            )


def main() -> None:
    n, m = map(int, input().split())
    print_design_pattern(n, m)


if __name__ == "__main__":
    main()
