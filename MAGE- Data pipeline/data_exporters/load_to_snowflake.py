from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_snowflake(data: DataFrame, **kwargs) -> None:
    table_name = 'FactSales'
    database = 'ECOMMERCE'
    schema = 'PUBLIC'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'dev-snow'

    with Snowflake.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        loader.export(
            DataFrame(data['FactSales']),
            table_name,
            database,
            schema,
            if_exists='replace',  # Specify resolution policy if table already exists
        )
