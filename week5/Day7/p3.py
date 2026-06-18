scores = {"Ali": 85, "Sara": 92, "Ahmed": 67}
# Print who passed (above 70)
# Print the highest scorer

for student, score in scores.items():
    if score > 70:
        print(f"{student} passed with a score of {score}.")
highest_scorer = max(scores, key=scores.get)
print(f"The highest scorer is {highest_scorer} with a score of {scores[highest_scorer]}.")
