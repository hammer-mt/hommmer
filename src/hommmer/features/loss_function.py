def loss_function(X_values, X_media, X_org):
    # X_media = {
    #   "labels": ["facebook", "tiktok"],
    #   "coefs": [6.454, 1.545],
    #   "drs": [0.6, 0.7]
    # }
    # X_org = {
    #   "labels": ["const"],
    #   "coefs": [-27.5],
    #   "values": [1]
    # }
    y = 0
    for i in range(len(X_values)):
        transform = X_values[i] ** X_media["drs"][i]
        contrib = X_media["coefs"][i] * transform
        y += contrib

    for i in range(len(X_org)):
        contrib = X_org["coefs"][i] * X_org["values"][i]
        y += contrib

    return -y