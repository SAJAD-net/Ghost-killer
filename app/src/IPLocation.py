import os,sys
from colorama import Fore,init
init()
from src.Banner import headers
import requests
#import ipapi
def IpLocation():
    os.system("clear") if os.name == "posix" else  os.system('cls')
    headers()
    print(Fore.GREEN+'[*]',Fore.LIGHTBLUE_EX+'Welcome To IPLocation\n')
    Site = input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Enter IP Address\n'+Fore.LIGHTBLUE_EX+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
    if Site == 'quit':
        sys.exit()
    try:
        Source=ipapi.location(ip=Site, key=None , field=None)
    except:
        input(Fore.RED+'Field, Check your Connected To Internet\n'+Fore.LIGHTBLUE_EX+'┌─[Press Enter To Back The Menu\n'+Fore.LIGHTBLUE_EX+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
        IpLocation()
    try:
        print(Fore.RED+'[!]'+Fore.GREEN+'See Your Info :))')
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'IP = ' + Source['ip'])
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'City = ' + Source['city'])
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'Region = ' + Source['region'])
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'ID Country = ' + Source['country'])
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'Country = ' + Source['country name'])
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'Calling Code = ' + Source['country_calling_code'])
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'Languages = ' + Source['languages'])
        print(Fore.GREEN+'[!]'+Fore.LIGHTBLUE_EX+'org = ' + Source['org'])
        try:
            input(Fore.RED+'[!]'+Fore.LIGHTBLUE_EX+'┌─[Press Enter For Back To IPLocation\n'+Fore.LIGHTBLUE_EX+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
            IpLocation()       
        except:
            input(Fore.RED+'┌─[Press Enter To IPlocation\n'+Fore.LIGHTBLUE_EX+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
            IpLocation()
    except:
        input(Fore.RED+'[1]'+Fore.LIGHTBLUE_EX+'┌─[Field, Please Enter Ip\n Press Enter To Back The IPLocation'+Fore.LIGHTBLUE_EX+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'✗')
        IpLocation()
