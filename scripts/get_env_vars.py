import boto

import os

from boto.s3.key import Key

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = 'django-forms'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)
k = Key(bucket, 'enviroment')
k.get_contents_to_filename('enviroment')
print "Downloading enviroment ..."
