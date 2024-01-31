from collections import namedtuple


def main() -> None:
    n = int(input())
    columns = [*input().split()]

    marks_position: int = None
    for i in range(len(columns)):
        if columns[i] == "MARKS":
            marks_position = i
            break

    sum_notes = 0
    for _ in range(n):
        row = [*input().split()]
        note = int(row[marks_position])
        sum_notes += note

    average_notes = float(sum_notes) / float(n)
    print("{:.2f}".format(average_notes))


if __name__ == "__main__":
    main()
