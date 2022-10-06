[1]# Import Modules
import time
import datetime
# Runtime variable
start = time.time()
import pandas as pd
import numpy as np

[2]# Load Dataset
df1 = pd.read_csv('src\dataset\combined_data_1.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
df2 = pd.read_csv('src\dataset\combined_data_2.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
df3 = pd.read_csv('src\dataset\combined_data_3.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])
df4 = pd.read_csv('src\dataset\combined_data_4.txt', header = None, names = ['User_Id', 'Rating'], usecols = [0,1])

[3]# Refactor Dataset - Goal: a Dataframe with the Columns 'User_Id', 'Rating' and 'Movie_id' which contains every Rating
# Create a Dataframe which indexes every Movie-id-row (they are the only rows without a rating)
def refactor(df, first_movie_id):
    moviesections = df[df['Rating'].isna()].reset_index()
    # Grab the first to the secondlast index
    indexlow = moviesections['index'][:-1]
    # Grab the second to the last index
    indexhigh = moviesections['index'][1:]

    movie_id_column = []
    movie_id = first_movie_id

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
    df['Movie_Id'] = movie_id_column.astype(int)
    return df


[4]# Export dataset
df1 = refactor(df1, first_movie_id = 1)
df2 = refactor(df2, first_movie_id = 4500)
df3 = refactor(df3, first_movie_id = 9211)
df4 = refactor(df4, first_movie_id = 13368)
df = df1
df = df.append(df2)
df = df.append(df3)
df = df.append(df4)

df.to_csv('refactored_data_complete.csv', sep=',', index=False, header=False)

[5]# Runtime analysis
end = time.time()
print('Runtime: {} hh:mm:ss'.format(str(datetime.timedelta(seconds=end-start))))