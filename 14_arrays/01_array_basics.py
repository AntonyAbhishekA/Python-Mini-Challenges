from array import array

numbers = array("i", [1, 2, 3, 4, 5])

def display_array(numbers):
    print("First:", numbers[0])
    print("Last:", numbers[-1])
    print("Length:", len(numbers))
    for number in numbers:
        print(number)
    return numbers

print(display_array(numbers))