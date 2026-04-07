# Calculate and print:
# ```
# → Total wins per team
# → Total losses per team
# → Total runs scored per team
# → Total runs conceded per team
# → Win percentage per team
# → Team with best win percentage
# → Team with highest average score per match
# → Print full standings table like this:

# TEAM        W  L  WIN%   AVG SCORE
# Pakistan    2  1  66.7%  195.0
# India       3  0  100%   186.7
# England     0  2  0.0%   179.0
# Australia   1  1  50.0%  192.5

matches = [
    {"team": "Pakistan", "opponent": "India",     "scored": 180, "conceded": 165, "result": "win"},
    {"team": "India",    "opponent": "Pakistan",  "scored": 165, "conceded": 180, "result": "loss"},
    {"team": "Pakistan", "opponent": "England",   "scored": 210, "conceded": 198, "result": "win"},
    {"team": "England",  "opponent": "Pakistan",  "scored": 198, "conceded": 210, "result": "loss"},
    {"team": "India",    "opponent": "England",   "scored": 175, "conceded": 160, "result": "win"},
    {"team": "England",  "opponent": "India",     "scored": 160, "conceded": 175, "result": "loss"},
    {"team": "Pakistan", "opponent": "Australia", "scored": 195, "conceded": 200, "result": "loss"},
    {"team": "Australia","opponent": "Pakistan",  "scored": 200, "conceded": 195, "result": "win"},
    {"team": "India",    "opponent": "Australia", "scored": 220, "conceded": 185, "result": "win"},
    {"team": "Australia","opponent": "India",     "scored": 185, "conceded": 220, "result": "loss"},
]
total_wins = {}
total_losses = {}
total_runs_scored = {}
total_runs_conceded = {}
win_percentage = {}
for match in matches:
    team = match["team"]
    result = match["result"]
    scored = match["scored"]
    conceded = match["conceded"]

    if team not in total_wins:
        total_wins[team] = 0
        total_losses[team] = 0
        total_runs_scored[team] = 0
        total_runs_conceded[team] = 0

    if result == "win":
        total_wins[team] += 1
    elif result == "loss":
        total_losses[team] += 1

    total_runs_scored[team] += scored
    total_runs_conceded[team] += conceded

for team in total_wins:
    total_matches = total_wins[team] + total_losses[team]
    win_percentage[team] = (total_wins[team] / total_matches * 100) if total_matches > 0 else 0
best_win_percentage_team = max(win_percentage, key=win_percentage.get)
average_score = {team: total_runs_scored[team] / (total_wins[team] + total_losses[team]) for team in total_wins}
best_average_score_team = max(average_score, key=average_score.get)
print("TEAM   W    L  WIN%   AVG SCORE")
for team in total_wins:
    print(f"{team:12} {total_wins[team]:2} {total_losses[team]:2} {win_percentage[team]:6.1f}% {average_score[team]:8.1f}")
print(f"\nTeam with best win percentage: {best_win_percentage_team} ({win_percentage[best_win_percentage_team]:.1f}%)")
print(f"Team with highest average score per match: {best_average_score_team} ({average_score[best_average_score_team]:.1f})")
