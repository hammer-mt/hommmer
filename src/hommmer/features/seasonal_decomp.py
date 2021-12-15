from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import pandas as pd
# https://juanitorduz.github.io/fb_prophet/

def seasonal_decomp(df, target_col, date_col, freq="D"):
    # freq == "W-Mon" or "W-Sun" or "D"
    pred_df = df[[date_col, target_col]].copy()
    pred_df.rename(columns={date_col:'ds', target_col:'y'}, inplace=True)
    pred_df = pred_df.set_index('ds').asfreq(freq)
    decomp_obj = seasonal_decompose(
        x=pred_df['y'],
        model='additive'
    )
    fig, ax = plt.subplots(4, 1, figsize=(12, 12))

    # Observed time series.
    decomp_obj.observed.plot(ax=ax[0])
    ax[0].set(title='observed')
    # Trend component. 
    decomp_obj.trend.plot(label='fit', ax=ax[1])
    ax[1].set(title='trend')
    # Seasonal component. 
    decomp_obj.seasonal.plot(label='fit', ax=ax[2])
    ax[2].set(title='seasonal')
    # Residual.
    decomp_obj.resid.plot(label='fit', ax=ax[3])
    ax[3].set(title='resid')

    fig.suptitle('Time Series Decomposition', y=1.01)
    plt.tight_layout()
    decomp_df = pd.DataFrame([decomp_obj.observed, decomp_obj.trend, decomp_obj.seasonal, decomp_obj.resid])
    decomp_df.fillna(0, inplace=True)
    return decomp_df