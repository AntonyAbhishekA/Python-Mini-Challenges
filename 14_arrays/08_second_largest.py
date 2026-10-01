from array import array

numbers = array("i", [10, 25, 5, 40, 30])

def second_largest(numbers):
    largest = 0
    second_largest = 0

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    return second_largest

print(second_largest(numbers))