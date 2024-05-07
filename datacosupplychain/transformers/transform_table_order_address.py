if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    order_address_df = data[['order_address_id', "order_city", "order_state", "order_country", "order_region", "market_id"]].drop_duplicates(subset='order_address_id')
   
    return order_address_df