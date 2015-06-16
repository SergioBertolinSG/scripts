#!/usr/bin/env python

import paramiko
import sys
import urllib

usage = '''
        Execute the script with this parameters port for ssh connection.

	host  port user password
        '''

if len(sys.argv) < 4:
    print usage
    sys.exit()


host = str(sys.argv[1]) 
port = int(sys.argv[2])
user = str(sys.argv[3])
password = str(sys.argv[4])



transport = paramiko.Transport((host, port))
transport.connect(username = user, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)


filepath = '/opt/owncloud/data/owncloud.log'
localpath = './owncloud_{0}_{1}.log'.format(host, port)


sftp.get(filepath, localpath)


sftp.close()
transport.close()


