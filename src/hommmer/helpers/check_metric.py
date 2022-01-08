from hommmer.metrics import *

def check_metric(metric_label, model):
    X_test = model.X_test
    y_test = model.y_test
    y_pred = model.predict(X=X_test)
    
    if metric_label == 'nrmse':
        return nrmse(y_test, y_pred)
    elif metric_label == 'rsquared':
        return rsquared(y_test, y_pred)
    elif metric_label == 'decomp-rssd':
        contrib_df = model.contribution()[model.media_labels]
        media_X_df = model.X_actual[model.media_labels]
        return decomp_rssd(effect_share(contrib_df), spend_share(media_X_df))
    elif metric_label == 'cond-no':
        return condition_number(model.X_train)
    elif metric_label == 'mape':
        return mape(y_test, y_pred)