# sports-data-analysis
# ⚽ Premier League Match Outcome Predictor

## Overview

This project focuses on predicting the outcome of Premier League matches (home win, away win, or draw) using match data.

The goal is to take raw match data and build a machine learning pipeline that can classify match results based on relevant features.

---

## Dataset
The dataset includes:
- home_team
- away_team
- score
- home_xg
- away_xg

---

## What I Did
- Loaded and explored the data using pandas  
- Cleaned the score column (handled weird dash issue)  
- Created a new column called `result`:
- home_win
- away_win
- draw  
- Applied this logic across the entire dataset  

---

## Why This Matters
The `result` column is what the model will learn to predict.

---

## Next Steps
- Choose features (like home_xg and away_xg)
- Train a machine learning model
- Evaluate performance

---

## How to Run
```bash
source venv/bin/activate
python src/explore_data.py

