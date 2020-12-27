import os
from colorama import init
init()
from colorama import Fore
import sys
import requests
def Whois():
    os.system('cls')
    print(Fore.RED+'[*]'+Fore.GREEN+'Welcome To Whois ((:\n')
    Addr=input(Fore.RED+'[!]'+Fore.BLUE+'IP/Domain\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
    if Addr == 'quit':
        sys.exit()
    try:
        data=requests.get('http://api.hackertarget.com/whois/?q='+Addr).text
        print(Fore.RED+'[+]'+Fore.BLUE+data)
        try:
            input(Fore.GREEN+'[!]'+Fore.BLUE+'Press Enter To Back The Whois\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            Whois()
        except:
            input('Field, Press Enter To Whois\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            os.system('cls')
            Whois()
    except:
        input('Field, Press Enter To Back The Whois\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        os.system('cls')
        Whois()
    
#Whois()