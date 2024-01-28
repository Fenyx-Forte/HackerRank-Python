def print_formatted(number: int) -> None:
    pad = len("{0:b}".format(number))

    for i in range(1, number + 1):
        string_decimal = str(i).rjust(pad)
        string_octal = oct(i)[2:].rjust(pad)
        string_hexadecimal = hex(i)[2:].upper().rjust(pad)
        string_binary = bin(i)[2:].rjust(pad)
        print(
            string_decimal,
            string_octal,
            string_hexadecimal,
            string_binary,
        )


def main() -> None:
    n = int(input())
    print_formatted(n)


if __name__ == "__main__":
    main()
