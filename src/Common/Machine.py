#
class Machine():
    """the machine information"""
    ip = None
    user = None
    passwd = None
    prompt = None
    connectMethod = None
    machinneType = None

    def __init__(self, ip=None, user=None, passwd=None,
	             prompt=None, connectMethod=None, machinneType=None):
	"""initinual the instance of machine
	:param ip:
	:param user:
	:param passwd:
	:param prompt:
	:connectMethod:
	:machinneType:
	"""

	self.ip = ip
	self.user = user
	self.passwd = passwd
	self.prompt = prompt
	self.connectMethod = connectMethod
	self.machinneType = machinneType
	pass

    def setMachineInfo(self,ip,user,passwd,prompt,
	                   connectMethod,machinneType):
	"""setMachineInfo 
	:param ip:	
	:param user:	
	:param passwd:
	:param prompt:	
	:connectMethod:
	:machinneType:
	"""
	self.ip = ip
	self.user = user
	self.passwd = passwd
	self.passwd = prompt
	self.connectMethod = connectMethod
	self.machinneType = machinneType
	
    @classmethod
    def create(cls,ip,user,passwd,prompt,
	           connectMethod,machinneType):
	"""
	:param ip:
	:param user:
	:param passwd:	
	:param prompt:
	:connectMethod:	
	:machinneType:
	"""

	mach = cls(ip,user,passwd,prompt,connectMethod,
		     machinneType)
	return mach



