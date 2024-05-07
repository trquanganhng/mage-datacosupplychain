if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    order_df = data[['row_id', 'order_id', 'order_date_dateorders', 'order_item_cardprod_id',
       'order_item_id', 'order_item_discount', 'order_item_discount_rate',
       'order_item_product_price', 'order_item_profit_ratio',
       'order_item_quantity', 'sales', 'order_item_total', 'order_customer_id',
       'department_id', 'order_status_id', 'order_address_id']]

    return order_df