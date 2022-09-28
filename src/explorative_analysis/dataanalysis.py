[1]# Import Modules
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot

[2]# Load Dataset
df1 = pd.read_csv('refactored_data_1.csv', names = ['User_Id', 'Rating','Movie_Id'])
df2 = pd.read_csv('refactored_data_2.csv', names = ['User_Id', 'Rating','Movie_Id'])
df3 = pd.read_csv('refactored_data_3.csv', names = ['User_Id', 'Rating','Movie_Id'])
df4 = pd.read_csv('refactored_data_4.csv', names = ['User_Id', 'Rating','Movie_Id'])

df = df1
df = df.append(df2)
df = df.append(df3)
df = df.append(df4)

[3]# Count Ratings, Rated Movies and Users
rating_count = df['Rating'].value_counts().sum()
user_count = df['User_Id'].nunique()
movie_count = df['Movie_Id'].nunique()
print(rating_count)
print(user_count)
print(movie_count)

[4]# Weighted Mean Ratings
ratings_and_counts = pd.DataFrame(df['Rating'].value_counts())
ratings_and_counts = ratings_and_counts.reset_index(level=0)
ratings = ratings_and_counts.iloc[:, 0]
counts = ratings_and_counts.iloc[:, 1]
weighted_mean = np.average(a = ratings, weights = counts)

[5]# Distribution of Ratings
# Get data
data = df['Rating'].value_counts().sort_index(ascending=False)

# Create trace
trace = go.Bar(x = data.index,
               text = ['{:.1f} %'.format(val) for val in (data.values / df.shape[0] * 100)],
               textposition = 'auto',
               textfont = dict(color = '#ffffff'),
               y = data.values,
               marker = dict(color = '#073763'))

# Create layout
layout = dict(title = 'Gesamtbestand: {} Filme, {} User, {} Bewertungen; gewichteter Mittelwert der Bewertungen: {} <br><br>                                                                                       Verteilung der Bewertungen' 
                      .format(movie_count, user_count, rating_count,str(round(weighted_mean,3)).replace('.', ',')),                
                xaxis = dict(title = 'Bewertung'),
                yaxis = dict(title = 'Anzahl'))

# Create plot
fig = go.Figure(data=[trace], layout=layout)
fig.update_layout(title_font_size=15)
plot(fig)

[6]# Ratings per User
# Get data
data = df.groupby('User_Id')['Rating'].count()
print(data.sort_values())

# Create trace
trace = go.Histogram(x = data.values,
                     name = 'Ratings',
                     xbins = dict(start = 0,
                                  size = 2),
                     marker = dict(color = '#073763'))
# Create layout
layout = go.Layout(title = 'Verteilung der Bewertungen je Benutzer',
                   xaxis = dict(title = 'Bewertungen je Benutzer'),
                   yaxis = dict(title = 'Anzahl'),
                   bargap = 0.2)

# Create plot
fig = go.Figure(data=[trace], layout=layout)
plot(fig)

#df_bla=df.sort_values('User_Id')
#print(df_bla)