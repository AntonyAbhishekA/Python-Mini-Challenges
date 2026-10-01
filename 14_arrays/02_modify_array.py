from array import array

numbers = array("i", [10, 20, 30, 40])

def modify_array(numbers):
    numbers.append(50)
    numbers.insert(1, 15)
    numbers.remove(30)

    return numbers

print(modify_array(numbers))