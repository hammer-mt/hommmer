def categorize_campaigns(campaign_name, categories=None):
    if categories is None:
        categories = {
            "prospecting": ['prosp'],
            "remarketing": ['remar', 'retar']
        }

    campaign_name = campaign_name.lower()

    campaign_category = "uncategorized"

    for category, containing in categories.items():
        for text in containing:
            if text in campaign_name:
                campaign_category = category

    return campaign_category