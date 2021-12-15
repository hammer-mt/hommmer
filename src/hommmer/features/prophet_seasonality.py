import pandas as pd
import numpy as np
from fbprophet import Prophet
from prophet.diagnostics import performance_metrics, cross_validation

def prophet_seasonality(df, target_col, date_col, country="US", p=30, freq="D"):
    pred_df = df[[date_col, target_col]].copy()
    pred_df.rename(columns={date_col:'ds', target_col:'y'}, inplace=True)
    daily = True if freq == "D" else False
    m = Prophet(yearly_seasonality=True,weekly_seasonality=daily,seasonality_mode='multiplicative') #instantiate Prophet
    m.add_country_holidays(country_name=country)

    #fit the model
    m.fit(pred_df)

    # predict the future
    future = m.make_future_dataframe(periods=p, freq = 'D')

    #use the data in the future dataframe to predict y and insert it into a new dataframe 
    forecast = m.predict(future)

    #let's see how the prediction worked
    m.plot(forecast, figsize=(40,10))

    #let's see how the seasonality worked to predict the y
    m.plot_components(forecast)

    # Cross validate your performances
    df_cv = cross_validation(m, initial='400 days', period='200 days', horizon = '60 days')
    #define how many days of prediction have the lowest mape 

    df_p = performance_metrics(df_cv)

    return forecast, df_p
    