# get
import pandas as pd
import boto3

bucket = "abxgh-test"
file_name = "sample.csv"

s3 = boto3.client('s3') 
# 's3' is a key word. create connection to S3 using default config and all buckets within S3

obj = s3.get_object(Bucket= bucket, Key= file_name) 
# get object and file (key) from bucket

initial_df = pd.read_csv(obj['Body']) # 'Body' is a key word
print(initial_df['이름'])




# put
# s3.put_object(Body=output, Bucket=bucket_name, Key=new_file)