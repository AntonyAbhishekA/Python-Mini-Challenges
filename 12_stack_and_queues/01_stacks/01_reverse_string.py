text="python"
def reverse_string(text):
    stack=[]
    result=""
    for i in text:
        stack.append(i)
    while stack:
        character = stack.pop()
        result += character
    return result
print(reverse_string(text))