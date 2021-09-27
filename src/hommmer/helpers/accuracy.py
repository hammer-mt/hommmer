import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def accuracy(y_actual, y_pred, y_label, nrmse):
    # set up figure and subplots
    fig, ax = plt.subplots(figsize=(14,8), nrows=2, ncols=1, gridspec_kw={'height_ratios': [3, 1]})
    
    # create plot df
    plot_df = pd.DataFrame()
    plot_df['Actual'] = y_actual
    plot_df['Predicted'] = y_pred
    plot_df['Error'] = (y_pred - y_actual) / y_actual * 100
    
    # plot actual vs predicted on grid
    plot_df[['Actual', 'Predicted']].plot(ax=ax[0], ylabel=y_label)

    ax[0].annotate(f'NRMSE = {nrmse}', xy=(0.05, 0.92), xycoords='axes fraction')

    ax[0].legend(loc="upper center", bbox_to_anchor=(0.5, 1.12), ncol=2)
    ax[0].grid(True, which='both')
    
    # plot error on grid
    plot_df[['Error']].plot(ax=ax[1], color='red')
    ax[1].grid(True, which='both')
    ax[1].legend(loc="upper center", bbox_to_anchor=(0.5, 1.35), ncol=2)
    fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax[1].yaxis.set_major_formatter(yticks)
    
    # show plots
    fig.autofmt_xdate(rotation=45)
    plt.gcf().suptitle("Actual vs Predicted", fontsize=20)
    
    plt.show()