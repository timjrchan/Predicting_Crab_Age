import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import cross_validate


def clean_headers(some_dataframe: pd.DataFrame):

    '''
    This function aims to clean a dataframe's column header by: 

    Lower case all text in the column headers
    Remove trailing and leading white spaces
    Replace the spaces between words with underscore
    Remove ID of each entry
    
    
    '''

    some_dataframe.columns = some_dataframe.columns.str.lower() # lower case the headers
    some_dataframe.columns = some_dataframe.columns.str.strip() # remove whitespace from front and rear
    some_dataframe.columns = some_dataframe.columns.str.replace(' ', '_') # insert underscore between words
    some_dataframe = some_dataframe.drop(columns='id')

    return some_dataframe


# Function to convert variables to float32

def convert_float32(some_dataframe):

    columns = some_dataframe.columns.to_list()

    for col in columns:
        some_dataframe[col] = some_dataframe[col].astype('float32')

        
    print(some_dataframe.dtypes)

# Conversion to DMatrix
def convert_to_dmatrix(X, y):
    return xgb.DMatrix(data=X, label=y)
