[1]# Import Modules
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import plot

[2]# Load Dataset
df = pd.read_csv('refactored_data_complete.csv', names = ['User_Id', 'Rating','Movie_Id'])
df_with_date = pd.read_csv('refactored_data_with_date_complete.csv', names = ['User_Id', 'Rating','Date','Movie_Id'])
df_training = pd.read_csv('trainingset.csv', names = ['User_Id', 'Rating','Movie_Id'])
df_movies = pd.read_csv('src\dataset\movie_titles.csv', 
                           usecols = [0,1,2],
                           encoding = 'ISO-8859-1', 
                           header = None, 
                           names = ['Id', 'Year', 'Name'])

[3]# Count Ratings, Rated Movies and Users
rating_count = df['Rating'].value_counts().sum()
user_count = df['User_Id'].nunique()
movie_count = df['Movie_Id'].nunique()

[4]# Weighted Mean Ratings
ratings_and_counts = pd.DataFrame(df['Rating'].value_counts())
ratings_and_counts = ratings_and_counts.reset_index(level=0)
ratings = ratings_and_counts.iloc[:, 0]
counts = ratings_and_counts.iloc[:, 1]
weighted_mean = np.average(a = ratings, weights = counts)

[5]# Distribution of Ratings
# Get data
data_ratings = df['Rating'].value_counts().sort_index(ascending=False)

# Create trace
trace = go.Bar(x = data_ratings.index,
               text = ['<b>{:.1f} %</b>'.format(val).replace('.', ',') for val in (data_ratings.values / df.shape[0] * 100)],
               textposition = 'outside',
               textfont = dict(color = '#123456'),
               y = data_ratings.values,
               marker = dict(color = '#123456'))

# Create layout
layout = dict(title = '<b>Verteilung der Bewertungen im Datensatz</b> <br>Bestand: {} Filme  |  {} Benutzer  |  {} Bewertungen <br>Gewichteter Mittelwert der Bewertungen: {}' 
                      .format(movie_count, user_count, rating_count,str(round(weighted_mean,3)).replace('.', ',')),
                xaxis = dict(title = 'Bewertung'),
                yaxis = dict(title = 'Anzahl'))

# Create plot
fig = go.Figure(data=[trace], layout=layout)
fig.update_layout(title_font_size=15)
plot(fig)

[6]# Ratings per User
# Get data
data_user = df.groupby('User_Id')['Rating'].count().clip(upper=800)
print(data_user.sort_values())

# Create trace
trace = go.Histogram(x = data_user.values,
                     xbins = dict(
                                    start = 0,
                                    end = 810,
                                    size = 10),
                     marker = dict(color = '#123456'))
# Create layout
layout = go.Layout(title = '<br>Verteilung der Bewertungen je Benutzer im Datensatz',
                   xaxis = dict(title = 'Anzahl Bewertungen je Benutzer'),
                   yaxis = dict(title = 'Anzahl Benutzer'),
                   bargap = 0.2)

# Create plot
fig = go.Figure(data=[trace], layout=layout)
plot(fig)
import time
time.sleep(1)

[7]# Movies per Year
# Get data
data_movies = df_movies['Year'].value_counts().sort_index()

# Create trace
trace = go.Scatter(x = data_movies.index,
                   y = data_movies.values,
                   marker = dict(color = '#123456'))
# Create layout
layout = dict(title = '{}  Filme nach Veröffentlichungsjahr'.format(df_movies.shape[0]),
              xaxis = dict(title = 'Veröffentlichungsjahr'),
              yaxis = dict(title = 'Anzahl Filme'))

# Create plot
fig = go.Figure(data=[trace], layout=layout)
plot(fig)

[8]# Movies and Ratings per Year
# Get data
data_movies = df_movies['Year'].value_counts().sort_index()
df_with_date['yyyy'] = pd.to_datetime(df_with_date['Date']).dt.year
data_ratings = df_with_date['yyyy'].value_counts().sort_index()

# Create trace
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x = data_movies.index,
                  y = data_movies.values,
                  marker = dict(color = '#123456'),
                  name="Filmerscheinungen"),
                  secondary_y=False
)
fig.add_trace(
    go.Scatter(x = data_ratings.index,
                  y = data_ratings.values,
                  marker = dict(color = '#B40404'),
                  name="Bewertungen"),
                  secondary_y=True
)

# Create layout
fig.update_layout(title = '<br>Anzahl Filme und Bewertungen nach Jahr',
                  xaxis = dict(title = 'Jahr'),
                  xaxis_range=[1896,2008],
                  yaxis = dict(showgrid = True, title = 'Filmerscheinungen'),
                  yaxis2 = dict(showgrid = False, title = 'Bewertungen'),
                  legend=dict(
                        x=0.033,
                        y=.93,
                        traceorder="normal",
                        font=dict(
                            family="sans-serif",
                            size=12,
                            color="black"
                        ),
    ))

# Show plot
plot(fig)

[9]# Distribution of Ratings in the Trainingset
rating_count_training = df_training['Rating'].value_counts().sum()
user_count_training = df_training['User_Id'].nunique()
movie_count_training = df_training['Movie_Id'].nunique()

# Weighted Mean Ratings
ratings_and_counts_training = pd.DataFrame(df_training['Rating'].value_counts())
ratings_and_counts_training = ratings_and_counts_training.reset_index(level=0)
ratings_training = ratings_and_counts_training.iloc[:, 0]
counts_training = ratings_and_counts_training.iloc[:, 1]
weighted_mean_training = np.average(a = ratings_training, weights = counts_training)

# Get data
data_training = df_training['Rating'].value_counts().sort_index(ascending=False)

# Create trace
trace = go.Bar(x = data_training.index,
               text = ['<b>{:.1f} %</b>'.format(val).replace('.', ',') for val in (data_training.values / df_training.shape[0] * 100)],
               textposition = 'outside',
               textfont = dict(color = '#0F4336'),
               y = data_training.values,
               marker = dict(color = '#0F4336'))

# Create layout
layout = dict(title = '<b>Verteilung der Bewertungen im Trainingsset</b> <br>Bestand: {} Filme  |  {} Benutzer  |  {} Bewertungen <br>Gewichteter Mittelwert der Bewertungen: {}' 
                      .format(movie_count_training, user_count_training, rating_count_training,str(round(weighted_mean_training,3)).replace('.', ',')),
                xaxis = dict(title = 'Bewertung'),
                yaxis = dict(title = 'Anzahl'))

# Create plot
fig = go.Figure(data=[trace], layout=layout)
fig.update_layout(title_font_size=15)
plot(fig)