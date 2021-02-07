import sys,os
import requests
from colorama import Fore,init
init()
import sys
from src.Banner import headers
@headers
def PortScanner():
    print(Fore.GREEN+'Welcome To Port Scanner\n')
    datas=input(Fore.RED+'[*]'+Fore.LIGHTBLUE_EX+'┌─[Enter IP/Domain\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+'✗  ')
    if datas == 'quit':
        input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Press Enter To Exit\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+'✗  ')
        sys.exit()
    try:
        resualtss=requests.get('https://api.hackertarget.com/nmap/?q='+datas).text
        print(Fore.LIGHTBLUE_EX+resualtss)
        try:
            input(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Press Enter To Back The PortScanner\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+'✗  ')
            PortScanner()       
        except:
            input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Field To Back The Menu, Press Enter To exit\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+'✗  ')
            sys.exit()
    except:
        input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Field To PortScanner, Press Enter To PortScanner\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+'✗  ')
        PortScanner()
