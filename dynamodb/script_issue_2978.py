__author__ = 'pauloalmeida'

from boto.dynamodb2.table import *
import time

print 'Creating table'

users = Table.create('users',
    schema=[
        HashKey('username'),
        RangeKey('date_joined')
    ],
    throughput={
    'read':2,
    'write': 1,
    },
    global_indexes=[
        GlobalKeysOnlyIndex('GenderIndexGSI',
            parts=[
                HashKey('username'),
                RangeKey('date_joined')
            ],
            throughput={
                'read': 2,
                'write': 1
            })
    ])

time.sleep(60)

print users.describe()

print 'Deleting GSI'
users.delete_global_secondary_index('GenderIndexGSI')

time.sleep(60)

print users.describe()

# users = Table('users')
users.delete()