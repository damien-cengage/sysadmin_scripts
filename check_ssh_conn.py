#!/usr/bin/env python
import crypto
import sys

#This is needed for a mac, on mac Crypto library gets compiled as crypto
#all other modules will look for Crypto
sys.modules['Crypto'] = crypto

import paramiko

import pycurl
import re
import sys
import os


server_group = sys.argv[1]
user = sys.argv[2]

def test_conn (hostname, username):
   try:
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(host)
      cmd = "ls /"
      ssh.exec_command(cmd)
      stdin, stdout, stderr = ssh.exec_command(cmd)
   #   print stdout.readlines()
      print "YES - %s - Connected and executed remote command with success" % hostname
   except paramiko.AuthenticationException:
      print "NO - %s - Authentication failed" % hostname
   except:
      print "NO - %s - Could not SSH" % hostname

def get_array_of_servers(server_group):
    f = '/tmp/machines.txt'
    myline = ""
    for line in open(f).readlines():
        if re.search(server_group, line):
            myline = line
    hello = re.split("=", myline)
    server_list = hello[1].replace("'", "")
    return re.split(",", server_list)

def curl_machines_to_tempfile():
    with open('/tmp/machines.txt', 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://monitor.mt.corp.web/cgi-bin/objects.cache.cgi')
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()

curl_machines_to_tempfile()        
server_array = get_array_of_servers(server_group)

for host in server_array:
   test_conn(host, user)

