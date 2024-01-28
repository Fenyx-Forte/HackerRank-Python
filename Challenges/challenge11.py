if __name__ == "__main__":
    n: int = int(input())

    student_marks: dict["str":"list[float]"] = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name: str = input()

    media: float = sum(student_marks[query_name]) / 3

    print("{:.2f}".format(media))
