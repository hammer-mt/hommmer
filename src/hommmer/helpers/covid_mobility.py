def covid_mobility(df, sub_region_1=None):
    if sub_region_1 is None:
        data = df[df['sub_region_1'].isnull()]
    else:
        data = df[df['sub_region_1'] == sub_region_1]
        data = df[df['sub_region_2'].isnull()]
    
    data.reset_index(inplace=True)
    return data[data.columns[9:]]