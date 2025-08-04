import pandas as pd
# Load csv file
df = pd.read_csv('netflix movie data.csv')
print(df)

# 1. handle missing values
print(df.isnull().sum())


# missing rows drop
df.dropna(inplace = True)

print(df)

# 2 column header clean
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')

# 3 columns uniform
column = ['genre','country','language']
for col in column:
    df[col] = df[col].str.strip().str.lower()

print(df.columns)

# 4 Standardize text values
df['country'] = df['country'].str.strip().str.title()
print(df)

# 5 Date format
#dd--mm-yyyy

df['date_added']= pd.to_datetime(df['date_added'], errors='coerce')
# convert to datetime
df['date_added'] = df['date_added'].fillna(pd.Timestamp('01-01-2000'))
df['date_added']=df['date_added'].dt.strftime('%d-%m-%Y')
print(df)

# 6 remove duplicate 
df.drop_duplicates('date_added',inplace=True)
print(df)