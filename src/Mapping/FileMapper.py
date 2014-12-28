class FileMapper :
    def model_mapper(self,mode_type,args) :
        file=""
        if mode_type == "model":
            file = "install_"+mode_type+mode_name+".txt"
            #if(mode_name == "ips") :
                #file="install_"+mode_type+mode_name+".txt"
            #if(mode_name == "update") :
                #file="install_update.txt"                
        elif mode_type == "file":
            file=args
        elif mode_type == "auto":
            file="file.txt"
        else:
            pass 
        return file
            
        