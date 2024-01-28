def is_leap(year: int) -> bool:
    if year % 4 != 0:
        return False

    if year % 400 == 0:
        return True

    if year % 25 == 0:
        return False

    return True


if __name__ == "__main__":
    year: int = int(input())
    print(is_leap(year))
