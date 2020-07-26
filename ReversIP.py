import os
import sys
import requests
from colorama import init
init()
from colorama import Fore
import json
def ReversIP():
    os.system('cls')
    print(Fore.GREEN+'[*]'+Fore.BLUE+'┌─[Welcome To ReversIP :))\n')
    Website=input(Fore.RED+'[!]'+Fore.BLUE+'Eneter Domain\n'+Fore.BLUE+'    └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
    if Website == 'quit':
        sys.exit()
    Reverss={'remoteAddress': Website}
    link=requests.post('http://domains.yougetsignal.com/domains.php',Reverss)
    jsons=json.loads(link.content)
    #file=open('RevesIP.txt','w')
    for Reverss in jsons['domainArray']:
        print(Fore.GREEN+'[!]'+Reverss[0]+'\n')
        #file.writelines[Reverss[0]]
        print(Fore.RED+'[+]'+Fore.GREEN+'┌─[The output Of The Operation Is Saved AS ReversIP.txt\n'+Fore.BLUE+'    └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        try:
            input(Fore.GREEN+'[!]'+Fore.BLUE+'┌─[Press Enter To back The ReversIP\n'+Fore.BLUE+'    └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            ReversIP()
        except:
            input(Fore.RED+'[*]'+Fore.BLUE+'┌─[Field, Press Enter To ReversIP\n'+Fore.BLUE+'    └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            os.system('cls')
            ReversIP()
#ReversIP()