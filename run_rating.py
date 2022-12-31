# generate the rating for all the fields and orientations

rating_type = ['qualitative','quantitative']
indicators_list = ind_list_en.loc[ind_list_en['type'].isin(rating_type), 'ind_title'] 
field_orientation_list = field_orientation_all # all fields and orientations

prompt = input('Are you sure to perform the whole rating?\n It may take about 2 hours.\ntype yes or no.\n')

if prompt == 'yes':
    value_score_df = aggregate_score_value(indicators_list, field_orientation_list, ind_list_en)
    
    # store results: determine the file name to store the results of rating

    if (field_orientation_list == field_orientation_all) & (indicators_list == ind_list_en.loc[ind_list_en['type'].isin(['quantitative','qualitative']), 'ind_title']):
        value_score_df.to_csv('./output/value_score.csv') # write to excel only if the complete rating is generated
    elif (field_orientation_list == field_orientation_all) & (indicators_list == ind_list_en.loc[ind_list_en['type'].isin(['quantitative']), 'ind_title']):
        value_score_df.to_csv('./output/quant_value_score.csv') # write to excel only if the quantitative rating is generated
    elif (field_orientation_list == field_orientation_all) & (indicators_list == ind_list_en.loc[ind_list_en['type'].isin(['qualitative']), 'ind_title']):
        value_score_df.to_csv('./output/quality_value_score.csv') # write to excel only if the qualitative rating is generated
    else:
        print('no data')

else:
    print('Rating run rejected by the user')
