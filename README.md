sysadmin_scripts
================

Scripts

---------------------------------------------------------------------------------------
check_ssh_conn.py -

Checks ssh connectivity to a pool of servers for a user.

Pulls from http://monitor.mt.corp.web/cgi-bin/objects.cache.cgi

usage:

$ python check_ssh_conn.py <server_type> <user>

example, check ssh connectivity for all vmware servers:

$ python check_ssh_conn.py vmware dmichalosky
---------------------------------------------------------------------------------------
