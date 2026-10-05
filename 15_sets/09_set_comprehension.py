numbers = {5, 10, 15, 20, 25, 30, 35}

def get_squares_of_even(numbers):
    return {num ** 2 for num in numbers if num % 2 == 0}

print(get_squares_of_even(numbers))