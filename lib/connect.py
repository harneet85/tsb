import paramiko

#from elasticsearch import transport

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#transport = paramiko.Transport("dummy",22)

class conn:

    def transfer(self,sfile,dfile):
        sftp = ssh.open_sftp()
        sftp.put(sfile,dfile)
        #print("transfer done")
        
    def recieve(self,sfile,dfile):
        sftp = ssh.open_sftp()
        sftp.get(sfile,dfile)
#        print("transfer done")
        
    def transfer2(self,sfile,dfile,host,user,passw):
        transport = paramiko.Transport((host,22))
        transport.connect(username = user, password = passw)
        sftp=paramiko.SFTPClient.from_transport(transport)
        sftp.put(sfile,dfile)
        print("transfer done")
        
    def conexe(self,host,user,passw):
        ssh.connect(hostname=host, username=user, password=passw)
        transport = paramiko.Transport((host,22))
        transport.connect(username = user, password = passw)
        
    def recieve2(self,sfile,dfile,host,user,passw):
        transport = paramiko.Transport((host,22))
        transport.connect(username = user, password = passw)
        #print(vars(transport))
        sftp=paramiko.SFTPClient.from_transport(transport)
        sftp.get(sfile,dfile)
        #print(type(transport))
        print("transfer done")

    def command(self,com):
        self.com = com
        (stdin, stdout, stderr) = ssh.exec_command(com)
        str1 = ''.join(stdout)

        return str1
    
    def hccommand(self,com):
        self.com = com
        (stdin, stdout, stderr) = ssh.exec_command(com)

        return stdout
    
#ab = conn("127.0.0.1","harneesi","85@chalan")
#ab.conexe("127.0.0.1","harneesi","85@chalan")
#ab.recieve2("/home/harneesi/1", "/tmp/1","127.0.0.1","harneesi","85@chalan")
