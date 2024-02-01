def main() -> None:
    n = int(input())

    set_int = set(map(int, input().split()))

    num_commands = int(input())

    for _ in range(num_commands):
        command = input().split()
        len_command = len(command)

        match len_command:
            case 1:
                set_int.pop()

            case _:
                function = command[0]
                arg = int(command[1])
                set_int.__getattribute__(function)(arg)

    print(sum(set_int))


if __name__ == "__main__":
    main()
