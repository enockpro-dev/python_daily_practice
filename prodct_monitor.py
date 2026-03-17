num_products = int(input("Enter number of products: "))
products = []
for i in range(num_products):
    name = input("Enter product name: ")
    stock = int(input("Enter stock: "))
    price = float(input("Enter price: "))
    cost = float(input("Enter cost: "))
    expiry_days = int(input("Enter expiry days: "))
    products.append({"name": name, "stock": stock, "sold": 0, "price": price, "cost": cost, "expiry_days": expiry_days})

# Simulate sales over 6 days
for day in range(1, 7):
    print(f"\n--- Day {day} ---")
    for p in products:
        sold_today = int(input(f"How many {p['name']} sold today? "))
        p["sold"] += sold_today
    # Decrement expiry days
    for p in products:
        p["expiry_days"] -= 1

most_sold = None
least_sold = None
most_profit = None
least_profit = None

for p in products:
    remaining = p["stock"] - p["sold"]
    profit = (p["price"] - p["cost"]) * p["sold"]

    print("\nProduct:", p["name"])
    print("Remaining:", remaining)
    print("Profit:", profit)

    # Expiry check
    if p["expiry_days"] <= 3:
        print("⚠️ Expiring soon!")

    # Most / Least sold
    if most_sold is None or p["sold"] > most_sold["sold"]:
        most_sold = p

    if least_sold is None or p["sold"] < least_sold["sold"]:
        least_sold = p

    # Most / Least profit
    if most_profit is None or profit > (most_profit["price"] - most_profit["cost"]) * most_profit["sold"]:
        most_profit = p

    if least_profit is None or profit < (least_profit["price"] - least_profit["cost"]) * least_profit["sold"]:
        least_profit = p

# Summary
print("\n--- WEEKLY REPORT ---")
print("Most Sold:", most_sold["name"])
print("Least Sold:", least_sold["name"])
print("Most Profitable:", most_profit["name"])
print("Least Profitable:", least_profit["name"])

# Recommendation
print("\n--- RECOMMENDATION ---")
for p in products:
    remaining = p["stock"] - p["sold"]

    if remaining < 20:
        print("Order more:", p["name"])
    elif p["expiry_days"] <= 3:
        print("Reduce order (expiring):", p["name"])