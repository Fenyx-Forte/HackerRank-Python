def print_rangoli(size: int) -> None:
    a_value_ascii = 97
    line_size = (size * 4) - 3
    lines_num = (size * 2) - 1
    floor_half_lines_num = lines_num // 2

    l1: list[str] = []
    l2: list[str] = []
    middle_letter_value_ascii: int
    middle_letter: str
    for i in range(lines_num):
        l1.clear()
        l2.clear()

        if i <= floor_half_lines_num:
            middle_letter_value_ascii = a_value_ascii + floor_half_lines_num - i
            l1 = [(chr(middle_letter_value_ascii + j) + "-") for j in range(i, 0, -1)]
            l2 = [("-" + chr(middle_letter_value_ascii + j)) for j in range(1, i + 1)]

        else:
            middle_letter_value_ascii = a_value_ascii + i - floor_half_lines_num
            l1 = [
                (chr(middle_letter_value_ascii + j) + "-")
                for j in range((2 * floor_half_lines_num) - i, 0, -1)
            ]
            l2 = [
                ("-" + chr(middle_letter_value_ascii + j))
                for j in range(1, (2 * floor_half_lines_num) - i + 1)
            ]

        middle_letter = chr(middle_letter_value_ascii)

        left_string = "".join(l1)
        right_string = "".join(l2)
        center_string = left_string + middle_letter + right_string
        line_string = center_string.center(line_size, "-")
        print(line_string)


def main() -> None:
    n = int(input())
    print_rangoli(n)


if __name__ == "__main__":
    main()
