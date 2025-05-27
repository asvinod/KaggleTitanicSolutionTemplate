## Import necessary libraries


from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Remove irrelevant data 
def clean_dataset(train): 
    # What is the irreelvant data here? 

    # Are there missing values? 

    # Does not hold int value, replace with char 
    return train

def transform_dataset(test, train):    
    cols = ["Sex", "Embarked"]

    for col in cols:
        le = preprocessing.LabelEncoder()
        le.fit(list(train[col].astype(str)) + list(test[col].astype(str)))
        train[col] = le.transform(train[col].astype(str))
        test[col] = le.transform(test[col].astype(str))

def predict(test, train):
    y = train["Survived"]
    x = train.drop("Survived", axis=1)
    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(x_train, y_train)

    score = model.score(x_val, y_val)
    print(f"Validation accuracy: {score:.4f}")

    predictions = model.predict(test)
    
    predictions_df = pd.DataFrame({
    'PassengerId': test['PassengerId'],
    'Survived': predictions
    })

    return predictions_df

