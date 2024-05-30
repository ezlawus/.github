# %% [code]
# %% [code]
import numpy as np
import pandas as pd

def info(df:pd.DataFrame):
    info=[]
    columns=df.columns
    for column in columns:
        dtypes = df[column].dtypes
        counts = df[column].count()
        nunique = df[column].nunique()
        sum_null = df[column].isnull().sum()
        info.append([column, dtypes, counts, nunique, sum_null])
    df_info = pd.DataFrame(info)
    df_info.columns = ['column', 'dtypes', 'count', 'nunique', 'sum_null']
    return df_info