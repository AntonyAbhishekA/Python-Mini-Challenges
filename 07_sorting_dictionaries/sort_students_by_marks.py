students = [
    {"name": "John", "marks": 75},
    {"name": "Alice", "marks": 92},
    {"name": "David", "marks": 68},
    {"name": "Bob", "marks": 85}
]


def sort_students(students):
    return sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )


print(sort_students(students))
