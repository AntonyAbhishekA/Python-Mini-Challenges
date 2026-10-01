from array import array

numbers = array("i", [10, 25, 30, 45, 50])

def search_array(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

print(search_array(numbers, 30))