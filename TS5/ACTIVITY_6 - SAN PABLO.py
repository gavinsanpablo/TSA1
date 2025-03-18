import json

class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = self.validate_id(item_id)
        self.name = self.validate_name(name)
        self.description = description
        self.price = self.validate_price(price)
    
    @staticmethod
    def validate_id(item_id):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        return item_id
    
    @staticmethod
    def validate_name(name):
        if not name or not isinstance(name, str):
            raise ValueError("Name cannot be empty and must be a string.")
        return name.strip()
    
    @staticmethod
    def validate_price(price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        return price
    
    def to_dict(self):
        return {"id": self.item_id, "name": self.name, "description": self.description, "price": self.price}

class ItemManager:
    def __init__(self):
        self.items = []
    
    def create_item(self, item_id, name, description, price):
        try:
            item = Item(item_id, name, description, price)
            self.items.append(item)
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items:
                print(item.to_dict())
    
    def update_item(self, item_id, name=None, description=None, price=None):
        for item in self.items:
            if item.item_id == item_id:
                try:
                    if name:
                        item.name = Item.validate_name(name)
                    if description:
                        item.description = description
                    if price is not None:
                        item.price = Item.validate_price(price)
                    print("Item updated successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
                return
        print("Item not found.")
    
    def delete_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print("Item deleted successfully!")
                return
        print("Item not found.")
    
    def save_to_file(self, filename="items.json"):
        with open(filename, "w") as file:
            json.dump([item.to_dict() for item in self.items], file, indent=4)
        print("Data saved to file.")
    
    def load_from_file(self, filename="items.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.items = [Item(**item) for item in data]
            print("Data loaded from file.")
        except (FileNotFoundError, json.JSONDecodeError):
            print("No saved data found.")

if __name__ == "__main__":
    manager = ItemManager()
    
    while True:
        print("\nItem Management System")
        print("1. Create Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Save Items")
        print("6. Load Items")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Item Name: ")
                description = input("Enter Item Description: ")
                price = float(input("Enter Item Price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input. Please enter correct values.")
        elif choice == "2":
            manager.read_items()
        elif choice == "3":
            try:
                item_id = int(input("Enter Item ID to update: "))
                name = input("Enter new name (leave blank to keep current): ")
                description = input("Enter new description (leave blank to keep current): ")
                price = input("Enter new price (leave blank to keep current): ")
                price = float(price) if price else None
                manager.update_item(item_id, name if name else None, description if description else None, price)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            try:
                item_id = int(input("Enter Item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            manager.save_to_file()
        elif choice == "6":
            manager.load_from_file()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
