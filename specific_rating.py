# specific field and orientation for quant, qual or total rating

rating_type = ['qualitative','quantitative']
indicators_list = ind_list_en.loc[ind_list_en['type'].isin(rating_type), 'ind_title'] 
field_orientation_list = pd.DataFrame({'field_id':[4], 'orientation_id':[112]}) # specific field and orientation
filename = 'f_' + str(field_orientation_list.iloc[0,0]) + '_' + 'ori_' + str(field_orientation_list.iloc[0,1])

specific_value_score_df = aggregate_score_value(indicators_list, field_orientation_list, ind_list_en)
specific_value_score_df

specific_value_score_df.to_csv('./output/' + filename + '.csv') # write to excel only if specific part of rating is generated
