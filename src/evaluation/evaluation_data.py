import pandas as pd
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from src.service.recommenderservice import get_neighbors
from src.evaluation.evaluation_calc import get_calculation_base

df = pd.read_csv('refactored_data_complete.csv', names = ['User_Id', 'Rating','Movie_Id'])
print(df)

df_example = df.loc[df['User_Id'] == 132390]
df_example = df_example.drop(df_example[df_example.Rating < 4].index)
df_example = df_example.iloc[2:]
print(df_example)

raw_true = df_example['Movie_Id'].tolist()
print(raw_true)

raw_pred = np.array(get_neighbors(28))
raw_pred = np.append(raw_pred, np.array(get_neighbors(58)))
raw_pred = np.append(raw_pred, np.array(get_neighbors(175)))
print(raw_pred)

boolean_true, boolean_pred = get_calculation_base(raw_true, raw_pred)

precision = precision_score(y_true = boolean_true, y_pred = boolean_pred)
recall = recall_score(y_true = boolean_true, y_pred = boolean_pred)
print(precision)
print(recall)