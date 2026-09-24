names = ["John", "Alice", "David", "Bob", "Emma"]
marks = [75, 92, 68, 85, 55]

def get_passing_students(names, marks):
    return [
        (name, mark)
        for name, mark in zip(names, marks)
        if mark >= 70
    ]
print(get_passing_students(names,marks))