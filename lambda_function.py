import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        # Copy objects/current bucket info
        src_cpy = {
            'Bucket': bucket,
            'Key': key
        }

        # Copy objects to backup bucket
        backup_bucket = 'cis4010-oyako-backup'
        s3.copy_object(CopySource=src_cpy, Bucket=backup_bucket, Key=key)
        print(key + " copied to cis4010-oyako-bucket")

        response = s3.get_object(Bucket=bucket, Key=key)
        print(key + " has been uploaded to cis4010-oyako")

        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
