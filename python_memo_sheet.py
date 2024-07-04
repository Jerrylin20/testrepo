#Grouping by attributes
df_group = df[['attribute_1', 'attribute_2', ...]]

#GroupBy statements
##Group by a single attribute
df_group = df_group.groupby(['attribute_1'], as_index=False).mean()
##Group by multiple attributes
df_group = df_group.groupby(['attribute_1','attribute_2'], as_index=False).mean()

#Pivot tables
grouped_pivot=df_group.pivot(index='attribute_1', columns='attribute_2')
