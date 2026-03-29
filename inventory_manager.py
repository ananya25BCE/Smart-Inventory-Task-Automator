import json
import os

class SmartInventory:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_item(self, name, quantity, threshold):
        # Using Boolean Logic to validate input
        if quantity < 0 or threshold < 0:
            print("Error: Values must be positive.")
            return
        
        self.data[name] = {"quantity": quantity, "threshold": threshold}
        self.save_data()
        print(f"Success: {name} added.")

    def check_alerts(self):
        """Simulates a simple AI decision-making process based on thresholds."""
        alerts = [item for item, info in self.data.items() 
                  if info['quantity'] <= info['threshold']]
        return alerts

# --- Example Usage ---
if __name__ == "__main__":
    app = SmartInventory()
    
    # Simulate adding data
    app.add_item("Batteries", 2, 5)
    app.add_item("Paper Reams", 10, 3)

    # Logic Check
    low_stock = app.check_alerts()
    if low_stock:
        print(f"⚠️ LOW STOCK ALERT: Please restock {', '.join(low_stock)}")
    else:
        print("✅ All systems normal.")