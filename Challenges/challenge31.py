import itertools


def sort_and_join_characters(element: tuple[str]) -> str:
    return "".join(sorted(element))


def main() -> None:
    input_list = input().split()
    string = input_list[0]
    num = int(input_list[1])
    list_tuple_combinations: list[tuple[str]]
    list_string_combinations: list[str]
    for i in range(1, num + 1):
        list_tuple_combinations = [*itertools.combinations(string, i)]

        list_string_combinations = [
            *map(sort_and_join_characters, list_tuple_combinations)
        ]

        list_string_combinations.sort()

        print(*list_string_combinations, sep="\n")


if __name__ == "__main__":
    main()
