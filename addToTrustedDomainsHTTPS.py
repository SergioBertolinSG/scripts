#!/usr/bin/env python

import paramiko
import sys
import fileinput


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


filepath = '/opt/owncloud/config/config.php'
localpath = './config.php'
sftp.get(filepath, localpath)



processing_config = False

for line in fileinput.input('config.php', inplace=1):
  if line.startswith("    0 => '{0}:".format(host)):
    processing_config = True
  else:
    if processing_config:
      print '    1 => \'{0}:{1}\','.format(host, port-1)
    processing_config = False
  print line,

sftp.put(localpath, filepath)


sftp.close()
transport.close()




#FOR CHECKING IT IS EDITED WELL
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, password=password, port=port)


stdin, stdout, stderr = ssh.exec_command("sudo cat /opt/owncloud/config/config.php")
output = stdout.readlines()
for line in output:
	print line

