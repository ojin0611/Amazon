from io import StringIO
import pandas as pd
import boto3

bucket = 'abxgh-test'
file_name = "sample.csv"
df = pd.read_csv(file_name)


csv_buffer = StringIO()
df.to_csv(csv_buffer)
s3 = boto3.resource('s3')
s3.Object(bucket, 'upload_sample.csv').put(Body=csv_buffer.getvalue())
print(file_name)

# put way 2
# s3 = boto3.client('s3') 
# s3.put_object(Body=output, Bucket=bucket_name, Key=new_file)




