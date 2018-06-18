import time
import serial
import paramiko


# def createSSHClient(server, port, user, password):
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(server, port, user, password)
#     return client

# ssh = createSSHClient("10.77.3.120", 22, "poppy", "poppy")
# scp = SCPClient(ssh.get_transport())


# import os
# os.system("scp data poppy@10.77.3.120:/home/pi/poppy_project/game_code/data")

# f = open('data', 'w')
# f.write(5)
# f.write(100)
# f.write(200)
# f.close()
# scp('data','/home/pi/poppy_project/game_code/data')

import os
import paramiko

ssh = paramiko.SSHClient() 
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect("10.77.3.120", username="poppy", password="poppy")
sftp = ssh.open_sftp()
sftp.put("data", "/home/pi/poppy_project/game_code/data")
sftp.close()
ssh.close()