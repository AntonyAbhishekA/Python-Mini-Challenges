numbers = (10, 20, 30, 40, 50)
result=[]
for number in numbers:
    result.append(number)
result[0],result[-1]=result[-1],result[0]
print(tuple(result))

numbers = (10, 20, 30, 40, 50)
first,*middle,last=numbers
result=(last,*middle,first)

print(result)