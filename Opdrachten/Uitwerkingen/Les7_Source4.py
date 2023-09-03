students_per_classroom = {
    "SWDVT-2023-1A": [
        {
            "naam": "Diederik de Vries",
            "resultaten": {
                "WP1": "uitstekend",
                "WP2": "voldoende",
                "WP3": "uitstekend",
                "WP4": "voldoende",
            },
        },
        {
            "naam": "Veysel Altinok",
            "resultaten": {
                "WP1": "goed",
                "WP2": "goed",
                "WP3": "goed",
                "WP4": "goed",
            },
        },
    ],
    "SWDVT-2023-1B": [
        {
            "naam": "Mark Otting",
            "resultaten": {
                "WP1": "onvoldoende",
                "WP2": "voldoende",
                "WP3": "voldoende",
                "WP4": "onvoldoende",
            },
        },
        {
            "naam": "Jelle van der Loo",
            "resultaten": {
                "WP1": "voldoende",
                "WP2": "uitstekend",
                "WP3": "goed",
                "WP4": "voldoende",
            },
        },
    ],
}


def get_is_student_excellent(student):
    excellent = False
    excellent_count = 0
    no_low_grades = True

    for result in student["resultaten"]:
        if student["resultaten"][result] == "uitstekend":
            excellent_count += 1
        if (
            student["resultaten"][result] == "onvoldoende"
            or student["resultaten"][result] == "voldoende"
        ):
            no_low_grades = False

    if no_low_grades or excellent_count > 1:
        excellent = True

    return excellent


def get_excellent_students(students):
    excellent_students = []
    for student in students:
        if get_is_student_excellent(student):
            excellent_students.append(student)
    return excellent_students


def get_most_excellent_classroom(students_per_classroom):
    best_classroom = None
    best_classroom_count = -1
    for classroom in students_per_classroom:
        excellent_students = get_excellent_students(students_per_classroom[classroom])
        if len(excellent_students) > best_classroom_count:
            best_classroom = classroom
            best_classroom_count = len(excellent_students)
        elif len(excellent_students) == best_classroom_count:
            best_classroom = f"{best_classroom}, {classroom}"
    return best_classroom


def calculate_score_per_student(student):
    score = 0
    for result in student["resultaten"]:
        if student["resultaten"][result] == "uitstekend":
            score += 3
        if student["resultaten"][result] == "goed":
            score += 2
        if student["resultaten"][result] == "voldoende":
            score += 1
    return score


def get_best_scoring_classroom(students_per_classroom):
    best_classroom = ""
    best_classroom_score = 0
    for classroom in students_per_classroom:
        classroom_score = 0
        for student in students_per_classroom[classroom]:
            classroom_score += calculate_score_per_student(student)
        if classroom_score > best_classroom_score:
            best_classroom = classroom
            best_classroom_score = classroom_score
        elif classroom_score == best_classroom_score:
            best_classroom = f"{best_classroom}, {classroom}"
    return best_classroom


def get_failed_students(students, min_score=3):
    failed_students = []
    for student in students:
        score = calculate_score_per_student(student)
        if score < min_score:
            student["score"] = score
            failed_students.append(student)
    return failed_students


def full_report(students_per_classroom):
    all_students = []
    for classroom in students_per_classroom:
        for student in students_per_classroom[classroom]:
            all_students.append(student)

    print("----- Report -----")
    print("Excellente studenten:")
    excellent_students = get_excellent_students(all_students)
    for student in excellent_students:
        print(f'\t{student["naam"]}')

    print("Klas met de meeste excellente studenten:")
    best_classroom = get_most_excellent_classroom(students_per_classroom)
    print(f"\t{best_classroom}")

    print("Klas met de hoogste scores gemiddeld:")
    best_classroom = get_best_scoring_classroom(students_per_classroom)
    print(f"\t{best_classroom}")

    print("Studenten met inhaalopdracht:")
    failed_students = get_failed_students(all_students)
    for student in failed_students:
        print(f'\t{student["naam"]}')
        for subject, result in student["resultaten"].items():
            print(f"\t\t{subject}: {result}")


full_report(students_per_classroom)
