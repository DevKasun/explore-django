class PurchaseError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def purchase_item(self, item_names):
          purchased_items = []
          errors = []
          for item_name in item_names:
              item_found = False
              for item in store:
                  if item["item_name"] == item_name:
                      item_found = True
                      if self.budget >= item["price"]:
                          self.budget -= item["price"]
                          purchased_items.append(item_name)
                      else:
                          errors.append(f"Insufficient budget to purchase {item_name}")
                      break
              if not item_found:
                  errors.append(f"Item {item_name} not found")

          if errors:
              raise PurchaseError("; ".join(errors))

          return f"{self.name} purchased {', '.join(purchased_items)}"

    def __repr__(self):
        return f"{self.name} has {self.budget} remaining in their budget"


store = [
    {"item_name": "Milk", "price": 250},
    {"item_name": "Bread", "price": 100},
    {"item_name": "Butter", "price": 300},
    {"item_name": "Eggs", "price": 50},
    {"item_name": "Cheese", "price": 500},
    {"item_name": "Yogurt", "price": 150}
]

kasun = Customer("Kasun", 1000)

try:
    print(kasun.purchase_item(["Milk", "Bread", "Cheese", "Eggs", "Butter", "Yogurt"]))
except PurchaseError as e:
    print(e)
