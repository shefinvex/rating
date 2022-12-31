# Create Total Score Either from Cache or Database

# Total rating total score
try:
    total_score_df = total_score(value_score_df, ind_list_en)
except:
    value_score_df = pd.read_csv('./output/value_score.csv')
    total_score_df = total_score(value_score_df, ind_list_en)

# OR

# Specific rating total score
try:
    specific_total_score_df = total_score(specific_value_score_df, ind_list_en)
except:
    specific_total_score_df = pd.read_csv('./output/' + filename + '.csv')
    specific_total_score_df = total_score(pd.read_csv('./output/' + filename + '.csv'), ind_list_en)
