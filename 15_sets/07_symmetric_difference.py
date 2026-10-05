python_students = {"Alice", "Bob", "David"}
java_students = {"Bob", "John", "David"}

def get_unique_students(python_students, java_students):
    unique_students = python_students ^ java_students
    return unique_students

print(get_unique_students(python_students, java_students))