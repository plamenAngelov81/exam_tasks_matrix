from collections import deque

pizzas_orders = deque(map(int, input().split(", ")))
employees = input().split(", ")

completed_orders = 0

while pizzas_orders and employees:
    if len(employees) == 0:
        break
    pizzas = pizzas_orders[0]
    employee_power = int(employees[-1])
    if 0 < pizzas <= 10:
        if pizzas <= employee_power:
            completed_orders += pizzas
            pizzas_orders.popleft()
            employees.pop()
        elif pizzas > employee_power:
            pizzas_orders[0] = pizzas - employee_power
            completed_orders += employee_power
            employees.pop()
    else:
        pizzas_orders.popleft()

if len(pizzas_orders) == 0:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {completed_orders}")
    print(f"Employees: {', '.join(map(str, employees))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizzas_orders))}")
