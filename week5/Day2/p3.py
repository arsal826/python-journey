scores = {"Ali": 72, "Sara": 88, "Ahmed": 65, "Zara": 91}
# → Print pass/fail (passing is 70)
# → Give 10 bonus marks to anyone below 70
# → Print updated scores
# Print pass/fail
for name, score in scores.items():
    if score >= 70:
        print(f"{name} passed.")
    else:
        print(f"{name} failed.")
# Give 10 bonus marks to anyone below 70
for name in scores:
    if scores[name] < 70:
        scores[name] += 10
# Print updated scores
print("Updated scores:", scores)
