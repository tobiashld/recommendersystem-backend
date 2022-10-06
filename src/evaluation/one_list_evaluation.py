# Import Modules
import time
import datetime
# Runtime variable
start = time.time()
import json
import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from statistics import mean
from src.service.recommenderservice import get_shared_neighbors_for_list

def get_user_ids_to_drop():
    user_ids_to_drop = []
    f = open('testset.json')
    data = json.load(f)
    for i in data:
        user_ids_to_drop.append(i['User_Id'])
    return user_ids_to_drop

def get_calculation_base(raw_true, raw_pred):
    boolean_true = []
    boolean_pred = []
    for i in range(17770):
        boolean_true.append(False)
        boolean_pred.append(False)
    for i in raw_true:
        boolean_true[i-1] = True
    for i in raw_pred:
        boolean_pred[int(i-1)] = True
    return boolean_true, boolean_pred

def get_mean_precision_recall(): 
    # Opening JSON file
    f = open('testset.json')
    
    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the dictionary
    precision_total = []
    recall_total = []
    for i in data:        
        # Get predictions for the prediction base
        raw_pred = []
        pred_base = i['Prediction_Base']
        raw_pred = get_shared_neighbors_for_list(pred_base)

        # Get true values for the prediction base
        raw_true = i['Raw_true']

        # Get precision and recall for particular testdata
        boolean_true, boolean_pred = get_calculation_base(raw_true, raw_pred)
        precision = precision_score(y_true = boolean_true, y_pred = boolean_pred)
        recall = recall_score(y_true = boolean_true, y_pred = boolean_pred)
        precision_total = np.append(precision_total,precision)
        recall_total = np.append(recall_total,recall)

    return mean(precision_total), mean(recall_total)

mean_precision, mean_recall = get_mean_precision_recall()
print(mean_precision)
print(mean_recall)

# Runtime analysis
end = time.time()
print('Runtime: {} hh:mm:ss'.format(str(datetime.timedelta(seconds=end-start))))