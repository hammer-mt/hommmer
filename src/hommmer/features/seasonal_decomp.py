from statsmodels.tsa.seasonal import seasonal_decompose
# https://juanitorduz.github.io/fb_prophet/

def seasonal_decomp(df, target_col, date_col):
    pred_df = df[date_col, target_col].copy()
    pred_df.rename(columns={date_col:'ds', target_col:'y'})
    decomposition_obj = seasonal_decompose(
        x=pred_df.set_index('ds'),
        model='additive'
    )
    return decomposition_obj