[1]# Import Modules
import pandas as pd
from sklearn.neighbors import NearestNeighbors

[2]# Load Dataset
df = pd.read_csv('refactored_data_1.csv', names = ['User_Id', 'Rating','Movie_Id'])
df['User_Id'] = df['User_Id'].astype(int)
df['Rating'] = df['Rating'].astype(float)
df['Movie_Id'] = df['Movie_Id'].astype(int)

# Check for missing values
print(df.isna().sum())

[3]# Filter dataset because otherwise it will lead to memory errors
# Drop Ratings from Users who rated under 200 movies
min_user_ratings = 200
filter_users = (df['User_Id'].value_counts()>min_user_ratings)
filter_users = filter_users[filter_users].index.tolist()

df_filterd = df[(df['User_Id'].isin(filter_users))]

[4]# Calculate Movie_id x User_Id matrix with NaN-values = 0
df_matrix = df_filterd.pivot_table(index='Movie_Id',columns='User_Id',values='Rating')
df_matrix=df_matrix.fillna(0)

print(df_matrix)

[5]# Calculate Nearest Neighbors for each movie
knn = NearestNeighbors(algorithm='brute', metric='cosine').fit(df_matrix)
distances,neighbours = knn.kneighbors(df_matrix,n_neighbors=6)

[6]# Export Model
pd.DataFrame(neighbours).to_csv('neighbours_1.csv', sep=',', index=False, header=False)


#######################################################################################
########################### Calculation for full movie list ###########################
#######################################################################################

[7]# Repeat 1-6 for full movie list
df1 = pd.read_csv('refactored_data_1.csv', names = ['User_Id', 'Rating','Movie_Id'])
df2 = pd.read_csv('refactored_data_2.csv', names = ['User_Id', 'Rating','Movie_Id'])
df3 = pd.read_csv('refactored_data_3.csv', names = ['User_Id', 'Rating','Movie_Id'])
df4 = pd.read_csv('refactored_data_4.csv', names = ['User_Id', 'Rating','Movie_Id'])

df1['User_Id'] = df1['User_Id'].astype(int)
df1['Rating'] = df1['Rating'].astype(float)
df1['Movie_Id'] = df1['Movie_Id'].astype(int)

df2['User_Id'] = df2['User_Id'].astype(int)
df2['Rating'] = df2['Rating'].astype(float)
df2['Movie_Id'] = df2['Movie_Id'].astype(int)

df3['User_Id'] = df3['User_Id'].astype(int)
df3['Rating'] = df3['Rating'].astype(float)
df3['Movie_Id'] = df3['Movie_Id'].astype(int)

df4['User_Id'] = df4['User_Id'].astype(int)
df4['Rating'] = df4['Rating'].astype(float)
df4['Movie_Id'] = df4['Movie_Id'].astype(int)

min_user_ratings = 200

filter_users = (df1['User_Id'].value_counts()>min_user_ratings)
filter_users = filter_users[filter_users].index.tolist()
df1_filterd = df1[(df1['User_Id'].isin(filter_users))]

filter_users2 = (df2['User_Id'].value_counts()>min_user_ratings)
filter_users2 = filter_users2[filter_users2].index.tolist()
df2_filterd = df2[(df2['User_Id'].isin(filter_users2))]

filter_users3 = (df3['User_Id'].value_counts()>min_user_ratings)
filter_users3 = filter_users3[filter_users3].index.tolist()
df3_filterd = df3[(df3['User_Id'].isin(filter_users3))]

filter_users4 = (df4['User_Id'].value_counts()>min_user_ratings)
filter_users4 = filter_users4[filter_users4].index.tolist()
df4_filterd = df4[(df4['User_Id'].isin(filter_users4))]

df_complete = df1_filterd
df_complete = df_complete.append(df2_filterd)
df_complete = df_complete.append(df3_filterd)
df_complete = df_complete.append(df4_filterd)

df_complete_matrix = df_complete.pivot_table(index='Movie_Id',columns='User_Id',values='Rating')
df_complete_matrix = df_complete_matrix.fillna(0)

knn = NearestNeighbors(algorithm='brute', metric='cosine').fit(df_complete_matrix)
distances,neighbours = knn.kneighbors(df_complete_matrix,n_neighbors=11)

pd.DataFrame(neighbours).to_csv('neighbours.csv', sep=',', index=False, header=False)

[8]# Increase every number by one to make sure the model contains ids instead of indices
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