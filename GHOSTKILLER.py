import os
import sys
from colorama import init
init()
from colorama import Fore
from Banner import headers
from CloudFlare import CloudFlare
from HttpHeaders import HttpHeaders
from IPLocation import IpLocation
from PortScanner import PortScanner
from ReversIP import ReversIP
from ClientSection import Client
from WEBSection import WEB
def GHOSTKILLER(): 
    os.system('cls')
    headers()
    WE=(Fore.GREEN+'[*]'+Fore.BLUE+'Welcome To GHOST KILLER ((:\n')
    print(WE.center(65))
    print(Fore.RED+'[{}]'.format('1')+Fore.BLUE+'WEB Section\n')
    print(Fore.RED+'[{}]'.format('2')+Fore.BLUE+'Client Section\n')
    SECL=input(Fore.GREEN+'[!]'+Fore.BLUE+'┌─[Enter Number Section To Go The That\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
    if SECL == '1':
        os.system('cls')
        headers()
        WEB()
    elif SECL == '2':
        os.system('cls')
        headers()
        Client()
GHOSTKILLER()