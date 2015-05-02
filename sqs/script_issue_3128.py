__author__ = 'pauloalmeida'

import boto.sqs
from boto.sqs.queue import Queue
from boto.compat import json

conn = boto.sqs.connect_to_region("us-west-2")
regularQueue = conn.create_queue('BOTO-QUEUE-TEST');
deadLetterQueue = conn.create_queue('BOTO-QUEUE-DEADLETTER-TEST');

print regularQueue.get_attributes()

regularQueue.set_attribute('DelaySeconds', 900)
regularQueue.set_attribute('MaximumMessageSize', 1024)
regularQueue.set_attribute('MessageRetentionPeriod', 1209600)
regularQueue.set_attribute('VisibilityTimeout', 43200)
regularQueue.set_attribute('ReceiveMessageWaitTimeSeconds', 20)


regularQueue.set_attribute('RedrivePolicy', json.dumps({'maxReceiveCount': 5, 'deadLetterTargetArn': deadLetterQueue.get_attributes('QueueArn').current_value}))

print regularQueue.get_attributes()

regularQueue.delete()
deadLetterQueue.delete()