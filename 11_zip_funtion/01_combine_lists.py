names = ["John", "Alice", "David", "Bob"]
ages = [21, 22, 20, 23]

def combine_data(names, ages):
    return list(zip(names, ages))
print(combine_data(names, ages))