import paramiko
import ConnecterBase
import PlatformInfo

class SSHConnecter(ConnecterBase.ConnnecterBase):
    """ """
    ip = None
    out = None
    correspondent = None
    prompt = None
    
    def connect(self, ip, prompt):
        self.correspondent = paramiko.SSHClient()
        self.correspondent.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ip = ip
        self.prompt = prompt
        pass
    
    def login(self, user, passwd):
        self.correspondent.connect(self.ip, 22, user, 
                                  passwd)
        pass
    
    def logout(self):
        self.correspondent.close()
        pass
    
    def send(self, sendbuffer):
        """ """
        stdin, self.stdout, self.stderr = self.correspondent.exec_command(
            sendbuffer)
        print sendbuffer
        print "##result="
        out = self.stdout.read()
        print out
        err = self.stderr.read()
        if "" != err:
            print err
            pass
        pass
    
    def recive(self,recivebuffer):
        if recivebuffer in self.stdout:
            pass
        pass
    