names = ["John", "Alice", "David", "Bob"]
marks = [75, 92, 68, 85]

def get_student_status(names, marks):
    return [
        f"{name}: {'Pass' if mark >= 70 else 'Fail'}"
            for name, mark in zip(names, marks)]
print(get_student_status(names, marks))