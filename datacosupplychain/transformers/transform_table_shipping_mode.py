import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    shipping_mode_df = data[['shipMode_id', 'shipMode_name']].drop_duplicates()
    
    return shipping_mode_df
