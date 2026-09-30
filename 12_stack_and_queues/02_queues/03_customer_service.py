from collections import deque

customers = [
    ("John", 2),
    ("Alice", 1),
    ("David", 3),
    ("Bob", 2)
]

def process_customers(customers):

    queue = deque()

    for name, time in customers:
        queue.append((name,time))

    served=[]
    total_time =0


    while queue:
        name, time = queue.popleft()
        served.append(name)
        total_time += time

    return served, total_time

print(process_customers(customers))