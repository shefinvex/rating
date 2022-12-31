# define function

def total_score(df, ind_list_en):
    if 'type' not in df.columns:
        df = df.merge(ind_list_en[['ind_title','type']], how='left', on='ind_title')
    
    total_score_df = df.groupby(['org_id','field_id','orientation_id','type'])['score'].sum().reset_index()
    total_score_df = total_score_df.pivot(index=['org_id','field_id','orientation_id'], columns='type', values='score').reset_index()
    total_score_df.columns.name = None
    total_score_df['total_score'] = total_score_df['qualitative'] + total_score_df['quantitative']
    total_score_df = total_score_df.sort_values(by='total_score', ascending=False).reset_index(drop=True)
    return total_score_df
