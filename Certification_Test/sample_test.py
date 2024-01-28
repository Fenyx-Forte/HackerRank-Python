def test_fizz_buzz(n: int) -> str:
    if (n % 3 == 0) and (n % 5 == 0):
        return "FizzBuzz"

    if (n % 3 == 0) and (n % 5 != 0):
        return "Fizz"

    if (n % 3 != 0) and (n % 5 == 0):
        return "Buzz"

    return str(n)


def fizzBuzz(n: int) -> None:
    for i in range(1, n + 1):
        print(test_fizz_buzz(i))


if __name__ == "__main__":
    n = int(input().strip())

    fizzBuzz(n)
