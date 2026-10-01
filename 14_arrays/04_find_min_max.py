from array import array

numbers = array("i", [15, 4, 27, 8, 19])

def find_min_max(numbers):
    min_value = numbers[0]
    max_value = numbers[0]

    for number in numbers:
        if number < min_value:
            min_value=number
        if number > max_value:
            max_value=number
    return (min_value, max_value)

print(find_min_max(numbers))