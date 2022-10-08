[1]# Import Modules
import time
import datetime
# Runtime variable
start_script = time.time()
import json
import pandas as pd
from sklearn.neighbors import NearestNeighbors

[2]# Load Dataset
df = pd.read_csv('refactored_data_complete.csv', names = ['User_Id', 'Rating','Movie_Id'])
df['User_Id'] = df['User_Id'].astype(int)
df['Rating'] = df['Rating'].astype(float)
df['Movie_Id'] = df['Movie_Id'].astype(int)

[3]# Filter dataset because otherwise it will lead to memory errors
# Drop testset users and ratings from users who rated under 800 movies

# Runtime variable
start_filter = time.time()

# Remove users who rated under 800 movies
min_user_ratings = 800
filter_users = (df['User_Id'].value_counts()>min_user_ratings)
filter_users = filter_users[filter_users].index.tolist()
df_filtered = df[(df['User_Id'].isin(filter_users))]

# Remove Users from testset
users_in_testset = []
f = open('testset.json')
data = json.load(f)
for i in data:
    users_in_testset.append(i['User_Id'])

df_filtered = df_filtered[~df_filtered['User_Id'].isin(users_in_testset)]

df_filtered.to_csv('trainingset.csv', sep=',', index=False, header=False)

# Runtime variable
end_filter = time.time()
runtime_filter = end_filter-start_filter
print('Runtime filter: {} hh:mm:ss'.format(str(datetime.timedelta(seconds=runtime_filter))))

[4]# Calculate Movie_id x User_Id matrix with NaN-values = 0

# Runtime variable
start_model = time.time()

df_matrix = df_filtered.pivot_table(index='Movie_Id',columns='User_Id',values='Rating')
df_matrix=df_matrix.fillna(0)

[5]# Calculate Nearest Neighbors for each movie
knn = NearestNeighbors(algorithm='brute', metric='cosine').fit(df_matrix)
distances,neighbours = knn.kneighbors(df_matrix,n_neighbors=11)

[6]# Export Model
pd.DataFrame(neighbours).to_csv('neighbours.csv', sep=',', index=False, header=False)

# Runtime variable
end_model = time.time()
runtime_model = end_model-start_model
print('Runtime model: {} hh:mm:ss'.format(str(datetime.timedelta(seconds=runtime_model))))

[7]# Increase every number by one to make sure the model contains ids instead of indices
df = pd.read_csv('neighbours.csv', names = ['self', 'n_1','n_2','n_3','n_4','n_5','n_6','n_7','n_8','n_9','n_10'])

for index, row in df.iterrows():
    row['self']+=1
    row['n_1']+=1
    row['n_2']+=1
    row['n_3']+=1
    row['n_4']+=1
    row['n_5']+=1
    row['n_6']+=1
    row['n_7']+=1
    row['n_8']+=1
    row['n_9']+=1
    row['n_10']+=1

pd.DataFrame(df).to_csv('neighbours_ids.csv', sep=',', index=False, header=False)

[8]# Runtime analysis full script
end_script = time.time()
runtime_script = end_script-start_script
print('Runtime script: {} hh:mm:ss'.format(str(datetime.timedelta(seconds=runtime_script))))
print('Runtime other: {} hh:mm:ss'.format(str(datetime.timedelta(seconds=runtime_script-runtime_filter-runtime_model))))