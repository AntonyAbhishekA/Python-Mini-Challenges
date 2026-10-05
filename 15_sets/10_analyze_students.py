python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Bob", "David", "Eve", "Frank"}

def analyze_students(python_students, java_students):
    both = python_students & java_students
    only_python = python_students - java_students
    only_one_language = python_students ^ java_students
    return both, only_python, only_one_language

both_students, only_python_students, unique_students = analyze_students(python_students, java_students)
print("Both courses:", both_students)
print("Only in Python course:", only_python_students)
print("In only one course:", unique_students)