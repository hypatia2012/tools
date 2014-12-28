#-*-coding:utf 8 -*-
# Copyright 2015 hypatia as represented
#
#    If you have any questions just send them to me by mailbox.
#
#    mailaddr:    lou_ting@nec.cn
#
# All Rights Reserved.
"""
      remote script
"""
import sys
import getopt
import os
from Installer.InstallerFactory import InstallerFactory

tool_version="0.0.1"
tool_author="HY"
tool_company="NEC"

def usage():
    """show help"""
    print   'tool -v | -h | \
    \n\t\t\t --mode=  |  --transfer-inputfile= \
    \n\t\t\t--transfer-inputfile= file | --version | --help | --auto'       
    print   '\t\t\t --model="model_type" excute by model \
    \n\t\t\t\t\t model_type:{ips|update}'      
    print   '\t\t\t  mode:mode_type| \
    \n\t\t\t\t\t mode_type {mode|file|atuo} \
    \n\t\t\t\t\t transfer-inputfile="filename" \
    \n\t\t\t\t\t filename is excute script by transfer host \
    \n\t\t\t\t\t remote-inputfile="filename" \
    \n\t\t\t\t\t filename is excute script by remote host'
    print   '\t\t\t -v or --version show version imformation'      
    print   '\t\t\t -h or --help  show help'
    print   '\t\t\t -a or --auto \
    \n\t\t\t\t\t auto execute'        

def show_version():
    """show about"""
    print   'DashBoardtool version %s' % tool_version
    print   'DashBoardtool author %s' % tool_author
    print   'Dashboardtool company %s' % tool_company
    
def modeinstall(models=[]):
    """install_by_model
    ：param models:
    """
    if(models.count == 1):
        ti=InstallerFactory.create("TransferInstaller")
        ti.do("mode", None, None, models)
        return 0
    else:
        raise("/'model= /'argments is error")


def fileinstall(tfiles=[],rfiles=[]):
    """install_by_files
    :param tfiles:
    :param rfiles:
    """
    
    ifor = InstallerFactory()
    if(tfiles == []):
        ri = ifor.create("RemoteInstaller")
        ri.do("file", None, rfiles, None)  
    else:
        ti = ifor.create("RemoteInstaller")
        ti.do("file", tfiles, rfiles, None)
    
def autoinstall():
    """install_by_auto"""

    ifor = InstallerFactory()
    ti = ifor.create("TransferInstaller")
    ti.do("auto")    
    return 0

transfer_inputfiles_list=""
remoter_inputfiles_list=""
model_list=""
mode=None
