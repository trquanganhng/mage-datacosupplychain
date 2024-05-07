import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    delivery_status_df = data[['delivery_status_id', 'delivery_status_name']].drop_duplicates()
  
    return delivery_status_df