
from src import tool
import os
import sys
import getopt
if __name__ == "__main__" :
    
    opts, args = getopt.getopt(
        sys.argv[1:],"h:v:",
        [
            "help",
            "verison",
            "transfer-inputfile=",
            "remote-inputfile=",
            "model=","auto"
         ])
    
    if opts == None:
        print "Faild to load command argments"
        sys.exit(-1)
        
    for op, value in opts: 
        tmp = value 
        models = tmp.split(",")
        
        if op in ("-m","--model"): 
            model_name = value 
            mode = "model"
            sys.exit(0)
                
        elif op in ("-h", "--help"): 
            usage() 
            sys.exit(0) 
                
        elif op in ("-v", "--version"):
            show_version()
            sys.exit(0)
                
        elif op in ("--transfer-inputfile", "--remote-inputfile"):
            tmp = value
            mode = "file"
            input_files=tmp.split(",")
            
            if(op is "--transfer-inputfile"):
                tool.transfer_inputfiles.append(input_files)
                
            if(op is "--remote-inputfile"):
                remoter_inputfiles.append(input_files)  
                
            tool.fileinstall(transfer_inputfiles, remoter_inputfiles)
            sys.exit(0)
            pass
        
        elif op in ("--auto"):
            mode = "auto"
            tool.autoinstall()
            sys.exit(0)      
            pass
        
        else:
            usage() 
            sys.exit(-1)  
            pass
        
    print "completed"
