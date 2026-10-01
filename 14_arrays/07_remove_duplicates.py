from array import array

numbers = array("i", [10, 20, 10, 30, 20, 40, 30])

def remove_duplicates(numbers):
    result=array("i", [])
    for number in numbers:
        if number not in result:
            result.append(number)
    return result

print(remove_duplicates(numbers))