traffic = [
    {"date": "2026-04-01", "page": "Home",      "visits": 1200},
    {"date": "2026-04-01", "page": "Contact",   "visits": 300},
    {"date": "2026-04-02", "page": "Home",      "visits": 1500},
    {"date": "2026-04-02", "page": "Blog",      "visits": 700},
    {"date": "2026-04-03", "page": "Home",      "visits": 1000},
    {"date": "2026-04-03", "page": "Contact",   "visits": 400},
    {"date": "2026-04-03", "page": "Blog",      "visits": 800}
]  
total_visits_per_page = {}
total_visits_per_day = {}
highest_traffic_page = ""
highest_traffic_day = ""
page_more_than_1000 = []
for entry in traffic:
    page = entry["page"]
    visits = entry["visits"]
    date = entry["date"]

    # Total visits per page
    if page in total_visits_per_page:
        total_visits_per_page[page] += visits
    else:
        total_visits_per_page[page] = visits

    # Total visits per day
    if date in total_visits_per_day:
        total_visits_per_day[date] += visits
    else:
        total_visits_per_day[date] = visits

    # Pages with more than 1000 visits
    if visits > 1000:
        page_more_than_1000.append(entry)
# Page with highest traffic
highest_traffic_page = max(total_visits_per_page, key=total_visits_per_page.get)
# Day with highest traffic
highest_traffic_day = max(total_visits_per_day, key=total_visits_per_day.get)

#print results
print("Total visits per page:")
for page, visits in total_visits_per_page.items():
    print(f"{page}: {visits} visits")
print("\nTotal visits per day:")
for date, visits in total_visits_per_day.items():
    print(f"{date}: {visits} visits")
print(f"\nPage with highest traffic: {highest_traffic_page} ({total_visits_per_page[highest_traffic_page]} visits)")
print(f"Day with highest traffic: {highest_traffic_day} ({total_visits_per_day[highest_traffic_day]} visits)")
print("\nPages with more than 1000 visits:")
for entry in page_more_than_1000:
    print(f"{entry['date']} - {entry['page']}: {entry['visits']} visits")
    