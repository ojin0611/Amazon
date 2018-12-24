import boto3
import botocore

BUCKET_NAME = 'cosmee-productbarcode' # 내 bucket
KEY = 'cosmochain_team.png' # bucket 안의 파일 이름

dir_name  = 'C:/Users/dongm/COSMOCHAIN/'
output_name = 'fileFromS3.png'

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, dir_name + output_name)
    print('file download complete! -', output_name)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
        
