if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    customer_address = data[["customer_address_id", "customer_city", "customer_country", 
                             "customer_state", "customer_street", "customer_zipcode"]].sort_values(by="customer_address_id")
    
    return customer_address