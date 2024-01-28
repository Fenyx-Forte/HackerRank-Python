def verify_if_string_has_alphanumeric_characters(string: str) -> bool:
    output = False
    for charac in string:
        if charac.isalnum():
            output = True
            break

    return output


def verify_if_string_has_alphabetical_characters(string: str) -> bool:
    output = False
    for charac in string:
        if charac.isalpha():
            output = True
            break

    return output


def verify_if_string_has_digits(string: str) -> bool:
    output = False
    for charac in string:
        if charac.isdigit():
            output = True
            break

    return output


def verify_if_string_has_lowercase_characters(string: str) -> bool:
    output = False
    for charac in string:
        if charac.islower():
            output = True
            break

    return output


def verify_if_string_has_uppercase_characters(string: str) -> bool:
    output = False
    for charac in string:
        if charac.isupper():
            output = True
            break

    return output


def main() -> None:
    string = input()

    print(verify_if_string_has_alphanumeric_characters(string))
    print(verify_if_string_has_alphabetical_characters(string))
    print(verify_if_string_has_digits(string))
    print(verify_if_string_has_lowercase_characters(string))
    print(verify_if_string_has_uppercase_characters(string))


if __name__ == "__main__":
    main()
