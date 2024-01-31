from collections import OrderedDict


def main() -> None:
    n = int(input())

    ord_dict = OrderedDict()

    for _ in range(n):
        row = input().split()
        product_name = " ".join(row[:-1])
        net_price = int(row[-1])

        if product_name in ord_dict:
            ord_dict[product_name] += net_price

        else:
            ord_dict[product_name] = net_price

    for key, value in ord_dict.items():
        print(key, value)


if __name__ == "__main__":
    main()
