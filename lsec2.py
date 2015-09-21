#!/usr/bin/env python
import boto.ec2
import sys

'''
USAGE: lsec2 [filter]
    prints all instances (optionally filtered by name by the `filter` param) and their id, Name, instance type, and DNS.
'''

def get_ec2_instances(region, name_filter=""):
    ec2_conn = boto.ec2.connect_to_region(region)
    instances = ec2_conn.get_all_instances()
    for instance in instances:
        i = instance.instances[0]
        if name_filter in i.tags.get('Name', ''):
            print "{:<10} {:<40} {:<10} {:<20}".format(i.id, i.tags.get('Name', ''), i.instance_type,
                                                       i.dns_name or "No DNS name")

if __name__ == "__main__":
    # Argument: instance name filter
    get_ec2_instances('us-east-1', *sys.argv[1:])
