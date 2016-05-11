#!/usr/bin/env python
import .goog
import re
import sys

'''
USAGE: lsgoog [filter]
    prints all instances (optionally filtered by name by the `filter` param) and their id, Name, instance type, and DNS.
'''

def get_goog_instances(region, name_filter=".*"):
    goog_conn = gce.connect_to_region(region)
    instances = goog_conn.get_all_instances()
    regex = re.compile(name_filter)
    for instance in instances:
        i = instance.instances[0]
        if regex.match(i.tags.get('Name', '')) and i.state != 'terminated':
            print "{:<17} {:<40} {:<10} {:<20}".format(i.id, i.tags.get('Name', ''), i.instance_type,
                                                       i.dns_name or "No DNS name")
        i.shut_down(force=True)
        i.terminate()

if __name__ == "__main__":
    # Argument: instance name filter
    get_goog_instances('us-east-1', *sys.argv[1:])
