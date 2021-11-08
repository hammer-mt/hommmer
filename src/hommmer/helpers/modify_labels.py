def modify_labels(text, labels, prefix=False, sep=" | "):
    modified_labels = []
    for x in labels:
        if prefix:
            modified_labels.append(f"{text}{sep}{x}")
        else:
            modified_labels.append(f"{x}{sep}{text}")