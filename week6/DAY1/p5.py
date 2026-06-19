matches = [
    {"team": "Brazil",     "goals_for": 3, "goals_against": 1},
    {"team": "Argentina",  "goals_for": 2, "goals_against": 2},
    {"team": "Brazil",     "goals_for": 1, "goals_against": 0},
    {"team": "France",     "goals_for": 4, "goals_against": 2},
    {"team": "Argentina",  "goals_for": 3, "goals_against": 1},
    {"team": "France",     "goals_for": 0, "goals_against": 1},
    {"team": "Brazil",     "goals_for": 2, "goals_against": 2},
]

# For each team calculate:
# → total goals scored (goals_for)
# → total goals conceded (goals_against)
# → goal difference (scored - conceded)
# → number of matches played
# Print the team with the best goal difference
team_data = {}
for match in matches:
    team = match["team"]
    goals_for = match["goals_for"]
    goals_against = match["goals_against"]

    if team not in team_data:
        team_data[team] = {"goals_for": 0, "goals_against": 0, "matches": 0}

    team_data[team]["goals_for"] += goals_for
    team_data[team]["goals_against"] += goals_against
    team_data[team]["matches"] += 1
# Calculate goal difference and find the team with the best goal difference
best_team = None
best_diff = float('-inf')
for team, data in team_data.items():
    goal_diff = data["goals_for"] - data["goals_against"]
    print(f"{team}: Goals For = {data['goals_for']}, Goals Against = {data['goals_against']}, Goal Difference = {goal_diff}, Matches Played = {data['matches']}")

    if goal_diff > best_diff:
        best_diff = goal_diff
        best_team = team

print(f"\nTeam with the best goal difference: {best_team} with a difference of {best_diff}")