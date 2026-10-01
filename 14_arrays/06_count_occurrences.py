from array import array

numbers = array("i", [10, 20, 10, 30, 10, 40, 20])

def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count+= 1
    return count

print(count_occurrences(numbers, 10))