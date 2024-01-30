def average(array: list[int]) -> float:
    set_array = set(array)
    result = float(sum(set_array) / len(set_array))
    return round(result, 3)


def main() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


if __name__ == "__main__":
    main()
