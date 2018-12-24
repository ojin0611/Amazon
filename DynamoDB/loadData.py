import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')#, endpoint_url="http://localhost:8000")

# table name
table = dynamodb.Table('ProductBarcode')

dir_name  = 'C:/Users/dongm/COSMOCHAIN/'
json_name= 'ProductBarcode.json'

json_data=open(dir_name + json_name, encoding='UTF8').read()
products = json.loads(json_data)#, encoding='utf-8')


# Input Start
for product in products:
    BARCODE = product['BARCODE']
    PRNM = product['PRNM']
    GLN = product['GLN']
    CONAMEK = product['CONAMEK']
    CLASSCODE = product['CLASSCODE']
    CLASSNAME4 = product['CLASSNAME4']

    print("Adding test:", BARCODE, PRNM)

    table.put_item(
       Item={
           'BARCODE': BARCODE,
           'PRNM': PRNM,
           'GLN': GLN,
           'CONAMEK': CONAMEK,
           'CLASSCODE': CLASSCODE,
           'CLASSNAME4': CLASSNAME4,
        }
    )