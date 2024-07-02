import pandas as pd
import numpy as np



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


