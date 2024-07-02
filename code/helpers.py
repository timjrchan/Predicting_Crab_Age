import pandas as pd
import numpy as np
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


# Function to get CV results out

def get_cv_results(model, X,y, no_of_folds):

    '''
    
    '''

    cv_results = cross_validate(model, X, y, cv = no_of_folds,
                                scoring = ('neg_mean_absolute_error', 'neg_mean_squared_error', 'r2'),
                                return_train_score = True)
    
    print('Cross Validation Results:')

    for k,v in cv_results.items():
        print(k,v)


