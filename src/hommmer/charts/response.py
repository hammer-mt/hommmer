from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
def predict_and_plot_response(df, interval, tranformer, **kwargs):
    df['spend_transformed'] = tranformer(df['spend'], **kwargs)
    predict_y = 'conversions' # variable you're predicting
    dependent_X = ['spend_transformed'] # variables you're using to predict 

    y = df[predict_y] 
    X = df[dependent_X] 

    model = linear_model.LinearRegression()
    model.fit(X, y)
    
    xmax = df['spend'].max()
    xmax_round = xmax if xmax % interval == 0 else xmax + interval - xmax % interval
    
    resp_df = pd.DataFrame({
        "spend": range(interval, int(xmax_round), interval)
    })
    
    resp_df['spend_transformed'] = tranformer(resp_df['spend'], **kwargs)
    X_resp = resp_df[['spend_transformed']]
    resp_df['forecast'] = model.predict(X_resp)
    resp_df['forecast'] = resp_df['forecast'].round().astype(int)
    resp_df['CPA'] = round(resp_df['spend'] / resp_df['forecast'],2)

    resp_df.plot(x='spend', y='forecast', kind='line', figsize=(10,5), style='.-')
    plt.title('Response Curve', y=1.12)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.12), ncol=2)
    r_sq = round(model.score(X, y), 2)
    plt.annotate(f'R-squared = {r_sq}', xy=(0.05, 0.90), xycoords='axes fraction')
    plt.annotate(f'Transform = {tranformer.__name__}', xy=(0.05, 0.80), xycoords='axes fraction')
    plt.annotate(f'{"".join([f"{k}={v} " for k,v in kwargs.items()])}', xy=(0.05, 0.70), xycoords='axes fraction')
    
    plt.xticks(df.index) # force all x values to show
    plt.ylabel('Conversions')

    plt.show();
    return resp_df