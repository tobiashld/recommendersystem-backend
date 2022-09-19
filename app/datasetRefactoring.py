[1]# Import Modules
import pandas as pd
import numpy as np

[2]# Load Dataset
df = pd.read_csv('dataset\combined_data_1.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
df['Rating'] = df['Rating'].astype(float)

[3]# Refactor Dataset
moviesections = df[df['Rating'].isna()].reset_index()

print(moviesections)

movie_indices_list = moviesections['index'].tolist()
print(movie_indices_list)

movie_np = []
movie_id = 1


for i,j in zip(moviesections['index'][1:],moviesections['index'][:-1]):
    temp = np.full((1,i-j-1), movie_id)
    movie_np = np.append(movie_np, temp)
    movie_id += 1

last_record = np.full((1,len(df) - moviesections.iloc[-1, 0] - 1),movie_id)
movie_np = np.append(movie_np, last_record)

df = df[pd.notnull(df['Rating'])]

df['Movie_Id'] = movie_np.astype(int)
df['User_Id'] = df['User_Id'].astype(int)