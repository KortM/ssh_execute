from socket import socket
from paramiko import SSHClient, MissingHostKeyPolicy, AutoAddPolicy
import time
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('176.32.0.1', username='root', password='Mar02031812', allow_agent=False, look_for_keys=False)
channel = client.get_transport().open_session()
channel.get_pty()
channel.settimeout(5)
channel.exec_command('/opt/VPNagent/bin/auth_login')
channel.send('kort\n')
channel.send('Mar02031812\n')
channel.send('configure\n')
channel.send('cscons\n')
time.sleep(3)
channel.send('csp\n')
channel.send('conf t\n')
channel.send('enable password Mar02031812\n')
#channel.send('Mar02031812\n')
time.sleep(2)
channel.send('end\n')
channel.send('terminal length 100\n')
channel.send('sh run\n')
channel.send(' \n')
data = ''
while True:
    try:
        part = channel.recv(1024).decode('utf-8')
        data +=part
    except Exception as e:
        print(e)
        break
print(data)

    