import os
import sys
from colorama import Fore,init
init()
from src.Banner import headers
import socket
from socket import gethostbyname
from time import sleep

@headers
def CloudFlare():
    print(Fore.LIGHTBLUE_EX+'[*]-',Fore.RED+"Welcome To CloudFlare Bypass Part\n")
    subdomain=['ftp','localhost','host','webmail','local','mysql','vb','blog']
    print()
    Addrss=input(Fore.RED+"[!]-"+Fore.LIGHTBLUE_EX+'┌─[Please Enter The Target Website Address\n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+"✗ ")
    if Addrss == "back":

    elif Addrss == "quit":
        sys.exit()   
    for sub in subdomain:
        try:
            Hosts=str(sub) + '.' + str(Addrss)
            Bypass = socket.gethostbyname(str(Hosts))
            print(Fore.RED+'[!]-',Fore.LIGHTBLUE_EX+'CloudFlare Bypass' + str(Bypass) + '::' + str(Hosts))
        except Exception:
            input('\n'+Fore.LIGHTBLUE_EX+'┌─[Error Exception Field, Press Enter To Go The Cloudflare \n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+"✗ ")
            CloudFlare()
    try:
        input('\n'+Fore.GREEN+'┌─[Field,Check Your Connected To Internet\nPress Enter To Back CloudFlare\n'+Fore.LIGHTBLUE_EX+'└──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+"✗ ")
        CloudFlare()
    except:
        input('\n'+Fore.LIGHTBLUE_EX+'┌─[Field, Press Enter To Go The Cloudflare \n'+Fore.LIGHTBLUE_EX+'   └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+"✗ ")
        CloudFlare()
