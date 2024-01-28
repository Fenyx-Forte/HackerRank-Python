if __name__ == "__main__":
    n: int = int(input().strip())
    output: str = ""
    if n % 2 == 1:
        output = "Weird"
    elif n <= 5:
        output = "Not Weird"
    elif n <= 20:
        output = "Weird"
    else:
        output = "Not Weird"

    print(output)
