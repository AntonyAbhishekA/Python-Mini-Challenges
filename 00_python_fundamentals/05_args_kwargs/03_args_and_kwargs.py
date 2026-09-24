def student(name, *marks, **details):
    print(f"Name: {name}")

    for mark in marks:
        print(f"Mark: {mark}")

    total = sum(marks)
    average = total / len(marks)

    print(f"Total: {total}")
    print(f"Average: {average}")

    for key, value in details.items():
        print(f"{key}: {value}")


student(
    "Antony",
    85,
    90,
    78,
    99,
    age=23,
    course="MCA"
)