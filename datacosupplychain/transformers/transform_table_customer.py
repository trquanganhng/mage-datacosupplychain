if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    customer_df = data[["customer_id", "customer_fname", "customer_lname", 
                        "customer_segment", "customer_email", "customer_address_id"]].drop_duplicates(subset="customer_id").sort_values(by="customer_id")

    return customer_df