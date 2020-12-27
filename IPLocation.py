import os
from colorama import init
init()
from colorama import Fore
import sys
import requests
#import ipapi
def IpLocation():
    os.system('cls')
    print(Fore.GREEN+'[*]',Fore.BLUE+'Welcome To IPLocation\n')
    Site = input(Fore.RED+'[!]'+Fore.BLUE+'┌─[Enter IP Address\n'+Fore.BLUE+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
    if Site == 'quit':
        sys.exit()
    try:
        Source=ipapi.location(ip=Site, key=None , field=None)
    except:
        input(Fore.RED+'Field, Check your Connected To Internet\n'+Fore.BLUE+'┌─[Press Enter To Back The Menu\n'+Fore.BLUE+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        os.system('cls')
        IpLocation()
    try:
        print(Fore.RED+'[!]'+Fore.GREEN+'See Your Info :))')
        print(Fore.GREEN+'[!]'+Fore.BLUE+'IP = ' + Source['ip'])
        print(Fore.GREEN+'[!]'+Fore.BLUE+'City = ' + Source['city'])
        print(Fore.GREEN+'[!]'+Fore.BLUE+'Region = ' + Source['region'])
        print(Fore.GREEN+'[!]'+Fore.BLUE+'ID Country = ' + Source['country'])
        print(Fore.GREEN+'[!]'+Fore.BLUE+'Country = ' + Source['country name'])
        print(Fore.GREEN+'[!]'+Fore.BLUE+'Calling Code = ' + Source['country_calling_code'])
        print(Fore.GREEN+'[!]'+Fore.BLUE+'Languages = ' + Source['languages'])
        print(Fore.GREEN+'[!]'+Fore.BLUE+'org = ' + Source['org'])
        try:
            input(Fore.RED+'[!]'+Fore.BLUE+'┌─[Press Enter For Back To IPLocation\n'+Fore.BLUE+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            os.system('cls')
            IpLocation()       
        except:
            input(Fore.RED+'┌─[Press Enter To IPlocation\n'+Fore.BLUE+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            os.system('cls')
            IpLocation()
    except:
        input(Fore.RED+'[1]'+Fore.BLUE+'┌─[Field, Please Enter Ip\n Press Enter To Back The IPLocation'+Fore.BLUE+'└──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        os.system('cls')
        IpLocation()
#IpLocation()
