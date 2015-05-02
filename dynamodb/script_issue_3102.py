__author__ = 'pauloalmeida'

from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table

ddb = DynamoDBConnection(host='localhost',
                         port=8000,
                         is_secure=False,
                         aws_access_key_id='test',
                         aws_secret_access_key='bar')


table = Table.create("table",
                     schema=[HashKey('k')],
                     connection=ddb)