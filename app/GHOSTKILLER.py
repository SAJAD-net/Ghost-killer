import os, sys
from colorama import Fore,init
init()
from src.Banner import headers


@headers
def GHOSTKILLER(): 
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
        Self=input(Fore.GREEN+'[!]-'+Fore.LIGHTBLUE_EX+' ┌─[Enter Number To Go The Tools ((:\n'+Fore.LIGHTBLUE_EX+'     └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+'✗ '+Fore.LIGHTBLUE_EX)
        if Self == '1':
            import src.CloudFlare.CloudFlare
        elif Self == '2':
            import src.HttpHeaders.HttpHeaders
        elif Self == '3':
            import src.IPLocation.IpLocation
        elif Self == '4':
            import src.PortScanner.PortScanner
        elif Self == '5':
            import src.ReversIP.ReversIP
        elif Self == '6':
            import src.Whois.Whois
        elif Self == "quit":
            exit()
        else:
            input(Fore.LIGHTRED_EX+'[!]-'+Fore.LIGHTBLUE_EX+' ┌─[Field, Press enter to exit :( \n'+Fore.LIGHTBLUE_EX+'     └──╼ '+Fore.GREEN+'GHOST-K '+Fore.RED+'✗ '+Fore.LIGHTBLUE_EX)
            exit()