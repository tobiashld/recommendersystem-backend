from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import numpy as np

def get_calculation_base(raw_true, raw_pred):
    boolean_true = []
    boolean_pred = []
    for i in range(17770):
        boolean_true.append(False)
        boolean_pred.append(False)
    for i in raw_true:
        boolean_true[i-1] = True
    for i in raw_pred:
        boolean_pred[i-1] = True
    return boolean_true, boolean_pred

raw_true = np.array([720,3,50,10,57])
raw_pred = np.array([1,2,10,720])
#TP = 2
#FP = 2
#FN = 3
#TN = viele :D

boolean_true, boolean_pred = get_calculation_base(raw_true, raw_pred)

precision = precision_score(y_true = boolean_true, y_pred = boolean_pred)
recall = recall_score(y_true = boolean_true, y_pred = boolean_pred)
print(precision)
print(recall)
print(2/(2+2) == precision)
print(2/(2+3) == recall)



