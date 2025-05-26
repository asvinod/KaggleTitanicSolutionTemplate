## Import necessary libraries

# Remove irrelevant data 
def clean_dataset(df): 
    # What is the irreelvant data here? 
    
    # Are there missing values? 

def transform_dataset(test, train):
    le = preprocessing.LabelEncoder()
    
    cols = ["Sex", "Embarked"]

    for col in cols:
        train[col] = le.fit_transform(train[col])
        test[col] = le.transform(test[col])

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

