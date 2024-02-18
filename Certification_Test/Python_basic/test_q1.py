def avg(*args) -> float:
    num_args = len(args)
    sum_args = sum(args)
    avg_args = float(sum_args / num_args)

    return avg_args


def main():
    nums = list(map(int, input().split()))
    res = avg(*nums)

    print("%.2f" % res + "\n")


if __name__ == "__main__":
    main()
