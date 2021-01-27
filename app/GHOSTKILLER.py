import os, sys
from colorama import Fore,init
init()
from src.Banner import headers
from src.CloudFlare import CloudFlare
from src.HttpHeaders import HttpHeaders
from src.IPLocation import IpLocation
from src.PortScanner import PortScanner
from src.ReversIP import ReversIP
from src.Whois import Whois
def GHOSTKILLER(): 
    os.system("clear") if os.name == "posix" else os.system('cls')
    headers()
    print(Fore.GREEN+'[*]- '+Fore.LIGHTBLUE_EX+'Welcome To GHOST-KILLER (H4CK3R) V1.0\n')
    Tools=["CloudeFlare",
    "HttpHeaders",
    "IPLocation",
    "PortScanner",
    "ReversIP",
    "Whois",]
    while True:
        count = 1
        c=0
        for i in range(len(Tools)//2):
            print(Fore.LIGHTRED_EX+f'[{count}]- ',Fore.LIGHTBLUE_EX+Tools[c],"\t",end="")
            count+=1
            c+=1
            if c == 5:
                print("\t",end="")
            print(Fore.LIGHTRED_EX+f'[{count}]- ',Fore.LIGHTBLUE_EX+Tools[c],"\t",end="\n") 
            count+=1
            c+=1
        print("")
        Self=input(Fore.GREEN+'[!]-'+Fore.LIGHTBLUE_EX+' ┌─[Enter Number To Go The Tools ((:\n'+Fore.LIGHTBLUE_EX+'     └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗ '+Fore.LIGHTBLUE_EX)
        if Self == '1':
            CloudFlare()
        elif Self == '2':
            HttpHeaders()
        elif Self == '3':
            IpLocation()
        elif Self == '4':
            PortScanner()
        elif Self == '5':
            ReversIP()
        elif Self == '6':
            Whois()
        elif Self == "quit":
            input("Press Enter to quit "+Fore.RED+"✗ ")
            exit()
        else:
            input('Field,It Is Not Found, Press Enter To Back\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗ ')
GHOSTKILLER()
