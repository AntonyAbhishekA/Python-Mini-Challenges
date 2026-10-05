numbers = [10, 20, 10, 30, 20, 40, 30]

def remove_duplicates(numbers):
    unique=set()
    for num in numbers:
        if num not in unique:
            unique.add(num)
    return unique

print(remove_duplicates(numbers))