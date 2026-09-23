def find_min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

        if number > maximum:
            maximum = number

    return [minimum, maximum]


numbers = [25, 10, 40, 5, 30]

print(find_min_max(numbers))
# Output: [5, 40]
