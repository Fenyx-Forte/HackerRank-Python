if __name__ == "__main__":
    n: int = int(input())
    score_list: list[int] = [int(score) for score in input().split()]

    max_score: int = max(score_list)

    second_high_score: int = -101

    for score in score_list:
        if score > second_high_score and score < max_score:
            second_high_score = score

    print(second_high_score)
