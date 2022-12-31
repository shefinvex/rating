def aggregate_score_value(indicators_list, field_orientation_list, ind_list_en):
    
    operation_count = len(field_orientation_list) * len(indicators_list)
    percent_complete = 0
    aggregate_df = pd.DataFrame()
    
    for idx in range(len(field_orientation_list)):
        my_field_id = field_orientation_list.loc[idx, 'field_id']
        my_orientation_id = field_orientation_list.loc[idx, 'orientation_id']
        for my_ind in indicators_list:
            clear_output()
            print('currect process step')
            print('my_field_id: ', my_field_id, 'my_orientation_id: ', my_orientation_id)
            print('current indicator: ', my_ind)
            print('percent complete: ', '%', '%.0f' % percent_complete)
            a = indicator_score_value_analysis(items_prepared, ind_list_en, ind_items, ind_points, my_ind, my_field_id, my_orientation_id)
            b = indicator_score_value(a, my_ind)
            aggregate_df = pd.concat([aggregate_df,b])
            percent_complete += 100 / operation_count
            
    print('percent complete: ', '%', '%.0f' % percent_complete)
    
    aggregate_df = aggregate_df.merge(ind_list_en[['ind_title','type']], how='left', on='ind_title')[['org_id',	'field_id',	'orientation_id',	'ind_title', 'type', 'value', 'score']]	
    
    return aggregate_df
