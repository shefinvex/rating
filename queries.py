# generate the rating for a specific coop

rating_type = ['qualitative','quantitative']
indicators_list = ind_list_en.loc[ind_list_en['type'].isin(rating_type), 'ind_title'] 

field_orientation_list = pd.DataFrame({'field_id':[1], 'orientation_id':[1]}) # specific field and orientation
# field_orientation_list = field_orientation_all # all fields and orientations

coops_value_score_df = aggregate_score_value(indicators_list, field_orientation_list, ind_list_en)
coop_org_id = 149229
specific_coops_value_score_df = coops_value_score_df.loc[coops_value_score_df.org_id == coop_org_id].copy()
specific_coops_value_score_df.score = specific_coops_value_score_df.score.round(2)


item_mask = items_prepared.item_en_title.isin(ind_items['priority_partnership'])
items_prepared.loc[(items_prepared.org_id == 149229) & item_mask]


specific_coops_value_score_df
