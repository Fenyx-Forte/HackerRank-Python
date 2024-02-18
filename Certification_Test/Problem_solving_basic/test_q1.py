def decryptPassword(s: str) -> str:
    len_s = len(s)
    qtd_0 = s.count("0")
    qtd_star = s.count("*")
    len_password = len_s - qtd_0 - qtd_star

    qtd_digits_except_zero = 0
    for j in range(1, 10):
        qtd_digits_except_zero += s.count(str(j))

    list_chars = ["" for _ in range(len_password)]
    count_zero = 0
    count_star = 0

    for i in range(len_s):
        if s[i] == "0":
            list_chars[i - qtd_digits_except_zero - count_star] = s[
                qtd_0 - count_zero - 1
            ]
            count_zero += 1

        elif (
            (i <= (len_s - 3))
            and s[i].isupper()
            and s[i + 1].islower()
            and s[i + 2] == "*"
        ):
            list_chars[i - qtd_digits_except_zero - count_star] = s[i + 1]
            list_chars[i + 1 - qtd_digits_except_zero - count_star] = s[i]
            count_star += 1

        elif s[i] not in "123456789*":
            list_chars[i - qtd_digits_except_zero - count_star] = s[i]

    password = "".join(list_chars)

    return password


def main() -> None:
    s = input()

    result = decryptPassword(s)

    print(result)


if __name__ == "__main__":
    main()
