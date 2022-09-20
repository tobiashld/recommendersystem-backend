[1]# Import Modules
import pandas as pd
import numpy as np

[2]# Load Dataset
df = pd.read_csv('dataset\combined_data_1.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
df['Rating'] = df['Rating'].astype(float)

[3]# Refactor Dataset - Goal: a Dataframe with the Columns 'User_Id', 'Rating' and 'Movie_id' which contains every Rating
# Create a Dataframe which indexes every Movie-id-row (they are the only rows without a rating)
moviesections = df[df['Rating'].isna()].reset_index()
# Grab the first to the secondlast index
indexlow = moviesections['index'][:-1]
# Grab the second to the last index
indexhigh = moviesections['index'][1:]

movie_id_column = []
movie_id = 1

# Consider the start(low) and end index(high) of each movie(_id)
for low,high in zip(indexlow,indexhigh):
    # create an arrray with one column, high-1-low rows and each row filled with movie_id
    # high-1, because high itself is not a rating but the following Movie-id-row
    current_movie = np.full((1,high-1-low), movie_id)
    # append the movie_ids to the movie_id_column
    movie_id_column = np.append(movie_id_column, current_movie)
    movie_id += 1

# Since this doesn't give us the Ratings from the last movie in our df, we need to add them now
# for this we invert the movie-id-indices and take the first value
lastindex = moviesections.iloc[-1,0]
# create an arrray with one column, len(df)-lastindex-1 rows and each row filled with movie_id
lastentry = np.full((1,len(df)-lastindex-1),movie_id)
movie_id_column = np.append(movie_id_column, lastentry)

# last delete the Movie-id-row 
df = df[pd.notnull(df['Rating'])]
# and declare the user-ids column as integer, since know it now contains only numbers
df['User_Id'] = df['User_Id'].astype(int)
# and add the movie_id_column to the dataframe
df['Movie_Id'] = movie_id_column.astype(int)

print(df)