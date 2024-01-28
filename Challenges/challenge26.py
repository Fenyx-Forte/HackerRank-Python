def minion_game(string: str) -> None:
    kevin_score = 0
    stuart_score = 0
    len_string = len(string)
    vowels = "AEIOU"

    for i in range(len_string):
        if string[i] in vowels:
            kevin_score += len_string - i

        else:
            stuart_score += len_string - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)

    elif kevin_score == stuart_score:
        print("Draw")

    else:
        print("Stuart", stuart_score)


def main() -> None:
    s = input()
    minion_game(s)


if __name__ == "__main__":
    main()
