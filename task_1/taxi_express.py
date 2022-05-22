from collections import deque

# take first customer
customers = deque([int(x) for x in input().split(", ")])

# take last car
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxis:
    customer = customers[0]
    car = taxis[-1]
    if car >= customer:
        total_time += customer
        customers.popleft()
        taxis.pop()
    elif car < customer:
        taxis.pop()

if len(customers) > 0:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
elif len(customers) == 0:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")