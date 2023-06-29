import boto3
import bottle
import os

APP_BUCKET = os.getenv('APP_BUCKET')
APP_KEY = os.getenv('APP_KEY')
APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
APP_PORT = os.getenv('APP_PORT', '8000')

s3 = boto3.client('s3')

@bottle.route('/')
def index():
    data = s3.get_object(Bucket=APP_BUCKET, Key=APP_KEY)
    contents = data['Body'].read()
    return contents.decode('utf-8')

if __name__ == '__main__':
    bottle.run(host=APP_HOST, port=int(APP_PORT))
