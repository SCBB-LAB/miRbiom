#!user/bin/python
import sys, os
sys.path.append('/home/scbb/.local/lib/python2.7/site-packages')
import pandas as pd
import numpy as np
vald3=sys.argv[1]
data = pd.read_csv(vald3, header=0)
mirna = list(data.miRNA)
y_pred = list(data.Predicted)
y_true= list(data.Actual)
def mean_absolute_percentage_error(y_true, y_pred): 
	y_true, y_pred = np.array(y_true), np.array(y_pred)
	return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rmse(y_true, y_pred):
	y_true, y_pred = np.array(y_true), np.array(y_pred)
	return np.sqrt(np.mean(np.square(y_true - y_pred)))

MAPE=mean_absolute_percentage_error(y_true, y_pred)
RMSE= rmse(y_true, y_pred)
print "Root Mean Square Error (RMSE): ",',', RMSE
print "Relative Mean Absolute Percentage Error (RMAPE): ",',', MAPE
print "Accuracy(%): ",',', "{:.2f}".format(100-MAPE) 
