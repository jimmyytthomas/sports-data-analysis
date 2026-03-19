import pandas as pd
prem_data = pd.read_csv("dataset/pl_24-25_matches_clean.csv")
#print(prem_data.head())
#print(prem_data.columns)
#print(prem_data[["home_team", "away_team", "score"]])
#en dash if needed –
first_score = prem_data["score"].iloc[0]

print(int(first_score.split("–")[0]))
print(int(first_score.split("–")[1]))
