if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    department_df = data[["department_id", "department_name"]].sort_values(by="department_id").drop_duplicates(subset="department_id")
    
    return department_df