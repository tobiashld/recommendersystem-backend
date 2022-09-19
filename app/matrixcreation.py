[1]# Import Modules
import pandas as pd
import numpy as np

[2]# Load Datasets
df = pd.read_csv('dataset\combined_data_1.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
df['Rating'] = df['Rating'].astype(float)
#df2 = pd.read_csv('dataset\combined_data_2.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
#df2['Rating'] = df1['Rating'].astype(float)
#df3 = pd.read_csv('dataset\combined_data_3.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
#df3['Rating'] = df1['Rating'].astype(float)
#df4 = pd.read_csv('dataset\combined_data_4.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
#df4['Rating'] = df1['Rating'].astype(float)

[3]# Refactor Dataset so that movie_id is a seperate column instead of a row
# Rows with 'Rating' NaN are the movie_id rows
moviesections = df[df['Rating'].isna()].reset_index()

movie_np = []
movie_id = 1

for i,j in zip(moviesections['index'][1:],moviesections['index'][:-1]):
    # numpy approach
    temp = np.full((1,i-j-1), movie_id)
    movie_np = np.append(movie_np, temp)
    movie_id += 1

# Account for last record and corresponding length
# numpy approach
last_record = np.full((1,len(df) - moviesections.iloc[-1, 0] - 1),movie_id)
movie_np = np.append(movie_np, last_record)

df = df[pd.notnull(df['Rating'])]

df['Movie_Id'] = movie_np.astype(int)
df['User_Id'] = df['User_Id'].astype(int)

print(df)