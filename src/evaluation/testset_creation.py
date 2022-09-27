import pandas as pd

[1]# Get complete Dataset
df = pd.read_csv('refactored_data_complete.csv', names = ['User_Id', 'Rating','Movie_Id'])
print(df)

[2]# Drop Ratings under 4
df = df.drop(df[df.Rating < 4].index)

[3]# Exclude Ratings from users who have rated under 20 movies >= 4
min_user_ratings = 20
filter_users = (df['User_Id'].value_counts()>=min_user_ratings)
filter_users = filter_users[filter_users].index.tolist()
df_filterd = df[(df['User_Id'].isin(filter_users))]

[4]# Get sample, evaluate value counts and extract sample
df_sample = df_filterd.sample(100000)
df_sample['Rating'].value_counts()
df_sample.to_csv('testdata.csv', sep=',', index=False, header=False)

[5]# Refactor sample
# {'User_Id' : 123, 'Prediction_Base' : [1,2,3,4,5], 'Raw_true' : [10,20,75,55,66,90,...]}