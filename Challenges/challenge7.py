def print_function(n: int) -> None:
    string_list: list[str] = (str(i) for i in range(1, n + 1))
    print("".join(string_list))


if __name__ == "__main__":
    n: int = int(input())
    print_function(n)
