if __name__ == "__main__":
    list_: list[int] = []

    input_list: list[str] = []

    n: int = int(input())

    for _ in range(n):
        command: str = input()
        input_list.append(command)

    for input in input_list:
        args = input.split()
        command = args[0]
        num_args = len(args)

        index: int
        element: int

        match num_args:
            case 2:
                element = int(args[1])

            case 3:
                index = int(args[1])
                element = int(args[2])

        match command:
            case "insert":
                list_.insert(index, element)

            case "print":
                print(list_)

            case "remove":
                list_.remove(element)

            case "append":
                list_.append(element)

            case "sort":
                list_.sort()

            case "pop":
                list_.pop()

            case default:
                list_.reverse()
