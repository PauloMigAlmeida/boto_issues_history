__author__ = 'pauloalmeida'

import boto.sqs

conn = boto.sqs.connect_to_region("us-west-2")
queue = conn.get_queue('THE-CROSS-ACCOUNT-QUEUE', owner_acct_id='123456789012')

print queue.get_attributes()