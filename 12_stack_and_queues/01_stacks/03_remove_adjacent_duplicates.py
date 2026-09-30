text = "abbaca"
def remove_duplicates(text):
    stack=[]
    for i in text:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)

print(remove_duplicates(text))