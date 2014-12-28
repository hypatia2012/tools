#
import platform

def getEndlineFlag():
    """ """
    endline = "\n"
    if platform.system() == "Windows":  
        endline = "\r\n"
    else: 
        endline = "\n"
	return endline
pass
    
        
        