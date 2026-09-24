def add(*args):
    total = 0

    for number in args:
        total += number

    return total


print(add(10, 20))
print(add(10, 20, 30, 40))