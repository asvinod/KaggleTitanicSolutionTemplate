# KaggleTitanicSolution
Most of the solution is already written out for you. Your challenge is to handle simple filtering with the given dataset. Credits to Asad Ali (Here is this article: https://medium.com/@asaadaali/how-i-solved-the-kaggles-titanic-machine-learning-from-disaster-competition-1d24f998059f) I'd reccomend taking a read after completing the dataset cleaning portion yourself. 

Consider what data is irrelevant. What can we drop from the dataset? How do we drop it? 

What exceptions should be considered (missing values), and how do we handle those? 

## sklearn & Other Functions
sklearn (Scikit-learn) is a python ML library that provides tools for prototyping models. 

### transform_dataset 
A LabelEncoder instance converts string categories into numeric values. This is called label mapping. 

```
cols = ["Sex", "Embarked"]

for col in cols:
    le = preprocessing.LabelEncoder()
    le.fit(list(train[col].astype(str)) + list(test[col].astype(str)))
    train[col] = le.transform(train[col].astype(str))
    test[col] = le.transform(test[col].astype(str))
```

Here, we specify the columns in both datasets that need to be encoded.

A LabelEncoder instance converts string categories into numeric values. This is called label mapping. 

The fit function learns the mapping of input values to numerical values. The transform function applies the mapped learning to the actual data. 


### predict
This is where we will train a logistic regression model. A logistic regression model predicts the probability that a specific outcome will occur.

```
y = train["Survived"]
x = train.drop("Survived", axis=1)
```

This is simply splitting the data into the input and output. The drop() function in pandas creates a new DataFrame that is a copy of train, without the "Survived" column. This is what is in x.

The "Survived" column is what y is. 

```
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)
```

The function ```train_test_split()``` splits the data into what will be used to train the model, and what will be used to validate the model's accuracy.

We set 20% of the data to validating the model, and 80% to training (this is pretty standard in training ML models).

```
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
```

This is where we actually create the Logistic Regression model, and train it with our data, essentially asking it to learn the relationship between the input and output.

```
score = model.score(x_val, y_val)
print(f"Validation accuracy: {score:.4f}")
```

This basically scores how accurate the model was.

```
predictions = model.predict(test)
```

This is a different predict function from sklearn! This is where the model actually makes the prediction with the given test data.

```
predictions_df = pd.DataFrame({
    'PassengerId': test['PassengerId'],
    'Survived': predictions
})
```

Finally, we just format the predictions into a DataFrame! 
