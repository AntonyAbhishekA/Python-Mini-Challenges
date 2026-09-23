students = [
    {"name": "John", "marks": 75},
    {"name": "Alice", "marks": 92},
    {"name": "David", "marks": 68},
    {"name": "Bob", "marks": 85}
]


def get_passing_students(students):
    return list(
        filter(
            lambda student: student["marks"] >= 75,
            students
        )
    )


print(get_passing_students(students))
