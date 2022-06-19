def shopping_list(budget, **kwargs):
    products_data = []
    if budget < 100:
        return "You do not have enough budget."
    else:
        for product in kwargs:
            if len(kwargs) == 0:
                break
            price_per_each = kwargs[product][0]
            quantity = kwargs[product][1]
            price = price_per_each * quantity
            if price <= budget:
                element = f"You bought {product} for {price:.2f} leva."
                products_data.append(element)
                budget -= price
            if len(products_data) == 5:
                break
        return "\n".join(products_data)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
