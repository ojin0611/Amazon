import boto3

# Create an S3 client
s3 = boto3.client('s3')

# directory + filename 을 넣고 filename으로 저장
dir_name  = 'C:/Users/dongm/COSMOCHAIN/'
filename = 'ProductBarcode.json'
bucket_name = 'cosmee-productbarcode'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(dir_name+filename, bucket_name, filename)

print('Upload Complete! - ',filename)