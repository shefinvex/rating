# test on a single indicator for a specific field-orientation

my_ind = 'credit_score' # set the indicator to analyse
my_field_id = 8 # set the field
my_orientation_id = 7 # set the orientation
print('parameters table')
display(pd.DataFrame(ind_list_en.loc[ind_list_en.ind_title == my_ind]).iloc[:,13:])

print('indicator value and score table')


a = indicator_score_value_analysis(items_prepared, ind_list_en, ind_items, ind_points, my_ind, my_field_id, my_orientation_id)
display(a)

fig, ax = plt.subplots(1,2,figsize=(10,5), sharey=True)

sns.set_theme()
a.plot(kind='scatter', x=my_ind, y=my_ind + '_score', ax=ax[0], color='blue');
a.plot(kind='scatter', x=my_ind+'_no_outlier', y=my_ind + '_score', ax=ax[1], color='blue');
