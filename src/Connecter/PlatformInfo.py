import platform

def get_flag_of_endline():
    flag_of_endline = "\n"
    if( platform.system() == "Windows") :  
        flag_of_endline = "\r\n"
    else : 
        flag_of_endline = "\n"
    return flag_of_endline
pass
    
        
        