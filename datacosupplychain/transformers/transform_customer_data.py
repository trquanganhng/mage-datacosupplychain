if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    customer_info = data[["customer_id", "customer_fname", "customer_lname", 
                          "customer_segment", "customer_email", "customer_city", 
                          "customer_country", "customer_state", "customer_street", 
                          "customer_zipcode"]].drop_duplicates(subset=["customer_id"])

    customer_info["customer_address_id"] = customer_info.reset_index().index + 1
    
    return customer_info