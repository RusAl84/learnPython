import paramiko
import time

# ssh_key_location = "/your/private/key/location.pem"
server_ip = "192.168.151.224"
username = "rusal"
password = "12345!"   # If you will use private key, you don't have fill it.

# p_key = paramiko.RSAKey.from_private_key_file(ssh_key_location)
con = paramiko.SSHClient()
con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
con.connect(hostname = server_ip, username = username, password = password)
# con.connect(hostname = server_ip, username = username, password = password, pkey = p_key)
print("Connected")
time.sleep(1)

commands = ["ls -al", "ls -alh"]
command = "python3 app.py"
time.sleep(1)
# If you have only one command, you have to use it.
print("Executing {$",command,"}")
stdin , stdout, stderr = con.exec_command(command)
print(stdout.readlines())
print("===== Errors ======")
print(stderr.readlines())
time.sleep(1)
# # If you will use commnad more then one of them, you have to use it.
# for command in commands:
# 	print("Executing {$", f"{command}", "}")
# 	stdin , stdout, stderr = con.exec_command(command)
# 	print(stdout.read())
# 	print("===== Errors ======")
# 	print(stderr.read())

con.close()