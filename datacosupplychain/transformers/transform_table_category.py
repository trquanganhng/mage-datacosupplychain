if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    category_df = data[["category_id", "category_name"]].sort_values(by="category_id").drop_duplicates(subset="category_id")

    return category_df

