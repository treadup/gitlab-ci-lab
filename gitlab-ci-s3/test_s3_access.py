import boto3

BUCKET = "foo"
KEY = "thekey"

client = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",
    aws_access_key_id="accesskey",
    aws_secret_access_key="secretkey",
    region_name="us-east-1",
)

client.create_bucket(Bucket=BUCKET)

client.put_object(
    Bucket=BUCKET,
    Body="Hello World".encode("utf-8"),
    ContentType="text/plain; charset=utf-8",
    Key=KEY,
)

response = client.get_object(Bucket=BUCKET, Key=KEY)
content = response["Body"].read().decode("utf-8")

if content == "Hello World":
    print("Succesfully wrote and read data from minio")
else:
    print("There was an error trying to write and read data from minio")
    exit(1)
