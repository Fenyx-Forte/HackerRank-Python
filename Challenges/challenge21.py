import textwrap


def wrap(string: str, max_width: int) -> str:
    list_wrap = textwrap.wrap(string, max_width)

    string_wrapped = "\n".join(list_wrap)

    return string_wrapped


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
