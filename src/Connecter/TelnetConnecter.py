from telnetlib import Telnet

from PlatformInfo import get_flag_of_endline
import ConnecterBase

class TelnetConnecter(ConnecterBase.ConnnecterBase):
    """remote connection by telnet"""
    
    prompt = None
    correspondent = None
    
    def connect(self, ip, prompt):
        """connect hostip"""
        
        self.correspondent = Telnet(ip)
        self.prompt = prompt
        pass
        
    def login(self, user, passwd):
        """user right user and password to login
        the remote machine"""
        
        self.recive("ogin: ")
        self.send(user)
        if(passwd) :
            self.recive("assword: ")
            self.send(passwd)
            pass 
        else:
            self.send(get_flag_of_endline)
        self.recive(self.prompt)
        pass     
    
    def logout(self):
        """logout from remote machine"""
        
        self.correspondent.write("exit" + get_flag_of_endline())  
        self.recive(self.prompt)
        pass
    
    def send(self, sendbuffer):
        """send strings or commands to remote machine.
        
        :parma buffer:the buffer not need to include '\n' if it is a command
        :param prompt: the command prompt of remote machine
        """
        
        print self.correspondent.write(sendbuffer)
        self.correspondent.write(get_flag_of_endline())
        pass
    def recive(self, recivebuffer):
        """the reciverbuff"""
        
        try:
            print self.correspondent.read_until(recivebuffer,5)
        except error as e:
            #log file or print buff timeout
            pass
        pass
    
    
        
