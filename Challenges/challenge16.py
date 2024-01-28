def print_full_name(first: str, last: str) -> None:
    template = "Hello {} {}! You just delved into python."
    output = template.format(first, last)
    print(output)


def main() -> None:
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


if __name__ == "__main__":
    main()
