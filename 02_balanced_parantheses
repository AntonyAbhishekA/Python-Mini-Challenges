text="(())"
def is_balanced(text):
    stack=[]
    for i in text:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

print(is_balanced(text))