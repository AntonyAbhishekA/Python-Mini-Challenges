numbers = (10, 25, 5, 40, 15)

def analyze_numbers(numbers):
    minimum=numbers[0]
    maximum=numbers[0]
    total=0

    for number in numbers:
        if maximum<number:
            maximum=number
        if minimum>number:
            minimum=number
        total+=number
    return (minimum, maximum,total)

print(analyze_numbers(numbers))