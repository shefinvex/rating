# set the point of indicators

ind_points = dict()
for ind in function_dict.keys():
    ind_points[ind] = round(ind_list_en.loc[ind_list_en['ind_title'] == ind, 'score'].values[0],3)
    
# set the intercept and slope of indicators

ind_intercepts = dict()
for ind in function_dict.keys():
    ind_intercepts[ind] = ind_list_en.loc[ind_list_en['ind_title'] == ind, 'intercept'].values[0]

ind_slopes = dict()
for ind in function_dict.keys():
    ind_slopes[ind] = ind_list_en.loc[ind_list_en['ind_title'] == ind, 'slope'].values[0]

# define function for creating ind_items dataframe 

def ind_items_func(my_ind, ind_items, items_prepared, my_field_id, my_orientation_id):
    
    if my_ind not in function_dict:
        raise Exception('ind_items_func error: indicator not in list')

    item_mask = items_prepared['item_en_title'].isin(ind_items[my_ind])
    field_mask = items_prepared['field_id'] == my_field_id
    orientation_mask = items_prepared['orientation_id'] == my_orientation_id

    ind_data_df = items_prepared.loc[item_mask & field_mask & orientation_mask, ['org_id','item_en_title','value']] # create df that has values
    
    coops_df = pd.DataFrame(items_prepared.loc[field_mask & orientation_mask, ['org_id','national_id','org_name','field_id','orientation_id']].drop_duplicates(subset=['org_id'])) # create df that has coops list for a specific field and orientation
    if coops_df.empty:
        raise Exception('no coop is in the field-orientation. correct the field and orientation input')
    ind_items_df = pd.DataFrame(ind_items[my_ind], columns=['item_en_title']) # transform indicator items dictionary to dataframe

    coops_ind_items_df = coops_df.merge(ind_items_df,how='cross') # cross coops with indicator items
    
    final_df = coops_ind_items_df.merge(ind_data_df, how='left', on=['org_id','item_en_title']) # create final indicator value dataframe
    final_df = final_df.pivot(index=['org_id','national_id','org_name','field_id','orientation_id'], columns='item_en_title', values='value').reset_index()
    final_df.columns.name = None
    
    final_df[my_ind] = final_df.apply(lambda row : indicator(my_ind,row), axis=1)
    final_df = final_df.sort_values(by=my_ind, ascending=False).reset_index(drop=True)
    return final_df

# define whisker function

def whisker_func(ind_items_df_indicator, upper_ind_limit, lower_ind_limit):
    
    x = ind_items_df_indicator

    if (np.isnan(lower_ind_limit)) & (np.isnan(upper_ind_limit)):
        a = x
        upper_whisker = min(a.quantile(0.75) + 1.5*(a.quantile(0.75) - a.quantile(0.25)), a.max())
        lower_whisker = max(a.quantile(0.25) - 1.5*(a.quantile(0.75) - a.quantile(0.25)), a.min())
    
    if (np.isnan(lower_ind_limit)) & (~np.isnan(upper_ind_limit)):
        a = x[x < upper_ind_limit]
        upper_whisker = np.nan
        lower_whisker = max(a.quantile(0.25) - 1.5*(a.quantile(0.75) - a.quantile(0.25)), a.min())
        
    if (~np.isnan(lower_ind_limit)) & (np.isnan(upper_ind_limit)):
        a = x[x > lower_ind_limit]
        upper_whisker = min(a.quantile(0.75) + 1.5*(a.quantile(0.75) - a.quantile(0.25)), a.max())
        lower_whisker = np.nan
    if (~np.isnan(lower_ind_limit)) & (~np.isnan(upper_ind_limit)):
        a = x[(x > lower_ind_limit) & (x < upper_ind_limit)]
        upper_whisker = np.nan
        lower_whisker = np.nan
    

    
    return (upper_whisker, lower_whisker)
    
# define no outlier function

def no_outlier(row, my_ind, upper_whisker, lower_whisker, upper_ind_limit, lower_ind_limit):
#     try:

        if row[my_ind] <= lower_ind_limit:
            return lower_ind_limit

        elif row[my_ind] < lower_whisker:
            return lower_whisker

        elif row[my_ind] >= upper_ind_limit:
            return upper_ind_limit

        elif row[my_ind] > upper_whisker:
            return upper_whisker

        else:
            return row[my_ind]
#     except:
#         raise Exception('no outlier function error')
#         print('row[my_ind]: ', row[my_ind])
#         print('upper_whisker: ', upper_whisker)
#         print('lower_whisker: ', lower_whisker)
#         print('upper_ind_limit: ', upper_ind_limit)
#         display('lower_ind_limit: ', lower_ind_limit)

# define outlier minimum and maximum function

def ind_maximum(ind_items_df_indicator_no_outlier, top_score_base_my_ind, upper_ind_limit):
    
    if top_score_base_my_ind == 'upper_ind_limit': # if upper indicator limit is a base for the maximum score
        return upper_ind_limit
    else:
        return ind_items_df_indicator_no_outlier.max() # if the top score is based on the data

def ind_minimum(ind_items_df_indicator_no_outlier, bottom_score_base_my_ind, lower_ind_limit):
    
    if bottom_score_base_my_ind == 'lower_ind_limit': # if lower indicator limit is a base for the minimum score
        return lower_ind_limit
    else:
        return ind_items_df_indicator_no_outlier.min() # if the bottom score is based on the data
    
    
# define score functions

def score(row, my_ind, lower_ind_limit, upper_ind_limit, ind_min, ind_max, point, ind_direction, intercept, slope): 
    
    
    if (ind_direction == 1) & (row[my_ind + '_no_outlier'] == lower_ind_limit):
        return 0
    elif (ind_direction == -1) & (row[my_ind + '_no_outlier'] == upper_ind_limit):
        return round(point,2)
    elif ind_max - ind_min == 0:
        return round(point,2)
    else:
        return round(intercept*point + slope*point*(row[my_ind + '_no_outlier'] - ind_min) / (ind_max - ind_min),2)

# ----------------------------------------------------------------------------------

def indicator_score_value_analysis(items_prepared, ind_list_en, ind_items, ind_points, my_ind, my_field_id, my_orientation_id):
    
    ind_items_df = ind_items_func(my_ind, ind_items, items_prepared, my_field_id, my_orientation_id) # generate the indicator-item dataframe for a specific indicator-field-orientation
    
    # default input parameters
    upper_ind_limit = ind_list_en.loc[ind_list_en['ind_title'] == my_ind, 'ind_upper_limit'].values[0] # set upper indicator limit
    lower_ind_limit = ind_list_en.loc[ind_list_en['ind_title'] == my_ind, 'ind_lower_limit'].values[0] # set lower indicator limit
    top_score_base = ind_list_en.loc[ind_list_en['ind_title'] == my_ind, 'top_score_base'].values[0] # set top score limit of the indicator_no_outlier
    bottom_score_base = ind_list_en.loc[ind_list_en['ind_title'] == my_ind, 'bottom_score_base'].values[0] # set bottom score limit of the indicator_no_outlier
    ind_direction = ind_list_en.loc[ind_list_en.ind_title == my_ind, 'direction'].values[0]
    intercept = ind_list_en.loc[ind_list_en.ind_title == my_ind, 'intercept'].values[0]
    slope = ind_list_en.loc[ind_list_en.ind_title == my_ind, 'slope'].values[0]
    point = ind_points[my_ind]
    
    # calculate whiskers
    upper_whisker, lower_whisker = whisker_func(ind_items_df[my_ind], upper_ind_limit, lower_ind_limit) # calculate upper and lower whiskers
    
    # calculate no outliers
    ind_items_df[my_ind + '_no_outlier'] = ind_items_df.apply(lambda row : no_outlier(row,my_ind,upper_whisker,lower_whisker,upper_ind_limit,lower_ind_limit), axis=1) # generate no_outlier column
    
    # calculate indicator no outlier min and max values
    ind_max = ind_maximum(ind_items_df[my_ind + '_no_outlier'], top_score_base, upper_ind_limit) # calculate indicator max value
    ind_min = ind_minimum(ind_items_df[my_ind + '_no_outlier'], bottom_score_base, lower_ind_limit) # calculate indicator min value
    
    # override parameters
#     upper_ind_limit = 'not_defined'
#     lower_ind_limit = 'not_defined'
#     top_score_base = 'not_defined'
#     bottom_score_base = 'not_defined'
#     ind_direction = 'not_defined'
#     intercept = 'not_defined'
#     slope = 'not_defined'
    
    ind_items_df[my_ind + '_score'] = ind_items_df.apply(lambda row : score(row, my_ind, lower_ind_limit, upper_ind_limit, ind_min, ind_max, point, ind_direction, intercept, slope), axis=1) # generate score column
    return ind_items_df

def indicator_score_value(ind_items_df, my_ind):
    
    ind_items_df['ind_title'] = my_ind # create a column with rows showing the name of the indicator
    ind_items_df = ind_items_df.rename(columns={my_ind:'value',my_ind + '_score':'score'})[['org_id','field_id','orientation_id','ind_title','value','score']] # rename columns and keep necessary columns
    return ind_items_df
