numbers = (15, 4, 27, 8, 19)

def get_min_max(numbers):
    minimum=numbers[0]
    maximum=numbers[0]

    for number in numbers:
        if maximum<number:
            maximum=number
        if minimum>number:
            minimum=number
    return (minimum, maximum)

print(get_min_max(numbers))