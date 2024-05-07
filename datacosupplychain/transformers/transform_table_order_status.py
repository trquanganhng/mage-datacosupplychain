import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    order_status_df = data[['order_status_id', 'order_status_name']].drop_duplicates()
        
    return order_status_df