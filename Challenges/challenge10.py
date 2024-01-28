def kept_only_students_with_second_lowest_grade(
    list_students: list[list[str | int]],
) -> list[str]:
    list_of_grades: list[float] = [student[1] for student in list_students]
    min_grade = min(list_of_grades)

    second_lowest_grade: float = 1000.0
    for grade in list_of_grades:
        if grade < second_lowest_grade and grade > min_grade:
            second_lowest_grade = grade

    list_names: list[str] = []
    for student in list_students:
        if student[1] == second_lowest_grade:
            list_names.append(student[0])

    return list_names


if __name__ == "__main__":
    number_of_students: int = int(input())

    list_students = []
    for student in range(number_of_students):
        name = input()
        score = float(input())

        list_students.append([name, score])

    list_names = kept_only_students_with_second_lowest_grade(list_students)

    list_names_ordered = sorted(list_names)

    print(*list_names_ordered, sep="\n")
