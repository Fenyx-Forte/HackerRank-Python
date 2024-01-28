def swap_case(string: str) -> str:
    list_carac: list[str] = []

    for carac in string:
        if carac.isupper():
            list_carac.append(carac.lower())

        else:
            list_carac.append(carac.upper())

    swap_string = "".join(list_carac)

    return swap_string


def main() -> None:
    string = input()
    result = swap_case(string)
    print(result)


if __name__ == "__main__":
    main()
