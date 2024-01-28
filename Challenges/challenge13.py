if __name__ == "__main__":
    n: int = int(input())

    t: tuple[int] = tuple((int(num) for num in input().split()))

    print(hash(t))
