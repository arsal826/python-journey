orders = [
    {"id": "F001", "customer": "Ali",   "restaurant": "KFC",    "items": 2, "price": 500},
    {"id": "F002", "customer": "Sara",  "restaurant": "McD",    "items": 1, "price": 700},
    {"id": "F003", "customer": "Ali",   "restaurant": "KFC",    "items": 3, "price": 500},
    {"id": "F004", "customer": "Ahmed", "restaurant": "PizzaHut","items": 2, "price": 800},
    {"id": "F005", "customer": "Sara",  "restaurant": "KFC",    "items": 1, "price": 500},
    {"id": "F006", "customer": "Ali",   "restaurant": "McD",    "items": 2, "price": 700},
]

coustomer_data = {}
popular_restaurant = {}
highest_revenue_restaurant = {}
for order in orders:
    customer = order["customer"]
    restaurant = order["restaurant"]
    items = order["items"]
    price = order["price"]
    total_price = items * price

    if customer not in coustomer_data:
        coustomer_data[customer] = {
            "orders": [],
            "total_spent": 0,
            "total_items": 0,
            "most_orders_restaurant": ("", 0),
            "most_spent_restaurant": ("", 0),
            "highest_single_order": 0,
            "lowest_single_order": float('inf'),

            # ✅ FIX 1: Proper structure (no nesting restaurant inside restaurant)
            "restaurant_counts": {},
            "restaurant_spending": {}
        }

    coustomer_data[customer]["orders"].append(order)
    coustomer_data[customer]["total_spent"] += total_price
    coustomer_data[customer]["total_items"] += items

    # highest / lowest order logic (correct already)
    if total_price > coustomer_data[customer]["highest_single_order"]:
        coustomer_data[customer]["highest_single_order"] = total_price

    if total_price < coustomer_data[customer]["lowest_single_order"]:
        coustomer_data[customer]["lowest_single_order"] = total_price

    # ✅ FIX 2: Proper dictionary usage (no unnecessary nesting)
    coustomer_data[customer]["restaurant_counts"][restaurant] = \
        coustomer_data[customer]["restaurant_counts"].get(restaurant, 0) + items

    coustomer_data[customer]["restaurant_spending"][restaurant] = \
        coustomer_data[customer]["restaurant_spending"].get(restaurant, 0) + total_price

    # ✅ FIX 3: Correct comparison using updated structure
    if coustomer_data[customer]["restaurant_counts"][restaurant] > coustomer_data[customer]["most_orders_restaurant"][1]:
        coustomer_data[customer]["most_orders_restaurant"] = (
            restaurant,
            coustomer_data[customer]["restaurant_counts"][restaurant]
        )

    if coustomer_data[customer]["restaurant_spending"][restaurant] > coustomer_data[customer]["most_spent_restaurant"][1]:
        coustomer_data[customer]["most_spent_restaurant"] = (
            restaurant,
            coustomer_data[customer]["restaurant_spending"][restaurant]
        )

    # global tracking
    if restaurant not in popular_restaurant:
        popular_restaurant[restaurant] = 0

    if restaurant not in highest_revenue_restaurant:
        highest_revenue_restaurant[restaurant] = 0

    # ✅ FIX 4: Use items (not +1) → correct metric
    popular_restaurant[restaurant] += items

    # correct already
    highest_revenue_restaurant[restaurant] += total_price


# final calculations
coustomer_order_most_items = max(coustomer_data, key=lambda x: coustomer_data[x]["total_items"])
coustomer_spent_most = max(coustomer_data, key=lambda x: coustomer_data[x]["total_spent"])
most_popular_restaurant = max(popular_restaurant, key=popular_restaurant.get)
highest_revenue = max(highest_revenue_restaurant, key=highest_revenue_restaurant.get)

print("\nCustomer Details:")
for customer, data in coustomer_data.items():
    print(f"\nCustomer: {customer}")
    print(f"Orders:")
    for order in data["orders"]:
        print(f"  - ID: {order['id']}, Restaurant: {order['restaurant']}, Items: {order['items']}, Price: {order['price']}")
    print(f"Total Spent: {data['total_spent']}")
    print(f"Total Items: {data['total_items']}")
    print(f"Most Orders Restaurant: {data['most_orders_restaurant'][0]} ({data['most_orders_restaurant'][1]} orders)")
    print(f"Most Spent Restaurant: {data['most_spent_restaurant'][0]} (Spent: {data['most_spent_restaurant'][1]})")
    print(f"Highest Single Order: {data['highest_single_order']}")
    print(f"Lowest Single Order: {data['lowest_single_order']}")
print(f"\nCustomer with Most Items Ordered: {coustomer_order_most_items} (Total Items: {coustomer_data[coustomer_order_most_items]['total_items']})")
print(f"Customer Who Spent Most: {coustomer_spent_most} (Total Spent: {coustomer_data[coustomer_spent_most]['total_spent']})")
print(f"Most Popular Restaurant: {most_popular_restaurant} (Total Orders: {popular_restaurant[most_popular_restaurant]})")
print(f"Restaurant with Highest Revenue: {highest_revenue} (Total Revenue: {highest_revenue_restaurant[highest_revenue]})")
