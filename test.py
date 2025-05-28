import pandas as pd 

# Series: 1D array 
names = ["Ashwin", "Nicholas", "John", "Joe", "Jeff"]
names_s = pd.Series(names)
ages = [10, 12, 15, 25, 19]
ages_s = pd.Series(ages)
#print(ages_s)

# DataFrame: combination of series
df = pd.DataFrame({'Name':names, 'Age': ages_s})
df.to_csv('csv_files/simple.csv')

#read_csv: converts a CSV file into a DataFrame
test_csv = pd.read_csv('csv_files/test.csv')
# print(test_csv)
#print(type(test_csv))

#head(num): returns num rows
first_3 = test_csv.head(3)
#print(first_3)

#dropping 
# drop function for dropping rows
# set axis to 1 to drop columns 

#df['col_name']
names = test_csv['Name']

# I want to KEEP rows where values in age column greater than 50 

# I want to know which columns in test.csv have NULL values..

#fillna and dropna 
#fillna: replaces null values with something
#dropna: removes rows / columns containing null values (axis parameter)
# inplace: another parameter, setting it to true modifies original DF

