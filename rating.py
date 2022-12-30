# import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import clear_output
import time

# options
pd.set_option('display.max_rows', 70)

# Data Cleaning

## Read Data
df = pd.read_csv('input_data/items.txt', header=0, low_memory=False, sep='\t')
display(df.head())
display(df.shape[0])
df.info()
np.sum(df.isna())


# replace '\\N' characters with np.nan (output for sql sometimes contains \\N character which has to be replaced with standard np.nan)
df_nan = df.copy()
df_nan.replace('\\N', np.nan, inplace=True)
print('removed records: ',df.shape[0] - df_nan.shape[0])
print('remained records: ', df_nan.shape[0])

# drop records with no unique_id
print('org_id list with no unique id: ', df_nan.loc[df_nan.unique_id.isna(), 'org_id'].drop_duplicates().values)

no_unique_id_index = df_nan.loc[df_nan.unique_id.isna(), 'org_id'].index
df_all_unique_id = df_nan.copy()
df_all_unique_id.drop(labels=no_unique_id_index, inplace=True)
print('removed records: ',df_nan.shape[0] - df_all_unique_id.shape[0])
print('remained records: ', df_all_unique_id.shape[0])

