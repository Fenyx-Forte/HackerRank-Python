from collections import Counter


def main() -> None:
    x = int(input())
    shoe_sizes = Counter(map(int, input().split()))

    n = int(input())
    list_list = [list(map(int, input().split())) for _ in range(n)]

    money_earned = 0

    for i in range(n):
        size, price = list_list[i]
        if shoe_sizes[size] > 0:
            shoe_sizes.update({size: -1})
            money_earned += price

    print(money_earned)


if __name__ == "__main__":
    main()
