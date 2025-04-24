"""
Approach:

1. Sort inventory by price per unit.
2. Try fulfilling as much of the order as possible within the budget.
3. Track how much of the order was fulfilled.
"""

def match_order(inventory, order_quantity, budget):
    inventory.sort(key=lambda x: x['price'])
    remaining_quantity = order_quantity
    total_cost = 0
    fulfillment = []

    for item in inventory:
        if remaining_quantity == 0:
            break
        take_quantity = min(item['quantity'], remaining_quantity)
        cost = take_quantity * item['price']
        if total_cost + cost > budget:
            max_affordable = (budget - total_cost) // item['price']
            if max_affordable > 0:
                fulfillment.append({'item': item['name'], 'quantity': max_affordable, 'price': item['price']})
                total_cost += max_affordable * item['price']
                remaining_quantity -= max_affordable
            break
        fulfillment.append({'item': item['name'], 'quantity': take_quantity, 'price': item['price']})
        total_cost += cost
        remaining_quantity -= take_quantity

    if remaining_quantity == 0:
        status = "Order is fully fulfillable"
    elif fulfillment:
        status = "Order is partially fulfillable"
    else:
        status = "Order is not fulfillable"

    return status, fulfillment, total_cost

# Example usage
inventory_list = [
    {'name': 'Product A', 'quantity': 10, 'price': 5},
    {'name': 'Product B', 'quantity': 5, 'price': 3},
    {'name': 'Product C', 'quantity': 20, 'price': 8},
]

order_qty = 12
customer_budget = 50

status, fulfillment_details, final_cost = match_order(inventory_list, order_qty, customer_budget)

print(status)
for item in fulfillment_details:
    print(f"{item['quantity']} of {item['item']} @ ₹{item['price']} each")
print(f"Total cost: ₹{final_cost}")
