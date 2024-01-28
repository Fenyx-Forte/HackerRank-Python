def merge_the_tools(string: str, k: int) -> None:
    len_string = len(string)

    substrings: list[str] = [
        string[i : i + k] for i in range(0, len_string - k + 1, k)
    ]

    list_charac: list[str] = []

    for substring in substrings:
        list_charac.clear()
        for character in substring:
            if not (character in list_charac):
                list_charac.append(character)

        print("".join(list_charac))


def main() -> None:
    string, k = input(), int(input())
    merge_the_tools(string, k)


if __name__ == "__main__":
    main()
