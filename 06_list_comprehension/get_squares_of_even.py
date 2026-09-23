def get_squares_of_even(numbers):
    return [x ** 2 for x in numbers if x % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6]

print(get_squares_of_even(numbers))
# Output: [4, 16, 36]
