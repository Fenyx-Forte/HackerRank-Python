def main() -> None:
    row = input().split()
    n = int(row[0])
    x = int(row[1])

    marks_total = []
    for _ in range(x):
        marks = list(map(float, input().split()))
        marks_total.append(marks)

    for i in range(n):
        sum_marks = 0
        for j in range(x):
            sum_marks += marks_total[j][i]

        average = round(sum_marks / x, 1)
        print(average)


if __name__ == "__main__":
    main()
