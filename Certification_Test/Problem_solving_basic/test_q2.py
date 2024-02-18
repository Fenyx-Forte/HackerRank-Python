def longestSubarray(arr: list[int]) -> int:
    len_arr = len(arr)

    len_longest = 1

    for i in range(len_arr):
        len_sub_arr = 1
        first_value = arr[i]

        set_values = set()
        set_values.add(first_value)

        for j in range(i + 1, len_arr):
            if abs(first_value - arr[j]) <= 1:
                set_values.add(arr[j])
                if len(set_values) > 2:
                    break
                else:
                    len_sub_arr += 1

            else:
                break

        if len_sub_arr > len_longest:
            len_longest = len_sub_arr

    return len_longest


def main() -> None:
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    print(result)


if __name__ == "__main__":
    main()
