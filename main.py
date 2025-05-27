import pandas as pd 
from titanic import clean_dataset, transform_dataset, predict

def main():
    test = pd.read_csv('input/test.csv')
    train = pd.read_csv('input/train.csv')

    test = clean_dataset(test)
    train = clean_dataset(train)

    transform_dataset(test, train)

    predicted = predict(test, train)
    predicted.to_csv('output/prediction.csv', index=False)


if __name__ == "__main__":
    main()