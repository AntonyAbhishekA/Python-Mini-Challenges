def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))


numbers = [2, 4, 6, 8]

print(square_numbers(numbers))
# Output: [4, 16, 36, 64]
