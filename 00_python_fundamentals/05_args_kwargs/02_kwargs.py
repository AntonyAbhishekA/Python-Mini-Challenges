def student_info(**student):
    for key, value in student.items():
        print(f"{key}: {value}")


student_info(
    name="Antony",
    age=23,
    course="MCA"
)