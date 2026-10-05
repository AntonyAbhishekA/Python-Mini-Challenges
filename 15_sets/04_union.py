python_students = {"Alice", "Bob", "David"}
java_students = {"Bob", "John", "David"}

def get_all_students(python_students, java_students):
    all_students = python_students | java_students
    return all_students

print(get_all_students(python_students, java_students))