
import time
import ConnecterContext
"""bridge of mach and context"""
class Connecter(object):
    context = None
    mach = None
    __instance = None
    order = None
    def __init__(self):
        pass
    
    @classmethod
    def getinstance(cls, mach, context):
        if cls.__instance == None:          
            cls.__instance = Connecter()
            cls.__instance.context = context
            cls.__instance.mach = mach
            cls.__instance.order = None
        else:
            cls.__instance.mach
        return cls.__instance
    
    def login(self, loginMach):
        if self.order == None:
            self.order = 1
            self.context.connect()
            self.context.login()
            
        else:
            self.order = self.order + 1
            self._secLogin(loginMach)
            #self.context.send()
            pass
        
    def _secLogin(self, machine):
        if machine.connectMethod == "ssh":
            self.context.send("ssh -tt " + machine.user + 
                              "@" + machine.ip)
            time.sleep(5)
            self.context.send(machine.passwd)
        elif machine.connectMethod == "telnet":
            self.context.send("telnet "+ machine.ip)
            self.context.send(machine.user)
            self.context.send(machine.passwd)
        pass
    
    def logout(self):
        if self.order == None:
            self.context.logout()
        else:
            self_seclogout()
            if self.order == 1:
                self.order = None
            
    def _seclogout(self):
        pass
     
    def send(self,sendbuff):
        self.context.send(sendbuff)
        
    def recive(self,recivebuff):
        self.context.recive(recivebuff)