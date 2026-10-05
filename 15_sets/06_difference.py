python_students = {"Alice", "Bob", "David"}
java_students = {"Bob", "John", "David"}

def get_python_only(python_students, java_students):
    python_only = python_students - java_students
    return python_only

print(get_python_only(python_students, java_students))