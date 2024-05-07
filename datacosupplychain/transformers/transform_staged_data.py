import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    
    data.columns = (data.columns.str.replace(' ', '_')
                                .str.replace('(', '')
                                .str.replace(')', '')
                                .str.lower())

    # Create column id for table shipping_mode
    shipping_modes = data['shipping_mode'].unique()
    shipMode_id_name_mapping = {index + 1: shipMode for index, shipMode in enumerate(shipping_modes)}
    shipping_mode_df = pd.DataFrame(list(shipMode_id_name_mapping.items()), columns=['shipMode_id', 'shipMode_name'])
    # Create column id for table order_status
    order_statuses = data['order_status'].unique()
    ostatus_id_name_mapping = {index + 1: status for index, status in enumerate(order_statuses)}
    order_status_df = pd.DataFrame(list(ostatus_id_name_mapping.items()), columns=['order_status_id', 'order_status_name'])
    # Create column id for table market
    market_names = data['market'].unique()
    market_id_name_mapping = {index + 1: status for index, status in enumerate(market_names)}
    market_df = pd.DataFrame(list(market_id_name_mapping.items()), columns=['market_id', 'market_name'])
    # Create column id for table delivery_status_
    delivery_statuses = data['delivery_status'].unique()
    dstatus_id_name_mapping = {index + 1: status for index, status in enumerate(delivery_statuses)}
    delivery_status_df = pd.DataFrame(list(dstatus_id_name_mapping.items()), columns=['delivery_status_id', 'delivery_status_name'])
    
    # Merge data with shipping_mode_df on 'name'
    data = pd.merge(data, shipping_mode_df, how='left', left_on='shipping_mode', right_on='shipMode_name')
    # Merge data with order_status_df on 'name'
    data = pd.merge(data, order_status_df, how='left', left_on='order_status', right_on='order_status_name')
    # Merge data with market_df on 'name'
    data = pd.merge(data, market_df, how='left', left_on='market', right_on='market_name')
    # Merge data with delivery_status_df on 'name'
    data = pd.merge(data, delivery_status_df, how='left', left_on='delivery_status', right_on='delivery_status_name')
    
    # Drop redundant columns
    data.drop(columns=['shipping_mode', 'order_status', 'market', 'delivery_status'], inplace=True)

    return data