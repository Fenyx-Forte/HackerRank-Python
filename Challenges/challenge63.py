# Company Logo
from collections import Counter


def main() -> None:
    s = input()
    list_tuple = Counter(sorted(s)).most_common(3)

    for key, value in list_tuple:
        print(key, value)


if __name__ == "__main__":
    main()
