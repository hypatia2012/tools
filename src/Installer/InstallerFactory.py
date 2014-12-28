from TransferInstaller import TransferInstaller
from RemoteInstaller import RemoteInstaller

class InstallerFactory():
    
    def create(self,className):
        if className == "RemoteInstaller":
            return RemoteInstaller("RemoteInstaller")
        elif className == "TransferInstaller":
            return TransferInstaller("TransferInstaller")
        else:
            pass
