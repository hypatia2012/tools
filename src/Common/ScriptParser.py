#-*-coding uft-8-*-

import re

class ScriptParserContext():
    """  """
    scriptparser = None
    scripttype = None
    def __init__(self,scripttype) :
        """ 
        :param scripttype:
        """
        
        self.scripttype = scripttype
        self._getContext(self._genScriptparser(scripttype))
            
    def _getContext(self,scriptparser):
        self.scriptparser=scriptparser
        
    def _genScriptparser(self,scripttype):
        if scripttype=="remote":
            return RemoteScriptParser()
        elif scripttype=="transfer":
            return TransferScriptParser()
        else:
            raise
        pass
         
    def do(self,filename):
        return self.scriptparser.do(filename)

    @classmethod
    def create(cls,scripttype):
        cls(scripttype)
        
class ScriptParserBase():
    
    def do(self,filename):
        pass
    
comment_pattern = re.compile(r"^#")
event_pattern = re.compile(r"\[event(?P<event_group_id>\d\d)\]")
cmd_pattern = re.compile(r"^cmd\s*=\s*(?P<cmd_list>.*)")
answer_pattern = re.compile(r"^answer\s*=\s*(?P<answer_list>.*)")
clean_pattern = re.compile(r"^clean_cmd\s*=\s*(?P<clean_list>.*)")

class RemoteScriptParser(ScriptParserBase):
    exc_cmd=[]
    
    def do(self,filename):
        afile = open(filename)
        self._doparser(afile)
        afile.close()
        return self.exc_cmd
    
    def _doparser(self,afile):
      
        global tmp_dirt_cmd
        global tmp_clean_cmd
        global tmp_result
        global event_group_flag
        global tmp_cmd
        tmp_dirt_cmd = {"cmd":None, "result":None, "clean":None}
        tmp_cmd = []
        tmp_clean_cmd = []
        tmp_result = None
        event_group_flag = 0

        def _do_answer(buff):
            global tmp_result
            if buff[0] != "None":
                tmp_result = buff[0] 
            else :
                tmp_result=None   
        def _do_clean(buff):
            global tmp_clean_cmd
            global tmp_dirt_cmd
            global event_group_flag
            if buff[0] != "None":
                tmp_clean_cmd = tmp_clean_cmd + buff[0].split(",")
            else :
                tmp_clean_cmd = None 
            #group data was finished
            event_group_flag = 1
            tmp_dirt_cmd["cmd"] = tmp_cmd
            tmp_dirt_cmd["clean"] = tmp_clean_cmd
            tmp_dirt_cmd["result"] = tmp_result
            self.exc_cmd.append(tmp_dirt_cmd.copy())                  
            pass
         
        def _do_cmd(buff):
            global tmp_cmd
            tmp_cmd = tmp_cmd + buff[0].split(",")
            
        def _do_comment(buff):
            pass
        
        def _do_event(buff):
            global tmp_cmd
            global tmp_clean_cmd
            global tmp_result
            global event_group_flag
            #init or clean tmp buff
            tmp_cmd = []
            tmp_clean_cmd = []
            tmp_result = None
            #:param event_group_flag: 
            #"0" indeify the group is beginning;
            #"1" indeify the group was finished
            event_group_flag = 0            
            pass        
            
        while(1):
            line = afile.readline()
            if not line: 
                break            
            for pattern in [answer_pattern,clean_pattern,
                            comment_pattern,cmd_pattern,event_pattern]:
                m = pattern.findall(line)
                if m != []:
                    if pattern == answer_pattern:
                        _do_answer(m)
                        break
                    elif pattern == clean_pattern:
                        _do_clean(m)
                    elif pattern == cmd_pattern:
                        _do_cmd(m)
                        break
                    elif pattern == comment_pattern:
                        _do_comment(m)
                        break                    
                    elif pattern == event_pattern:
                        _do_event(m)
                        break                    
                    pass
                pass
        pass
      
    pass

before_pattern = re.compile(r"\[before\].*")
behind_pattern = re.compile( r"\[behind\].*")

class TransferScriptParser(ScriptParserBase):
    exc_cmd = []
        
    def do(self,filename):
        afile = open(filename) 
        self._doparser(afile)
        afile.close()
        return self.exc_cmd
    
    def _doparser(self,afile):
        global dirt_cmds
        global tmp_dirt_cmd
        global tmp_list
        global tmp_exc_cmd
        global tmp_result
        global event_group_flag
        global before_or_behind_none_flag
        
        dirt_cmds = {"before":None, "behind":None}
        tmp_dirt_cmd = {"cmd":None, "result":None, "clean":None}
        tmp_list = []
        tmp_exc_cmd = []
        tmp_result = None
        event_group_flag = 0
        before_or_behind_none_flag = 0
        def _do_answer(buff):
            global tmp_result
            if(buff[0] != "None") :
                tmp_result = buff[0] 
            else :
                tmp_result = None            
            pass
        def _do_before(buff):
            global tmp_list
            global before_or_behind_none_flag
            if(buff[0].lower() == "None") :
                tmp_list = []
                before_or_behind_none_flag = 1 
            else:
                before_or_behind_none_flag = 0
            pass
        def _do_behind(buff):
            global tmp_list
            global before_or_behind_none_flag
            global dirt_cmds
            if before_or_behind_none_flag == 1:
                tmp_list = []
                before_or_behind_none_flag = 0
            dirt_cmds["before"] = tmp_list
            tmp_list = []
            if buff[0]== "None":
                before_or_behind_none_flag = 1
            else :           
                pass
        def _do_comment(buff):           
            pass
        def _do_cmd(buff):
            global tmp_exc_cmd
            tmp_exc_cmd = []
            tmp_exc_cmd = tmp_exc_cmd + buff[0].split(",")
            pass
        def _do_clean(buff):
            global tmp_clean_cmd
            if buff[0] != "None":
                tmp_clean_cmd = tmp_clean_cmd + buff[0].split(",")
            else :
                tmp_clean_cmd = None  
                evnet_group_flag = 1   
                tmp_dirt_cmd["cmd"] = tmp_exc_cmd
                tmp_dirt_cmd["clean"] = tmp_clean_cmd
                tmp_dirt_cmd["result"] = tmp_result
                tmp_list.append(tmp_dirt_cmd.copy())  
                #evnet_group_flag=0
                pass                        
            pass
        def _do_event(buff):
            global tmp_dirt_cmd
            global tmp_result
            global event_group_flag
            tmp_dirt_cmd = {"cmd":None, "result":None, "clean":None}
            tmp_exc_cmd = []
            tmp_clean_cmd = []
            tmp_result = None
            event_group_flag = 0            
            pass
        
        while(1):
            line = afile.readline()
            if not line: 
                if before_or_behind_none_flag == 1:
                    dirt_cmds["behind"] = None
                else:
                    dirt_cmds["behind"] = tmp_list
                    self.exc_cmd.append(dirt_cmds.copy())
                break
            for pattern in [before_pattern, behind_pattern, event_pattern,
                            comment_pattern, cmd_pattern,
                            answer_pattern, clean_pattern]:
                m = pattern.findall(line)
                if m != []:
                    if pattern == answer_pattern:
                        _do_answer(m)
                        break  
                    elif pattern == before_pattern:
                        _do_before(m)
                        break
                    elif pattern == behind_pattern:
                        _do_behind(m)
                        break
                    elif pattern == comment_pattern:
                        _do_comment(m)
                        break
                    elif pattern == cmd_pattern:
                        _do_cmd(m)
                        break
                    elif pattern == clean_pattern:
                        _do_clean(m)
                    elif pattern == event_pattern:
                        _do_event(m)
                        break
                    pass
            pass
        pass