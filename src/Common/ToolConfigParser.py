########
import os
import ConfigParser
from Common.Machine import Machine
"""
"""
class ToolConfigParser(object):
    cf = None
    print os.getcwd()
    filename = "conf//tool.conf"
    mech = None
    def __init__(self, filename=None):
        self.cf = ConfigParser.ConfigParser()  
        self.cf.read(self.filename) 
        pass
    
    def has_transfer_mathine(self):
        s = self.cf.sections()
        if "transfer" in s :
            return True
        else :
            return False
    
    def _paster_file(self, section_name) :
        """
        """
        self.mach = Machine()
        s = self.cf.sections()     
        if section_name.lower() in s:
            self.mach.connectMethod = self.cf.get(section_name,"connect") 
            self.mach.ip = self.cf.get(section_name,"ip") 
            self.mach.user = self.cf.get(section_name,"user")  
            self.mach.passwd = self.cf.get(section_name,"password") 
            self.mach.prompt = self.cf.get(section_name,"cmd_prompt")  
        
    def getInfo(self,classname):
        if classname == "RemoteInstaller":
            self._paster_file("remote")
        else:
            self._paster_file("transfer")
        return self.mach