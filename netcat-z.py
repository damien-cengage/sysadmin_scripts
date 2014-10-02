import sys, socket, getopt

#
# Damien - Quick implementation of netcat -z -v in python
#

def checkport(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
    except:
        return False

    return True

myhost = sys.argv[1]
myport = sys.argv[2]

print "Checking host: %s port: %s" % (myhost, myport)

#result = checkport("mms.mongodb.com", 443)

result = checkport(myhost, int(myport))

print result
