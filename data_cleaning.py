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

# drop records with no field
print('org_id list with no field id: ', df_all_unique_id.loc[df_all_unique_id.field_id.isna(), 'org_id'].drop_duplicates().values)

no_field_index = pd.DataFrame(df_all_unique_id.loc[pd.to_numeric(df_all_unique_id.field_id, errors='coerce').isna(),'field_id']).index
df_all_fields = df_all_unique_id.copy()
df_all_fields.drop(labels=no_field_index,inplace=True)
print('removed records: ',df_all_unique_id.shape[0] - df_all_fields.shape[0])
print('remained records: ', df_all_fields.shape[0])

# drop records with no orientation
print('org_id list with no orientation id: ', df_all_fields.loc[df_all_fields.orientation_id.isna(), 'org_id'].drop_duplicates().values)

no_orientation_index = pd.DataFrame(df_all_fields.loc[pd.to_numeric(df_all_fields.orientation_id, errors='coerce').isna(),'orientation_id']).index
df_all_ori = df_all_fields.copy()
df_all_ori.drop(labels=no_orientation_index,inplace=True)
print('removed records: ',df_all_fields.shape[0] - df_all_ori.shape[0])
print('remained records: ', df_all_ori.shape[0])

# check if there is non-numeric characters in a column (optional)
"""
Index(['item_id', 'item_title', 'value', 'field_id', 'field_title',
        'orientation_id', 'orientation_title', 'unique_id', 'org_id'],
       dtype='object')
""";
# dataframe = pl_quant # select dataframe
# column = 'ind_pl_score' # select column
# non_numeric = pd.DataFrame(dataframe.loc[pd.to_numeric(dataframe[column], errors='coerce').isna(),column])
# non_numeric

# trim spaces from string items
df_trim = df_all_ori.copy()
string_columns = ['item_title','field_title',
                  'orientation_title', 'org_name', 'unique_id']
for column in string_columns:
    df_trim[column] = df_trim[column].str.strip()
df_trim.shape[0]

# replace triple quality scale values with numerals
df_numeral_values = df_trim.copy()
df_numeral_values['value'].replace({'low':1, 'middle':2, 'high':3}, inplace=True)
df_numeral_values.shape[0]

# change dtype of remaining columns
df_modify_dtypes = df_numeral_values.copy()

dtypes = {'item_title':'string',
          'kind':'string',
          'value':'float64',
          'org_name':'string',
          'field_title':'string',
          'orientation_title':'string',
          'unique_id':'string',
#          'org_id':'int64',          
#          'field_id':'int64',
#          'orientation_id':'int64',
         }
for c in dtypes.keys():
    df_modify_dtypes[c] = df_modify_dtypes[c].astype(dtypes[c])
    
print('number of recored: ', df_modify_dtypes.shape[0])
df_modify_dtypes.info()

# drop record with np.nan value
df_drop_nan_value = df_modify_dtypes.copy()

df_drop_nan_value.dropna(subset=['value'], inplace=True)

print('number of nan values removed: ', df_modify_dtypes.shape[0] - df_drop_nan_value.shape[0])
print('total number of records removed from the base data: ', df.shape[0] - df_drop_nan_value.shape[0])
print('remained records: ', df_drop_nan_value.shape[0])

# read english titles for items
item_en = pd.read_excel('./input_data/item_en_names.xlsx', sheet_name='Sheet1')
item_en = item_en.convert_dtypes()
print('number of items is', item_en.shape[0], 'in', item_en.shape[1], 'columns: id and item_en_title')

# add english titles for items
df_item_en = df_drop_nan_value.copy()
df_item_en = df_item_en.merge(item_en,how='left', left_on='item_id',right_on='item_id')
items_prepared = df_item_en.copy()
print('final cleaned data number of records: ', items_prepared.shape[0])
items_prepared.head(1)

# read indicator english names
ind_list_en = pd.read_excel('./input_data/indicator_parameters.xlsx', na_values='nan'
#                             , usecols=[0,2]
                           )

print(ind_list_en.shape)
ind_list_en.head(1)

