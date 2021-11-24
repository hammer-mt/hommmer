from hommmer.metrics import *

def check_metric(metric_label, model):
    return {
        'nrmse': nrmse(model.y_train, model.predict()),
        'rsquared': rsquared(model.y_train, model.predict()),
        'decomp-rssd': decomp_rssd(effect_share(model.contribution()[model.media_labels]), spend_share(model.X_train[model.media_labels]))
    }[metric_label]