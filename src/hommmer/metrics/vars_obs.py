def vars_obs(df):
    # 7 - 10 observations per variable
    # https://storage.googleapis.com/pub-tools-public-publication-data/pdf/2d0395bc7d4d13ddedef54d744ba7748e8ba8dd1.pdf
    return df.shape[1] / df.shape[0] >= 7, df.shape[1] / df.shape[0]