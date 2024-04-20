import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Dim Data
    DimDate = data['Order Date'].drop_duplicates().reset_index(drop=True)
    DimDate = pd.DataFrame(DimDate)
    DimDate['year'] = DimDate['Order Date'].dt.year
    DimDate['month'] = DimDate['Order Date'].dt.month
    DimDate['Day'] = DimDate['Order Date'].dt.day
    DimDate['Day Name'] = DimDate['Order Date'].dt.day_name()
    DimDate['Month Name'] = DimDate['Order Date'].dt.month_name()
    DimDate['DateID'] = DimDate.index
    DimDate = DimDate[['DateID','Order Date','year','month','Day','Day Name','Month Name']]

    # DIM Customer

    DimCustomers = data[['Customer ID','Customer Name','Segment']].drop_duplicates().reset_index(drop=True)

    # Dim Market 

    DimMarket = data[['LOC ID','Market','Region','Country','State','City']].drop_duplicates().reset_index(drop=True)

    # Dim Product 
    
    DimProduct = data[['Product ID','Product Name','Sub-Category','Category']].drop_duplicates().reset_index(drop=True)

    # Fact sales 
    FactSales = data[['Row ID','Order ID','Order Date','Customer ID','Ship Mode','LOC ID','Product ID','Sales','Quantity','Discount','Profit','Shipping Cost']]
    FactSales = pd.merge(FactSales, DimDate, on='Order Date', how='left')
    FactSales = FactSales[['Row ID', 'Order ID', 'DateID', 'Ship Mode','Customer ID','LOC ID', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost']]


    return {
        "DimDate":DimDate.to_dict(orient="dict"),
        "DimCustomers":DimCustomers.to_dict(orient="dict"),
        "DimMarket":DimMarket.to_dict(orient="dict"),
        "DimProduct":DimProduct.to_dict(orient="dict"),
        "FactSales":FactSales.to_dict(orient="dict")
    }
    
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
