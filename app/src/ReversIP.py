import os,sys
import requests
from colorama import Fore,init
init()
import json
from src.Banner import headers
def ReversIP():
    os.system("clear") if os.name == "posix" else os.system('cls')
    headers()
    print(Fore.GREEN+'[*]'+Fore.LIGHTBLUE_EX+'┌─[Welcome To ReversIP :))\n')
    Website=input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'Eneter Domain\n'+Fore.LIGHTBLUE_EX+'    └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
    if Website == 'quit':
        sys.exit()
    Reverss={'remoteAddress': Website}
    link=requests.post('http://domains.yougetsignal.com/domains.php',Reverss)
    jsons=json.loads(link.content)
    #file=open('RevesIP.txt','w')
    for Reverss in jsons['domainArray']:
        print(Fore.GREEN+'[!]'+Reverss[0]+'\n')
        #file.writelines[Reverss[0]]
        print(Fore.RED+'[+]'+Fore.GREEN+'┌─[The output Of The Operation Is Saved AS ReversIP.txt\n'+Fore.LIGHTBLUE_EX+'    └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
        try:
            input(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Press Enter To back The ReversIP\n'+Fore.LIGHTBLUE_EX+'    └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
            ReversIP()
        except:
            input(Fore.RED+'[*]'+Fore.LIGHTBLUE_EX+'┌─[Field, Press Enter To ReversIP\n'+Fore.LIGHTBLUE_EX+'    └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
            ReversIP()
