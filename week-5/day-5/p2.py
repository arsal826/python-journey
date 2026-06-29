def add_product():
    product_name = input("Enter the product name: ")
    if product_name == "":
        print("Name cannot be empty")
        return
    
    product_category = input("Enter the product category: ")
    if product_category == "":
        print("Category cannot be empty")
        return
    
    try:
        product_price = float(input("Enter the product price: "))
        if product_price < 0:
            print("Price cannot be negative")
            return
    except ValueError:
        print("Price must be a number")
        return
    
    try:
        product_stock = int(input("Enter the product stock: "))
        if product_stock < 0:
            print("Stock cannot be negative")
            return
    except ValueError:
        print("Stock must be a number")
        return
    
    with open("inventory.txt", "a") as f:
        f.write(f"{product_name},{product_category},{product_price},{product_stock}\n")
    print("Product added!")

def view_inventory():
    try:
        with open("inventory.txt", "r") as f:
            products = f.readlines()
            if not products:
                print("Inventory is empty")
                return
            for product in products:
                name, category, price, stock = product.strip().split(",")
                print(f"Name: {name}, Category: {category}, Price: {price}, Stock: {stock}")
    except FileNotFoundError:
        print("Inventory file not found. Please add a product first.")

def low_stock_report():
    try:
        with open("inventory.txt", "r") as f:
            products = f.readlines()
            low_stock_products = [p for p in products if int(p.strip().split(",")[3]) < 10]
            if not low_stock_products:
                print("No products with low stock")
                return
            for product in low_stock_products:
                name, category, price, stock = product.strip().split(",")
                print(f"Name: {name}, Category: {category}, Price: {price}, Stock: {stock}")
    except FileNotFoundError:
        print("Inventory file not found. Please add a product first.")

def category_value():
    try:
        with open("inventory.txt", "r") as f:
            products = f.readlines()
            category_values = {}
            for product in products:
                name, category, price, stock = product.strip().split(",")
                price = float(price)
                stock = int(stock)
                value = price * stock
                if category in category_values:
                    category_values[category] += value
                else:
                    category_values[category] = value
            for category, total_value in category_values.items():
                print(f"Category: {category}, Total Stock Value: {total_value}")
    except FileNotFoundError:
        print("Inventory file not found. Please add a product first.")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Low Stock Report")
        print("4. Category Value")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice: ")
            if choice == "1":
                add_product()
            elif choice == "2":
                view_inventory()
            elif choice == "3":
                low_stock_report()
            elif choice == "4":
                category_value()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


main()
