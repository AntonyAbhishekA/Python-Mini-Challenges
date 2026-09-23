def second_largest(numbers):
    maximum = numbers[0]
    second_max = numbers[0]

    for number in numbers:
        if number > maximum:
            second_max = maximum
            maximum = number
        elif number > second_max and number != maximum:
            second_max = number

    return second_max


numbers = [10, 25, 5, 40, 30]

print(second_largest(numbers))
# Output: 30
