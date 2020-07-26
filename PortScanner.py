import sys
import requests
import os
from colorama import init
init()
from colorama import Fore
def PortScanner():
    os.system('cls')
    
    print(Fore.GREEN+'Welcome To Port Scanner\n')
    datas=input(Fore.RED+'[*]'+Fore.BLUE+'┌─[Enter IP/Domain\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
    if datas == 'quit':
        input(Fore.RED+'[!]'+Fore.BLUE+'┌─[Press Enter To Exit\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        sys.exit()
    try:
        resualtss=requests.get('https://api.hackertarget.com/nmap/?q='+datas).text
        print(Fore.BLUE+resualtss)
        try:
            input(Fore.GREEN+'[!]'+Fore.BLUE+'┌─[Press Enter To Back The PortScanner\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            os.system('cls')
            PortScanner()       
        except:
            input(Fore.RED+'[!]'+Fore.BLUE+'┌─[Field To Back The Menu, Press Enter To exit\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            sys.exit()
    except:
        input(Fore.RED+'[!]'+Fore.BLUE+'┌─[Field To PortScanner, Press Enter To PortScanner\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        PortScanner()
#PortScanner()
