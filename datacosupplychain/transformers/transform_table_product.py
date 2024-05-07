if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    product_df = data[["product_card_id", "product_category_id", "product_description", "product_image",
                    "product_name", "product_price", "product_status"]].sort_values(by="product_card_id").drop_duplicates(subset="product_card_id")

    return product_df