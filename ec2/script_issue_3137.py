__author__ = 'paulo.rodenas'

import boto.ec2
ec2 = boto.ec2.connect_to_region('us-west-2')
ec2.get_all_instance_types()