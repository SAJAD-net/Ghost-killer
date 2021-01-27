import os,sys
from colorama import Fore,init
init()
import requests
from src.Banner import headers

def Whois():
    os.system("clear") if os.name == "posix" else os.system('cls')
    headers()
    print(Fore.RED+'[*]'+Fore.GREEN+'Welcome To Whois ((:\n')
    Addr=input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'IP/Domain\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
    if Addr == 'quit':
        sys.exit()
    try:
        data=requests.get('http://api.hackertarget.com/whois/?q='+Addr).text
        print(Fore.RED+'[+]'+Fore.LIGHTBLUE_EX+data)
        try:
            input(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'Press Enter To Back The Whois\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
            Whois()
        except:
            input('Field, Press Enter To Whois\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
            Whois()
    except:
        input('Field, Press Enter To Back The Whois\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
        Whois()
    
