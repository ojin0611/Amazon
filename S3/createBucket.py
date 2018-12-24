import boto3

bucket_name = 'cosmee-productbarcode'

s3 = boto3.client('s3')#, region_name='ap-northeast-2')
s3.create_bucket(Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'})

print('Create Bucket Complete :',bucket_name)

