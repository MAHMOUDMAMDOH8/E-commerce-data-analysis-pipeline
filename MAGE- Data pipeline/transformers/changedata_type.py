import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    Dtype = {
        'Order ID': pd.Int64Dtype(),
        'Order Date': pd.to_datetime,
        'Order Date' : pd.to_datetime,
        'Sales' : float,
        'Quantity' : pd.Int64Dtype(),
        'Discount' : float,
        'Profit' : float,
        'Shipping Cost': float
    }

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
