#!/usr/bin/env python

import paramiko
import sys
import urllib

usage = '''
        Execute the script with this parameters port for ssh connection.
	host  port user password patchnumber
        '''

if len(sys.argv) < 5:
    print usage
    sys.exit()


host = str(sys.argv[1]) 
port = int(sys.argv[2])
user = str(sys.argv[3])
password = str(sys.argv[4])
patch = int(sys.argv[5])

github_url = 'http://github.com/owncloud/core/pull/'



urllib.urlretrieve ("{0}{1}.patch".format(github_url,patch), "{0}.patch".format(patch))

transport = paramiko.Transport((host, port))
transport.connect(username = user, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)


filepath = '/opt/owncloud/{0}.patch'.format(patch)
localpath = './{0}.patch'.format(patch)


sftp.put(localpath, filepath)


sftp.close()
transport.close()



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, password=password, port=port)

#PATCH IS NOT INSTALLED IN THE DOCKERS BY DEFAULT
stdin, stdout, stderr = ssh.exec_command("apt-get update && apt-get install patch")
output = stdout.readlines()
for line in output:
	print line


stdin, stdout, stderr = ssh.exec_command("cd /opt/owncloud && patch -p1 < {0}.patch".format(patch))
output = stdout.readlines()
for line in output:
	print line

