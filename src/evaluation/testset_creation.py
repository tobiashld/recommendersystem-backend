[1]# Import Modules
import time
# Runtime variable
start = time.time()
import pandas as pd
import random
import json

# Info: Probably some movies drop out of the "testprediction" this way

[1]# Get complete Dataset
df = pd.read_csv('refactored_data_complete.csv', names = ['User_Id', 'Rating','Movie_Id'])

[2]# Drop Ratings under 5
df = df.drop(df[df.Rating < 5].index)

[3]# Exclude Ratings from users who have rated under 20 movies with 5
min_user_ratings = 19
filter_users = (df['User_Id'].value_counts()>min_user_ratings)
filter_users = filter_users[filter_users].index.tolist()
df_filterd = df[(df['User_Id'].isin(filter_users))]

df_filterd['Rating'].value_counts()

[4]# Get 1.000 random Users matching the inclusion criteria
user_ids = df_filterd['User_Id'].unique().tolist()
random_user_ids = random.choices(user_ids, k = 1000)

[5]# Get part of the dataframe including those users and evaluate value counts
df_sample = df.loc[df['User_Id'].isin(random_user_ids)]
df_sample['Rating'].value_counts()

[6]# Refactor sample and extract it into a dict of the following form:
# {'User_Id' : 123, 'Prediction_Base' : [1,2,3,4,5], 'Raw_true' : [10,20,75,55,66,90,...]}

# Find all User_Ids in the Sample
user_ids = df_sample['User_Id'].unique().tolist()
df_sample = df_sample.sort_values('User_Id')

# Create the list of dicts
dicts = []
for i in user_ids:    
    df_example = df_sample.loc[df['User_Id'] == i]
    df_example_base = df_example.head(5)
    df_example_true = df_example.iloc[5:]
    dict = {'User_Id': i, 'Prediction_Base': df_example_base['Movie_Id'].tolist(), 'Raw_true': df_example_true['Movie_Id'].tolist()}
    dicts.append(dict)

# Write the dicts to testset.json
json_evaluation = json.dumps(dicts, indent=1)
with open("testset.json", "w") as outfile:
    outfile.write(json_evaluation)

[7]# Runtime analysis
end = time.time()
print('Runtime: {:5.3f}s'.format(end-start))