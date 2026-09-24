names = ["John", "Alice", "David", "Bob"]
marks = [75, 92, 68, 85]

def create_student_dict(names, marks):
    return dict(zip(names, marks))
print(create_student_dict(names, marks))