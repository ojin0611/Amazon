import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')#, endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='ProductBarcode',
    KeySchema=[
        {
            'AttributeName': 'BARCODE',
            'KeyType': 'HASH'  #Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'BARCODE',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 200
    }
)

print("Table status:", table.table_status)