def analyze_data(data, group_key, value_key, filter_threshold=None):
    """
    General analysis function:
    - data: list of dictionaries
    - group_key: key to group totals (e.g., "category", "product", "employee")
    - value_key: key to sum (e.g., "amount", "visits", "hours")
    - filter_threshold: optional threshold to filter entries (e.g., amount > 2000)
    Returns:
    - total_per_group: dict with sum per group
    - max_group: group with highest total
    - filtered_entries: list of entries above threshold (if given)
    """
    total_per_group = {}
    filtered_entries = []

    for entry in data:
        group = entry[group_key]
        value = entry[value_key]

        # Update total per group
        total_per_group[group] = total_per_group.get(group, 0) + value

        # Filter entries if threshold given
        if filter_threshold is not None and value > filter_threshold:
            filtered_entries.append(entry)

    # Find group with highest total
    max_group = max(total_per_group, key=total_per_group.get)

    return total_per_group, max_group, filtered_entries