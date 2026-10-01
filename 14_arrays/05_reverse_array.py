from array import array

numbers = array("i", [10, 20, 30, 40, 50])

def reverse_array(numbers):
    for i in range(len(numbers) // 2):
        numbers[i], numbers[-(i+1)] = numbers[-(i+1)], numbers[i]
    return numbers

print(reverse_array(numbers))