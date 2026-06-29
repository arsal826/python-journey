deliveries = [
    {"driver": "Arsal", "area": "north", "status": "delivered", "time": 25},
    {"driver": "Ahmed", "area": "south", "status": "delivered", "time": 35},
    {"driver": "Arsal", "area": "south", "status": "failed",    "time": 0},
    {"driver": "Sara",  "area": "north", "status": "delivered", "time": 20},
    {"driver": "Ahmed", "area": "north", "status": "delivered", "time": 30},
    {"driver": "Arsal", "area": "east",  "status": "delivered", "time": 40},
    {"driver": "Sara",  "area": "south", "status": "failed",    "time": 0},
    {"driver": "Ahmed", "area": "east",  "status": "delivered", "time": 28},
]

# Group by driver and calculate:
# → Total deliveries per driver
# → Failed deliveries per driver
# → Success rate per driver
# → Average delivery time (exclude failed)
# → Best driver overall
driver_data = {}
for delivery in deliveries:
    driver = delivery["driver"]
    status = delivery["status"]
    time = delivery["time"]

    if driver not in driver_data:
        driver_data[driver] = {
            "total_deliveries": 0,
            "failed_deliveries": 0,
            "total_time": 0,
            "successful_deliveries": 0
        }

    driver_data[driver]["total_deliveries"] += 1

    if status == "failed":
        driver_data[driver]["failed_deliveries"] += 1
    else:
        driver_data[driver]["total_time"] += time
        driver_data[driver]["successful_deliveries"] += 1

# Calculate success rate and average delivery time for each driver
for driver, data in driver_data.items():
    if data["total_deliveries"] > 0:
        data["success_rate"] = (data["successful_deliveries"] / data["total_deliveries"]) * 100
    else:
        data["success_rate"] = 0

    if data["successful_deliveries"] > 0:
        data["average_delivery_time"] = data["total_time"] / data["successful_deliveries"]
    else:
        data["average_delivery_time"] = 0

# Find best driver overall (highest success rate)
best_driver = max(driver_data, key=lambda x: driver_data[x]["success_rate"])
print("Driver Performance:")
for driver, data in driver_data.items():
    print(f"\n{driver}")
    print(f"  Total deliveries: {data['total_deliveries']}")
    print(f"  Failed:           {data['failed_deliveries']}")
    print(f"  Success rate:     {data['success_rate']:.1f}%")
    print(f"  Avg time:         {data['average_delivery_time']:.1f} min")