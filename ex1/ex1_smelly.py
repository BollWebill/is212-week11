class OrderProcessor:
    
    def check_order(self, order):
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")
    
        return True
    
    def calculate_discount(self, order):
        if order.get("discount_code") == "SUMMER20":
            discount = 0.8
        elif order.get("discount_code") == "WELCOME10":
            discount = 0.9
        else:
            discount = 1
    
    def calculate_total_price(self, order, discount):
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]
        
        total_price *= discount
        return total_price
    
    
    def update_inventory(self, order):
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")
    
    def generate_receipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

        return receipt
    
    #helper function
    
    def process_order(self, order):
        self.check_order(order)
        discount = self.calculate_discount(order)
        total_price = self.calculate_total_price(order, discount)
        self.update_inventory(order)
        receipt = self.generate_receipt(order, total_price)
        
        return receipt