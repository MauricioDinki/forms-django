import boto

import sys, os

from boto.s3.key import Key

LOCAL_PATH = './'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
print AWS_ACCESS_KEY_ID
bucket_name = 'django-forms'
# connect to the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)
# go through the list of files
bucket_list = bucket.list()
for l in bucket_list:
  keyString = "enviroment"
  l.get_contents_to_filename(LOCAL_PATH+keyString)
