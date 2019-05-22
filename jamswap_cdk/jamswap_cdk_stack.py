from aws_cdk import cdk
from aws_cdk import (
    aws_dynamodb as dynamodb
)


class JamswapCdkStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)

        stage = "DEV"

        models_table = dynamodb.Table(self,f"JamSwapModels{stage}", 
            table_name=f"JamSwapModels{stage}", 
            partition_key={ "name": 'id', "type": dynamodb.AttributeType.String },
            sort_key = { "name": 'slug', "type": dynamodb.AttributeType.String },
            billing_mode= dynamodb.BillingMode.Provisioned,
            read_capacity=1,
            write_capacity=1,
        )

        makes_table = dynamodb.Table(self,f"JamSwapMakes{stage}", 
            table_name=f"JamSwapMakes{stage}", 
            partition_key={ "name": 'id', "type": dynamodb.AttributeType.String },
            sort_key = { "name": 'slug', "type": dynamodb.AttributeType.String },
            billing_mode= dynamodb.BillingMode.Provisioned,
            read_capacity=1,
            write_capacity=1,
        )

        category_table = dynamodb.Table(self,f"JamSwapCategory{stage}", 
            table_name=f"JamSwapCategory{stage}", 
            partition_key={ "name": 'id', "type": dynamodb.AttributeType.String },
            billing_mode= dynamodb.BillingMode.Provisioned,
            read_capacity=1,
            write_capacity=1,
        )

        category_table.add_global_secondary_index(
            partition_key={ "name": 'category_slug', "type": dynamodb.AttributeType.String },
            read_capacity=1,
            write_capacity=1, 
            index_name= "category_slug_gsi",
            projection_type=dynamodb.ProjectionType.All
        )
        
        # The code that defines your stack goes here
