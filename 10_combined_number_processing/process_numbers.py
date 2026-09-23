numbers = [3, 10, 7, 20, 15, 2, 8]


def process_numbers(numbers):
    result = [x ** 2 for x in numbers if x > 5]
    result.sort(reverse=True)
    return result


print(process_numbers(numbers))
# Output: [400, 225, 100, 64, 49]
