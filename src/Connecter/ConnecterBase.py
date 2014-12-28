
#
import telnetlib

class ConnnecterBase():
    
    def connect(self,ip) :
        pass
    def login(self,user,passwd):
        pass
    def recive(self,buff):
        pass
    def send(self,buff,prompt):      
        pass
    def logout(self):
        pass
        