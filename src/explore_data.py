import pandas as pd
prem_data = pd.read_csv("dataset/pl_24-25_matches_clean.csv")
#print(prem_data.head())
#print(prem_data.columns)
#print(prem_data[["home_team", "away_team", "score"]])
#en dash if needed –
first_score = prem_data["score"].iloc[0]

home_goals = int(first_score.split("–")[0])
away_goals = int(first_score.split("–")[1])

result = None
if home_goals > away_goals:
    result = "home_win"
elif home_goals < away_goals:
    result = "away_win"
else:
    result = "draw"

print(result)
