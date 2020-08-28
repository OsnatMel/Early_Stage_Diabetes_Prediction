import numpy as np
import pandas as pd

def Basic_EDA_DF(input_df):
    """

        Conducting basic EDA to understand deeper the data quality and the data integrity.
        The function gets as input a dataframe and returns a dataframe with the results of a basic EDA.

        The following info ia returned:
            1. Datatype of each column - to see whether a column was defined with an unexpected datatype due to invalid value
               (e.g. - "Age" is expected to be numeric value but if string was given as well, than it will be defined as 'object').
            2. Number of nulls in each column - to see its portion out of all datapoints.
            3. Number of appearances for each value within 'object' type columns - to see whether a column is informative
            4. 'Describe' results (on numeric columns) - to explore the values, check for outliers etc.

    """

    #See what datatypes were defined
    df_datatypes = pd.DataFrame(input_df.dtypes,columns=['Column_Datatype'])

    #See how many nulls are in a column - all columns in the dataframe are included
    df_nulls = pd.DataFrame({
                            'col_key': input_df.columns
                            ,'NullCount':input_df.isna().sum()/len(input_df)
                           }).set_index('col_key')

    #Counting of values among a column
    columns_for_groupby = list(input_df.select_dtypes(include='object').columns)
    df_groupby = pd.DataFrame(index=columns_for_groupby,columns=['Values_Count'])
    for i in columns_for_groupby:
        df_groupby.loc[i]['Values_Count'] = (input_df.groupby([i]).size()/len(input_df)).sort_values(ascending=False).to_dict()

    #Describe on numeric columns
    df_desc = pd.DataFrame({
                            'col_key': list(input_df.describe().to_dict().keys())
                            ,'Basic_Pandas_Describe':list(input_df.describe().to_dict().values())
                           }).set_index('col_key')


    output_df = df_datatypes.join(df_nulls).join(df_groupby).join(df_desc)
    return output_df
