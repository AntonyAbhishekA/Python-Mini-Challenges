students = [
    {"name": "John", "marks": 75},
    {"name": "Alice", "marks": 92},
    {"name": "David", "marks": 68},
    {"name": "Bob", "marks": 85}
]


def get_top_students(students):
    filtered_students = list(
        filter(
            lambda student: student["marks"] >= 75,
            students
        )
    )

    return sorted(
        filtered_students,
        key=lambda student: student["marks"],
        reverse=True
    )


print(get_top_students(students))
