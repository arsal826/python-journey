scores = {"Ali": 85, "Sara": 92, "Ahmed": 67, "Zara": 78}
# → Print who passed (above 70)
# → Print who failed
# → Print the highest scorer
# → Add 5 marks to everyone and print new scores
for name, score in scores.items():
    if score > 70:
        print(f"{name} passed with a score of {score}.")
    else:
        print(f"{name} failed with a score of {score}.")
highest_scorer = max(scores, key=scores.get)
print(f"The highest scorer is {highest_scorer} with a score of {scores[highest_scorer]}.")
# Add 5 marks to everyone
for name in scores:
    scores[name] += 5
print("New scores after adding 5 marks:")
for name, score in scores.items():
    print(f"{name}: {score}")
    