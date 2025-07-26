import pandas as pd

# Load data once
products = pd.read_csv("data/products.csv")
inventory = pd.read_csv("data/inventory_items.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")

def handle_query(query):
    query = query.lower()

    if "top" in query and "sold" in query:
        top_products = (
            inventory.dropna(subset=["sold_at"])
            .groupby("product_name")
            .size()
            .sort_values(ascending=False)
            .head(5)
        )
        return top_products.to_string()

    elif "status of order" in query:
        import re
        match = re.search(r"order id (\d+)", query)
        if match:
            order_id = int(match.group(1))
            order = orders[orders["order_id"] == order_id]
            if not order.empty:
                return order[["status", "delivered_at", "returned_at"]].to_dict(orient="records")
            else:
                return "Order not found."

    elif "how many" in query and "left in stock" in query:
        match = re.search(r"how many (.+?) are left", query)
        if match:
            product_name = match.group(1).strip().title()
            unsold = inventory[inventory["sold_at"].isna()]
            count = unsold[unsold["product_name"] == product_name].shape[0]
            return f"{count} units of {product_name} are left in stock."
    
    return "Sorry, I didn't understand that."

