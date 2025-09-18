# AI Features for Ecommerce

# 1. Product Recommendations (using simple content-based filtering)
def recommend_products(user_profile, products, top_n=5):
    """
    Recommend products based on user profile interests.
    user_profile: dict with user interests (e.g., categories)
    products: list of dicts with product info
    """
    recommended = []
    for product in products:
        if product['category'] in user_profile['interests']:
            recommended.append(product)
    return recommended[:top_n]

# 2. Customer Support Chatbot (simple rule-based)
def chatbot_response(user_message):
    """
    Basic rule-based chatbot for customer support.
    """
    user_message = user_message.lower()
    if "order status" in user_message:
        return "Please provide your order ID to check the status."
    elif "refund" in user_message:
        return "To process a refund, please share your order details."
    elif "hello" in user_message or "hi" in user_message:
        return "Hello! How can I assist you today?"
    else:
        return "I'm here to help! Please tell me your query."

# 3. Sales Forecasting (dummy linear trend)
def forecast_sales(sales_history, periods=3):
    """
    Forecast future sales using a simple linear trend.
    sales_history: list of past sales numbers
    periods: number of future periods to forecast
    """
    if len(sales_history) < 2:
        return [sales_history[-1]] * periods
    trend = sales_history[-1] - sales_history[-2]
    forecast = []
    last = sales_history[-1]
    for _ in range(periods):
        last += trend
        forecast.append(last)
    return forecast

# 4. Inventory Management (simple reorder alert)
def check_inventory(inventory, reorder_level=10):
    """
    Check inventory and alert for items below reorder level.
    inventory: dict of {product_id: quantity}
    """
    low_stock = {pid: qty for pid, qty in inventory.items() if qty < reorder_level}
    return low_stock

# 5. Personalized Marketing (basic email content generator)
def generate_marketing_email(user_name, recommended_products):
    """
    Generate a personalized marketing email.
    """
    product_list = "\n".join([f"- {p['name']}" for p in recommended_products])
    email = (
        f"Hi {user_name},\n\n"
        "Based on your interests, we thought you might like these products:\n"
        f"{product_list}\n\n"
        "Happy shopping!\nYour Ecommerce Team"
    )
    return email

# Example usage (for testing)
if __name__ == "__main__":
    user_profile = {'interests': ['electronics', 'books']}
    products = [
        {'name': 'Smartphone', 'category': 'electronics'},
        {'name': 'Novel', 'category': 'books'},
        {'name': 'T-shirt', 'category': 'clothing'},
    ]
    inventory = {'Smartphone': 5, 'Novel': 15, 'T-shirt': 8}
    sales_history = [100, 120, 130]

    recs = recommend_products(user_profile, products)
    print("Recommended Products:", recs)
    print("Chatbot:", chatbot_response("Hi, I want to know my order status"))
    print("Sales Forecast:", forecast_sales(sales_history))
    print("Low Inventory:", check_inventory(inventory))
    print("Marketing Email:\n", generate_marketing_email("Avinash", recs))

