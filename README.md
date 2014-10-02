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

netcat-z.py

Implementation of netcat -z -v for servers where netcat is not installed.

usage:
$ python netcat-z.py <host> <port>

example, check to see if port 443 is open on mms.mongodb.com

$ python netcat-z.py mms.mongodb.com 443
Checking host: mms.mongodb.com port: 443
True

---------------------------------------------------------------------------------------
