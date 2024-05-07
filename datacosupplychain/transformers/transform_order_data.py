if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    order_info = data[["order_id", "order_date_dateorders", "order_item_cardprod_id", 
                       "order_item_id", "order_item_discount", "order_item_discount_rate", 
                       "order_item_product_price", "order_item_profit_ratio", "order_item_quantity", 
                       "sales", "order_item_total", "order_customer_id", "department_id", 
                       "order_status_id", "order_city", "order_state", "order_country", "order_region", "market_id"]]

    order_info["row_id"] = order_info.reset_index().index + 1

    # Concatenate address columns into a single string
    order_info['address_combined'] = order_info[['order_city', 'order_state', 'order_country', 'order_region', 'market_id']].astype(str).agg('-'.join, axis=1)

    # Create a mapping of unique address combinations to unique IDs
    address_id_mapping = {address: idx + 1 for idx, address in enumerate(order_info['address_combined'].unique())}

    # Map the address combinations to their respective IDs
    order_info['order_address_id'] = order_info['address_combined'].map(address_id_mapping)
    
    return order_info
