# Generate List of All Fields and Orientations
field_orientation_all = items_prepared.drop_duplicates(subset=['field_id','orientation_id'])[['field_id','orientation_id']].sort_values(by=['field_id','orientation_id']).reset_index(drop=True)
display(field_orientation_all.head(1))
print('number of field-orientations: ', field_orientation_all.shape[0])
