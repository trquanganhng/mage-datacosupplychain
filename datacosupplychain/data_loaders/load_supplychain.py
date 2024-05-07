import io
import pandas as pd
import requests
from pandas import DataFrame


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(**kwargs) -> DataFrame:

    url = 'https://github.com/trquanganhng/DataCoSupplyChain/releases/download/Download/DataCoSupplyChainDataset.csv?raw=True'

    supplychain_dtypes = {
        'Type' : str,
        'Days for shipping (real)' : pd.Int64Dtype(),
        'Days for shipment (scheduled)' : pd.Int64Dtype(),
        'Benefit per order' : float,
        'Sales per customer' : float,
        'Delivery Status' : str,
        'Late_delivery_risk' : pd.Int64Dtype(),
        'Category Id' : pd.Int64Dtype(),
        'Category Name' : str,
        'Customer City' : str,
        'Customer Country' : str,
        'Customer Email' : str,
        'Customer Fname' : str,
        'Customer Id' : pd.Int64Dtype(),
        'Customer Lname' : str,
        'Customer Password' : str,
        'Customer Segment' : str,
        'Customer State' : str,
        'Customer Street' : str,
        'Customer Zipcode' : str,
        'Department Id' : pd.Int64Dtype(),
        'Department Name' : str,
        'Latitude' : float,
        'Longitude' : float,
        'Market' : str,
        'Order City' : str,
        'Order Country' : str,
        'Order Customer Id' : pd.Int64Dtype(),       
        'Order Id' : pd.Int64Dtype(),
        'Order Item Cardprod Id' : pd.Int64Dtype(),
        'Order Item Discount' : float,
        'Order Item Discount Rate' : float,
        'Order Item Id' : pd.Int64Dtype(),
        'Order Item Product Price' : float,
        'Order Item Profit Ratio' : float,
        'Order Item Quantity' : pd.Int64Dtype(),
        'Sales' : float,
        'Order Item Total ' : float,
        'Order Profit Per Order'
        'Order Region' : str,
        'Order State' : str,
        'Order Status' : str,
        'Product Card Id' : pd.Int64Dtype(),
        'Product Category Id' : pd.Int64Dtype(),
        'Product Description' : str,
        'Product Image' : str,
        'Product Name' : str,
        'Product Price' : float,
        'Product Status' : pd.Int64Dtype(), 
        'Shipping Mode' : str,
    }
    parse_dates = ['order date (DateOrders)', 'shipping date (DateOrders)']
    return pd.read_csv(url, encoding='ISO-8859-1', sep=",",
                dtype=supplychain_dtypes, parse_dates=parse_dates)


@test
def test_output(df) -> None:
    assert df is not None, 'The output is undefined'
