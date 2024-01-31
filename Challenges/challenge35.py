from collections import defaultdict


def main() -> None:
    list_input = [*map(int, input().split())]
    n = list_input[0]
    m = list_input[1]

    defaultdict_a = defaultdict(list)

    for i in range(1, n + 1):
        word = input()
        defaultdict_a[word].append(i)

    for _ in range(1, m + 1):
        word = input()
        if len(defaultdict_a[word]) > 0:
            print(*defaultdict_a[word])
        else:
            print(-1)


if __name__ == "__main__":
    main()
