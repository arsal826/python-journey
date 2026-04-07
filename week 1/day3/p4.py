# Write calculate_discount(price, percent) — returns price after discount
def calculate_discount(price, percent):
    discount = price * (percent / 100)
    return price - discount

price = float(input("Enter the original price: "))
percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, percent)
print(f"The price after a {percent}% discount is: {final_price:.2f}")