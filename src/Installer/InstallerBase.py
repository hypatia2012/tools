
import sys
print sys.path 
from Common.ToolConfigParser import ToolConfigParser
from Connecter.Connecter import Connecter
from Connecter.ConnecterContext import ConnecterContext
from Common.ScriptParser import ScriptParserContext
import time

"""
"""

class InstallerBase():
    """ Install"""
    defult_file=None
    computer=None
    comunition=None
    cmds=None
    execCmds=None
    className=None
    def __init__(self,className):
        self.className=className
        if self.className == None:
            raise
        tcp=ToolConfigParser()
        #if tcp.has_transfer_mathine() == False: 
            #raise
        ##"There is no \"transfer\" serction at configure file" 
        self.computer = tcp.getInfo(className)
        self.comunition = Connecter.getinstance(self.computer,
                                                ConnecterContext(self.computer.connectMethod,
                                                                 self.computer.ip,
                                                                 self.computer.user,
                                                                 self.computer.passwd,
                                                                 self.computer.prompt))
        
    def logout(self):
        """exit"""
        self.comunition.logout()
        pass
                
    def login(self):
        self.comunition.login(self.computer)
               
    def execute(self):
        for exec_cmd_pair in self.execCmds:
            for exec_cmd in exec_cmd_pair["cmd"]:
                self.comunition.send(exec_cmd)
                self.comunition.recive(self.computer.prompt)
                time.sleep(2)
            if exec_cmd_pair["result"] != None :
                self.comunition.recive(exec_cmd_pair["result"])
            if exec_cmd_pair["clean"] != None :
                for exec_cmd in exec_cmd_pair["clean"] :
                    self.comunition.send(exec_cmd)
                    self.comunition.recive(self.computer.prompt)
        pass
    
        #@remote(remote_ip, remote_user, remote_password)
    def getCmdFiles(self,mode,targs=None,rargs=None,model=None):
        files = []
        args = []
        if mode == "auto":
            args.append(self.defult_file)
        elif mode == "model":
            pass
        elif mode == "file":
            if self.className == "RemoteInstaller":
                args = rargs
            elif self.className == "TransferInstaller":
                args = targs
        if self.computer.ip == "127.0.0.1" or self.computer.ip == None:
            pass
        else:
            if args != []:
                files = files + args
        return files

    def parserACmdFile(self, afile):
        cmds = []
        scriptType = None
        if self.className == "RemoteInstaller":
            scriptType = "remote"
        elif self.className == "TransferInstaller":
            scriptType="transfer"
        sp = ScriptParserContext(scriptType)
        cmds = sp.do(afile)        
        return cmds
    
    def parserCmdfiles(self, files):
        cmds = []
        for afile in files:
            cmds = cmds+self.parserACmdFile(afile)
        return cmds
                
    def do(self,files=None,scriptType=None):
        pass
        