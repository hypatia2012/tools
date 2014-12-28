#-*-coding utf-8*-
import TelnetConnecter
import SSHConnecter
import PlatformInfo
class ConnecterContext():
    """ """
    connecter=None
    method=None
    ip=None
    user=None
    passwd=None
    prompt=None
    
    def __init__(self, method, ip, user, passwd, prompt):
        self.method = method
        self.ip = ip
        self.user = user
        self.passwd = passwd
        self.prompt = prompt
        self._getContext(self._genConnecter(method)) 
    
    def _genConnecter(self,method):
        if self.method.lower() == "ssh":
            return SSHConnecter.SSHConnecter()
        elif self.method.lower() == "telnet":
            return TelnetConnecter.TelnetConnecter()
        else:
            raise        
        
    def _getContext(self,connecter):
        self.connecter = connecter
        
    def connect(self):
        self.connecter.connect(self.ip, self.prompt)
    def login(self):
        self.connecter.login(self.user, self.passwd)
        
    def logout(self):
        self.connecter.logout()
        
    def send(self,buff):
        self.connecter.send(buff)
        
    def recive(self,buff):
        self.connecter.recive(buff)
        
    @classmethod
    def create(cls, method, ip, user, passwd, prompt):
        cls(method, ip, user, passwd, prompt)      
        pass