import itertools


def main() -> None:
    input_list = input().split()
    string = input_list[0]
    num = int(input_list[1])

    list_tuple_permutations = [*itertools.permutations(string, num)]

    list_string_permutations = [*map("".join, list_tuple_permutations)]

    list_string_permutations.sort()

    print(*list_string_permutations, sep="\n")


if __name__ == "__main__":
    main()
