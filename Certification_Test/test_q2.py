def reverse_words_order_and_swap_cases(sentence: str) -> str:
    list_carac: list[str] = []
    for carac in sentence:
        if carac.isupper():
            list_carac.append(carac.lower())
        else:
            list_carac.append(carac.upper())

    sentence_swap_case: str = "".join(list_carac)

    list_words_swap_case: list[str] = sentence_swap_case.split()

    list_words_swap_case.reverse()

    output = " ".join(list_words_swap_case)

    return output


if __name__ == "__main__":
    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    print(result)
