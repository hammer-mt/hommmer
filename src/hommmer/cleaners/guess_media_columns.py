def guess_media_columns(columns):
    guesses = ['cost', 'spend', 'impression', 'spent', 'clicks']
    columns = [x.lower() for x in columns]
    media_columns = []
    for x in guesses:
        for y in columns:
            if x in y:
                media_columns.append(y)

    return media_columns