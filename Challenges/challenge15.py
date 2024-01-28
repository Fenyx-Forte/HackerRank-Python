def split_and_join(line: str) -> str:
    list_words: list[str] = line.split()
    new_string = "-".join(list_words)

    # return line.replace(" ", "-")
    return new_string


def main() -> None:
    line = input()
    result = split_and_join(line)
    print(result)


if __name__ == "__main__":
    main()
