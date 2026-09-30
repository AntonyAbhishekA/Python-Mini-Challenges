from collections import deque

customers = ["John", "Alice", "David", "Bob"]

def process_queue(customers):

    queue = deque()

    for customer in customers:
        queue.append(customer)

    served=[]

    while queue:
        served.append(queue.popleft())

    return served

print(process_queue(customers))