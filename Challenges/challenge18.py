def count_substring(string: str, sub_string: str) -> int:
    len_sub_string = len(sub_string)
    len_string = len(string)
    count = 0

    for i in range(len_string + 1 - len_sub_string):
        print(i, i + len_sub_string)
        if string[i : i + len_sub_string] == sub_string:
            count += 1

    return count


def main() -> None:
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


if __name__ == "__main__":
    main()
