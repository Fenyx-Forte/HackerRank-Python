import cmath


def main() -> None:
    complex_number = complex(input())
    print(abs(complex_number))
    print(cmath.phase(complex_number))


if __name__ == "__main__":
    main()
