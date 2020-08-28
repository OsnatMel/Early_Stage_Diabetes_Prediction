import numpy as np
import pandas as pd

def Replace_Null(df,fill_type='type',values = {}):
    """

        Replacing null values based either on column data type or on values given per column.

        The function gets a dataframe to update, which method of filling to take under "fill_type" and the values to replace
        with per column (if "fill_type" was defined as 'column')

    """
    
    if fill_type == 'type':
        for col in df:
            col_dt = df[col].dtype 
            if col_dt == int or col_dt == float:
                df[col].fillna(-1,inplace=True)
            elif col_dt == object:
                df[col].fillna('NA',inplace=True)
            else:
                df[col].fillna("",inplace=True)
    elif fill_type == 'column':
        if values == {}:
            print('Missimg values to replace nulls - fill type was defined as column based')
        else:
            df.fillna(value=values,inplace=True)
    return df

###############################################################################################################################

def Data_Binning(df,col_name,start_val,end_val,freq_val,closed_val):
    
    """

        Creating a categorical and codes columns for numeric column.
        
        The function gets a dataframe to update, the reference column for the categories and the category's limits.

    """
    #creating the categorical column
    category_column_name = str(col_name)+'_cat'
    df[category_column_name] = pd.cut(df[col_name]
                            ,bins=pd.interval_range(start=start_val, freq=freq_val, end=end_val, closed=closed_val)
                           )
    #creating the codes of the categorical column
    category_codes_column_name = str(col_name)+'_cat_codes'
    df[category_codes_column_name] = df[category_column_name].cat.codes
    
    return df

###############################################################################################################################

def Replace_Values(df,fill_type,values_for_replacement,column_to_update=''):
    
    """
    
        The function gets a dataframe to update, which method of filling to take under "fill_type" and the values to replace
        with.
        The replacement can be on the entire dataframe or on a specific column.

    """

    df_STG = df.copy()

    if fill_type == 'all':
        for i in range(values_for_replacement.shape[0]):
            df_STG = df_STG.replace(values_for_replacement[i,0], values_for_replacement[i,1])
    
    elif fill_type == 'column':
        for i in range(values_for_replacement.shape[0]):
            df_STG[column_to_update] = df_STG[column_to_update].replace(values_for_replacement[i,0], values_for_replacement[i,1])
    
    else:
        print('Unknown convert type')

    return df_STG

