from collections import deque

customers = [
    ("John", "normal"),
    ("Alice", "priority"),
    ("David", "normal"),
    ("Bob", "priority")
]

def process_priority_queue(customers):

    priority_queue = deque()
    normal_queue = deque()

    for name, status in customers:

        if status == "priority":
            priority_queue.append((name,status))
        else:
            normal_queue.append((name,status))

    served=[]

    while priority_queue:
        served.append(priority_queue.popleft())
    while normal_queue:
        served.append(normal_queue.popleft())

    return served

print(process_priority_queue(customers))