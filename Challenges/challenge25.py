def solve(string: str) -> str:
    list_charac: list[str] = []

    list_charac.append(string[0].upper())
    previous_charac_is_space = string[0] == ""

    for charac in string[1:]:
        if previous_charac_is_space:
            list_charac.append(charac.upper())

        else:
            list_charac.append(charac)

        if charac == " ":
            previous_charac_is_space = True

        else:
            previous_charac_is_space = False

    return "".join(list_charac)


def main() -> None:
    string = input()

    result = solve(string)

    print(result)


if __name__ == "__main__":
    main()
