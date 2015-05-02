__author__ = 'pauloalmeida'

from boto.dynamodb2.table import *

users = Table.create('users',
    schema=[
        HashKey('username'),
        RangeKey('date_joined')
    ],
    throughput={
    'read':2,
    'write': 1,
    },
    indexes=[
        IncludeIndex('GenderIndex',
            parts=[
                HashKey('username'),
                RangeKey('date_joined')
            ],
            includes=['gender']
        ),
    ])

print users.describe()

