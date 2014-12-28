import time
from Connecter.ConnecterContext import ConnecterContext
from InstallerBase import InstallerBase
from Common.ToolConfigParser import ToolConfigParser

class RemoteInstaller(InstallerBase):
    """
    the class was used at remote execute
    """
              
    def __init__(self, classname):
        """init"""
        
        self.classname = classname
        InstallerBase.__init__(self, classname)
        self.defult_file = "Script//remote//remote_file.txt"
        pass
    
    def do(self, mode, targs=None, rargs=None, model=None):
        self.exec_file = self.getCmdFiles(mode,None,rargs,model)
        self.cmds = self.parserCmdfiles(self.exec_file)
        tmpCmds = self.cmds
        self.execCmds = tmpCmds
        self.login()
        self.execute()
        self.logout()      
        
                
