import os
import sys
import requests
from colorama import Fore,init
init()
from src.Banner import headers
def HttpHeaders():
    os.system('clear') if os.name == "posix" else os.system("cls")
    headers()
    print(Fore.RED+'[*]'+Fore.GREEN+'Welcome To HttpHeaders\n')
    http1=input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Please Enter Domain\n'\
        +Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗ ')
    if http1 == 'quit':
        sys.exit()
    try:
        gets=requests.get('http://api.hackertarget.com/httpheader/?q='+http1)
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+gets)
        input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Press Enter To Back The HttpHeaders\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗ ')
        os.system('cls')
        HttpHeaders()
    except:
        input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'Field, Press Enter To Back the HttpHeaders\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗ ')
        HttpHeaders()
#HttpHeaders()