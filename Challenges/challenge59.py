from itertools import combinations_with_replacement


def sort_and_join_characters(tupla: tuple[str]) -> str:
    return "".join(sorted(tupla))


def main() -> None:
    row = input().split()
    string = row[0]
    num = int(row[1])
    list_string_combinations = [
        *map(sort_and_join_characters, combinations_with_replacement(string, num))
    ]
    list_string_combinations.sort()
    print(*list_string_combinations, sep="\n")


if __name__ == "__main__":
    main()
