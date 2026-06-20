prices = [120, 450, 80, 300, 95, 600, 210]

# Print the highest and lowest price
# Print the average price
# Print how many prices are above 200

highest_price = max(prices)
lowest_price = min(prices)
average_price = sum(prices) / len(prices)
above_200_count = sum(1 for price in prices if price > 200)

print("Highest price:", highest_price)
print("Lowest price:", lowest_price)
print("Average price:", average_price)
print("Number of prices above 200:", above_200_count)