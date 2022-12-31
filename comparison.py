# comparison with platform results
platform_quant_df = pd.read_csv('./input_data/platform_total_quantity.csv', usecols=[0,1])
platform_quant_df.columns = ['org_id', 'pl_quant_score']
platform_quant_df
platform_quality_df = pd.read_csv('./input_data/platform_total_quality.csv', usecols=[0,1])
platform_quality_df.columns = ['org_id', 'pl_quality_score']

a = total_score_df.round(2).merge(items_prepared[['org_id','national_id']].drop_duplicates(subset=['org_id','national_id']), how='left', on='org_id')
a = a.merge(platform_quant_df, how='left', on='org_id').merge(platform_quality_df, how='left', on='org_id')
a['pl_total_score'] = a['pl_quant_score'] + a['pl_quality_score']
a['quant_delta'] = a['pl_quant_score'] - a['quantitative']
a['quality_delta'] = a['pl_quality_score'] - a['qualitative']
a['total_delta'] = a['pl_total_score'] - a['total_score']

a = a.sort_values(by='total_delta', key=abs, ascending=False)
a
