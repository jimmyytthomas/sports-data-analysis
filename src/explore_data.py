import pandas as pd #import pandas so we can work with the data tables 

from sklearn.model_selection import train_test_split #before this works must install in terminall by doing pip install scikit-learn

prem_data = pd.read_csv("dataset/pl_24-25_matches_clean.csv") #load the dataset into the DataFrame (table)

#en dash if needed –
#open virtual environment source venv/bin/activate




def get_result(score): #This function takes a score like ("2-1") and returns the match result
    parts = score.replace("–","-").split("-") #This replaces the en dash with normal dash and then splits into ["2","1"]
    
    home_goals = int(parts[0]) #convert to int
    away_goals = int(parts[1]) #converts to int
    
    #This determines which team won based on goals 
    if home_goals > away_goals: 
        result = "home_win"
    elif home_goals < away_goals:
        result = "away_win"
    else:
        result = "draw"
    
    
    return result #returns the result of the score 


prem_data["result"] = prem_data["score"].apply(get_result) #applies the function to every row in "score" column and creates a new column called "result"

#select features (inputs for the model)
X = prem_data[["home_xg", "away_xg"]]

#select target (which we want to predict)
y = prem_data["result"] #“grab the result column from the dataset”

#create a mapping from text labels to numbers so it is taking 
mapping = {
    "home_win":0,
    "away_win":1,
    "draw":2
}

y = y.map(mapping) #then we change to convert those values into numbers so now y=0,1 or 2


#print features preview
#print(X.head())
#print target preview(now numeric)
#print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

print(len(X_train),len(X_test))