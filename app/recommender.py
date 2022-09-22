import pandas as pd

def recommend_for_movie(movie_id):
    df = pd.read_csv('neighbours_ids.csv', names = ['self', 'n_1','n_2','n_3','n_4','n_5','n_6','n_7','n_8','n_9','n_10'])
    neighbors = df.iloc[movie_id-1]
    if(neighbors['self']!=movie_id):
        print('Shit')
    else:
        neighbors = neighbors.drop(['self'])
        neighbors = neighbors.tolist()
    return neighbors

recommendations = recommend_for_movie(1)
df_movies = pd.read_csv('dataset\movie_titles.csv', encoding = "ISO-8859-1", header = None, names = ['Id', 'Year','Title'])
# 72,1974,At Home Among Strangers, A Stranger Among His Own
# Kann man Kommata nach dem 2. ignorieren?
print(df_movies)