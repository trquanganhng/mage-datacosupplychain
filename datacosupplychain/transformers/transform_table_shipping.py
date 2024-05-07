if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    shipping_info = data[['order_id', 'days_for_shipping_real', 'days_for_shipment_scheduled', 'delivery_status_id', 'shipping_date_dateorders', 'shipMode_id']].drop_duplicates(subset='order_id')
    
    shipping_info["row_id"] = shipping_info.reset_index().index + 1

    return shipping_info

