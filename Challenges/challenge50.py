import math


def main() -> None:
    len_ab = int(input())
    len_bc = int(input())

    angle_mbc = math.degrees(math.atan(len_bc / len_ab))
    result = int(round(90 - angle_mbc, 0))
    print(f"{result}\u00b0")


if __name__ == "__main__":
    main()
