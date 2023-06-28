## pip install sodapy 

# 1. Import libraries
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons

# 2. Imports data with API
client = Socrata("data.cdc.gov", None)
results = client.get("yni7-er2q", limit = 10084)
results_df = pd.DataFrame.from_records(results)


# Cleans up irrelevant columns with empty rows
results_df.drop(columns=['lowci','highci',
                     	'confidence_interval',
                     	'quartile_range',
                     	'suppression_flag',
                     	'phase',
                     	'time_period',
                     	'time_period_label',
                     	'time_period_end_date'], inplace = True)
results_df.dropna(subset = ['value'], inplace = True)
results_df = results_df[results_df.group != 'By State']


# Converts relevant columns to datetime data type
results_df.time_period_start_date = pd.to_datetime(results_df.time_period_start_date)


# TESTING
def model_eval(df, group_name):
    dummy_df = results_df[(results_df.group == group_name) & 
                  (results_df.indicator == 'Needed Counseling or Therapy But Did Not Get It, Last 4 Weeks')]
    dummy_df = pd.get_dummies(dummy_df, columns = ['subgroup'])
    value_idx = list(dummy_df.columns).index('value')
    #partition the data
    X   = dummy_df[list(dummy_df.columns)[value_idx+1:]] #get the input features
    y   = dummy_df['value']              #get the target

    X_train, X_test, y_train, y_test = train_test_split(X,              #the input features
                                                    y,              #the label
                                                    test_size=0.3,  #set aside 30% of the data as the test set
                                                    random_state=7, #reproduce the results
                                                   )
    #build the regressor
    rf = RandomForestRegressor(random_state=7)
    rf.fit(X_train, y_train)
    #predict the labels for the test set
    y_pred   = rf.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

    # Evaluate the Predictions
    return mse

for group in results_df.group.unique():
   print(group, ':', model_eval(results_df, group))
