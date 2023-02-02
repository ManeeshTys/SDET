import paramiko as paramiko
import csv

from utils.configuration import getConfig

#ssh connection to aws linux server
host = getConfig()['SERVER']['host']
username = getConfig()['SERVER']['username']
password = getConfig()['SERVER']['password']
port = getConfig()['SERVER']['port']
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)


#Run commands
stdin, stdout, stderr = ssh.exec_command("cat demofile")
lines = stdout.readlines()
print(lines[1])

#upload files
sftp = ssh.open_sftp()
destinationPath = 'Scripts.py'
localPath = 'batchFiles\script.py'
sftp.put(localPath,destinationPath)

destinationPath = 'loanasa.csv'
localPath = 'batchFiles\loanasa.csv'
sftp.put(localPath,destinationPath)

#Trigger the Batch jobs
stdin, stdout, stderr = ssh.exec_command("python Scripts.py")

#Download the file to local sysytem
sftp.get("loanasa.csv","outputFiles\loanasa.csv")

#parse the local csv file which we downloaded
with open("outputFiles\loanasa.csv") as csvFle:
    csvReader = csv.reader(csvFle,delimiter=',')
    for row in csvReader:
        if row[0]=='32321':
            assert row[1]=='approved'


ssh.close()