def main() -> None:
    k = int(input())
    elements = [*map(int, input().split())]

    sum_elements = sum(elements)  # Cap + (k * sum_others)
    sum_set = sum(set(elements))  # Cap + sum_others

    cap = int(((sum_set * k) - sum_elements) / (k - 1))

    print(cap)


if __name__ == "__main__":
    main()
