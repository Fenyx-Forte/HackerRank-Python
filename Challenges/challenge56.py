def main() -> None:
    t = int(input())

    for _ in range(t):
        row = input().split()

        try:
            a = int(row[0])
            b = int(row[1])

            print(a // b)

        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")

        except ValueError as e:
            print("Error Code:", e)


if __name__ == "__main__":
    main()
