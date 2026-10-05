numbers = {5, 10, 15, 20, 25, 30, 35}

def get_even_numbers(numbers):
    even_numbers = set()
    for num in numbers:
        if num % 2 ==0:
            even_numbers.add(num)
    return even_numbers

print(get_even_numbers(numbers))