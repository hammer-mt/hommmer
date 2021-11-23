def effect_share(contribution_df):
    return (contribution_df.sum()/contribution_df.sum().sum()).values