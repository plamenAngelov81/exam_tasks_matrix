def stock_availability(item, command, *args):
    store_list = item

    if command == "delivery":
        delivery_items = args
        store_list.extend(delivery_items)
    if command == "sell":
        if len(args) == 0:
            store_list.pop(0)
        elif str(args[0]).isdigit():
            step = int(args[0])
            if step < len(store_list):
                for i in range(step):
                    store_list.pop(0)
            else:
                store_list.clear()
        else:
            orders = args

            for order in orders:
                if order in store_list:
                    left_items = []
                    for j in store_list:
                        if j != order:
                            left_items.append(j)
                    store_list = left_items
    return store_list


print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
