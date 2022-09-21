[1]# Import Modules
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

[2]# Load Dataset
df = pd.read_csv('refactored_data_1.csv', names = ['User_Id', 'Rating','Movie_Id'])
df['User_Id'] = df['User_Id'].astype(int)
df['Rating'] = df['Rating'].astype(float)
df['Movie_Id'] = df['Movie_Id'].astype(int)

# Check for missing values
print(df.isna().sum())

[3]# Filter dataset because otherwise it will lead to memory errors
# Drop Ratings from Users who ratet under 200 movies
min_user_ratings = 200
filter_users = (df['User_Id'].value_counts()>min_user_ratings)
filter_users = filter_users[filter_users].index.tolist()

df_filterd = df[(df['User_Id'].isin(filter_users))]

print(df_filterd)

[4]# Calculate Movie_id x User_Id matrix with NaN-values = 0
df_matrix = df_filterd.pivot_table(index='Movie_Id',columns='User_Id',values='Rating')
df_matrix=df_matrix.fillna(0)

print(df_matrix)

[5]# Calculate Nearest Neighbors for each movie
knn = NearestNeighbors(algorithm='brute', metric='cosine').fit(df_matrix)
distances,neighbours = knn.kneighbors(df_matrix,n_neighbors=6)
#,return_distance=False
print(neighbours[47])



def recommend(matrix,stated_movie_ids):
    knn = NearestNeighbors(algorithm='brute', metric='cosine').fit(matrix)
    distances,neighbours = knn.kneighbors(matrix,n_neighbors=3)



[6]# Datasets
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

dfkomplett = df1_filterd
dfkomplett = dfkomplett.append(df2_filterd)
dfkomplett = dfkomplett.append(df3_filterd)
dfkomplett = dfkomplett.append(df4_filterd)


dfkomplett_matrix = dfkomplett.pivot_table(index='Movie_Id',columns='User_Id',values='Rating')
dfkomplett_matrix = dfkomplett_matrix.fillna(0)


[5]# Calculate Nearest Neighbors for each movie
knn = NearestNeighbors(algorithm='brute', metric='cosine').fit(dfkomplett_matrix)
distances,neighbours = knn.kneighbors(dfkomplett_matrix,n_neighbors=11)
#,return_distance=False

print(neighbours)

pd.DataFrame(neighbours).to_csv('neighbours.csv', sep=',', index=False, header=False)