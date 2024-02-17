def verify_upper_case(uid: str) -> bool:
    alphabet_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count_upper = 0
    for char in uid:
        if char in alphabet_characters:
            count_upper += 1

        if count_upper >= 2:
            break

    if count_upper >= 2:
        return True

    return False


def verify_3_digits(uid: str) -> bool:
    digits = "0123456789"

    count_digits = 0
    for char in uid:
        if char in digits:
            count_digits += 1

        if count_digits >= 3:
            break

    if count_digits >= 3:
        return True

    return False


def verify_alpha(uid: str) -> bool:
    return uid.isalpha


def verify_repeat(uid: str) -> bool:
    set_characs = set(uid)

    return len(set_characs) == len(uid)


def verify_lenght(uid: str) -> bool:
    return len(uid) == 10


def verify_uid(uid: str) -> bool:
    if (
        verify_upper_case(uid)
        and verify_3_digits(uid)
        and verify_alpha(uid)
        and verify_repeat(uid)
        and verify_lenght(uid)
    ):
        return True

    return False


def main() -> None:
    n = int(input())
    for _ in range(n):
        uid = input()

        uid_is_valid = verify_uid(uid)

        if uid_is_valid:
            print("Valid")

        else:
            print("Invalid")


if __name__ == "__main__":
    main()
