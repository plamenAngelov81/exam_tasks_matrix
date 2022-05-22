from collections import deque

ramen = [int(y) for y in input().split(", ")]
queue_customers = deque([int(x) for x in input().split(", ")])


while queue_customers and ramen:
    current_ramen = ramen[-1]
    current_customer = queue_customers[0]
    if current_ramen == current_customer:
        ramen.pop()
        queue_customers.popleft()

    elif current_ramen > current_customer:
        ramen[-1] -= current_customer
        queue_customers.popleft()

    elif current_ramen < current_customer:
        queue_customers[0] -= current_ramen
        ramen.pop()

if len(queue_customers) == 0:
    print("Great job! You served all the customers.")
elif len(ramen) == 0:
    print("Out of ramen! You didn't manage to serve all customers.")

if ramen:
    print(f"Bowls of ramen left: {', '.join(map(str, ramen))}")

if queue_customers:
    print(f"Customers left: {', '.join(map(str, queue_customers))}")
