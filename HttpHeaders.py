import os
import sys
import requests
from colorama import init
init()
from colorama import Fore
def HttpHeaders():
    os.system('cls')
    print(Fore.RED+'[*]'+Fore.GREEN+'Welcome To HttpHeaders\n')
    http1=input(Fore.RED+'[!]'+Fore.BLUE+'┌─[Please Enter Domain\n'\
        +Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
    if http1 == 'quit':
        sys.exit()
    try:
        gets=requests.get('http://api.hackertarget.com/httpheader/?q='+http1)
        print(Fore.GREEN+'[!]'+Fore.BLUE+gets)
        input(Fore.RED+'[!]'+Fore.BLUE+'┌─[Press Enter To Back The HttpHeaders\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        os.system('cls')
        HttpHeaders()
    except:
        input(Fore.RED+'[!]'+Fore.BLUE+'Field, Press Enter To Back the HttpHeaders\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        os.system('cls')
        HttpHeaders()
#HttpHeaders()