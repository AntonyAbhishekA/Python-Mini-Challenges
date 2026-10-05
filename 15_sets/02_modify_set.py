fruits = {"apple", "banana", "orange"}

def modify_set(fruits):
    fruits.add("mango")
    fruits.remove("banana")
    return fruits

print(modify_set(fruits))