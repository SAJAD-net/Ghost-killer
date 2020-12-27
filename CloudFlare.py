import os
import sys
from colorama import init
init()
from colorama import Fore
import socket
from socket import gethostbyname
from time import sleep
def CloudFlare():
    os.system('cls')
    print(Fore.BLUE+'[*]',Fore.RED+"Welcome To CloudFlare Bypass Part\n")
    subdomain=['ftp','localhost','host','webmail','local','mysql','vb','blog']
    print()
    Addrss=input(Fore.RED+"[!]"+Fore.BLUE+'┌─[Please Enter The Target Website Address\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+"卐")
    if Addrss == 'quit':
        input(Fore.GREEN+'[!]'+Fore.BLUE+'Press Enter To Exit\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+"卐")
        sys.exit()   
    for sub in subdomain:
        try:
            Hosts=str(sub) + '.' + str(Addrss)
            Bypass = socket.gethostbyname(str(Hosts))
            print(Fore.RED+'[!]',Fore.BLUE+'CloudFlare Bypass' + str(Bypass) + '::' + str(Hosts))
        except Exception:
            input('\n'+Fore.BLUE+'┌─[Error Exception Field, Press Enter To Go The Cloudflare \n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+"卐")
            CloudFlare()
    try:
        input('\n'+Fore.GREEN+'┌─[Field,Check Your Connected To Internet\nPress Enter To Back CloudFlare\n'+Fore.BLUE+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+"卐")
        os.system('cls')
        CloudFlare()
    except:
        input('\n'+Fore.BLUE+'┌─[Field, Press Enter To Go The Cloudflare \n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+"卐")
        CloudFlare()
        
#CloudFlare()