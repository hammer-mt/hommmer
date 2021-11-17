def lag(series, periods):
    return series.shift(periods).fillna(0)