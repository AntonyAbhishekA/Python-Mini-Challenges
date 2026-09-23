def get_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(get_even_numbers(numbers))
# Output: [2, 4, 6, 8]
