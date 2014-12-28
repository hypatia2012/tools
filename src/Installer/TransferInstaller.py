from InstallerBase import InstallerBase
from RemoteInstaller import RemoteInstaller

class TransferInstaller(InstallerBase):
    """TransferInstaller class manager Transfer computer"""
    
    def __init__(self, classname):
        """
        Initialize, but do not start  
        """
        
        self.classname = classname
        InstallerBase.__init__(self, classname)        
        #parse the format of configue file
        self.defult_file = "Script//transfer//transfer_file.txt"
        pass
    
    def do(self, mode, targs=None, rargs=None, model=None):
        dirt_brfore_behind = None
        beforeCmds = None
        afterCmds = None
        files = self.getCmdFiles(mode, targs, None, model)
        self.cmds = self.parserCmdfiles(files)
        tmpCmds = self.cmds
        self.login()
        if(self.cmds != []) :
            dirt_brfore_behind = tmpCmds[0]
        beforeCmds = dirt_brfore_behind["before"]
        self.execCmds = beforeCmds
        self.execute()
        ri = RemoteInstaller("RemoteInstaller")
        ri.do(mode,targs,rargs,model)
        afterCmds=dirt_brfore_behind["behind"]
        self.execCmds = afterCmds
        self.execute()
        self.logout()
