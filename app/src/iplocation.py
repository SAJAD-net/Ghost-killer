from colorama import Fore,init
init()
from src.Banner import headers
import requests, readline
import ipapi
while True:
    @headers
    def ipLocation():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To IP-Location-Finder Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        Site = input(f"\n{Fore.GREEN}[!]- {Fore.LIGHTBLUE_EX}┌─[Enter IP Address\n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)
        if Site == 'quit':
            exit()
        if Site == "0":
            import src.chdir
        try:
            #Source=ipapi.location(ip=Site)
            Source=requests.get(f"https://ipapi.co/{Site}/json/")
            print(Source.text)
            # print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.GREEN}See Your Info :))")
            # print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}IP  =  "+Source["ip"])
            # #print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}City  =  "+Source['city'])
            # print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}Region  =  "+Source['region'])
            # print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}ID Country  =  "+ Source['country'])
            # print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}Country  =  "+Source['country name'])
            # print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}Calling Code  =  "+Source['country_calling_code'])
            # print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}Languages  =  "+Source['languages'])
            # print(f"{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}org  =  "+Source['org'])
            input(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except Exception as e:
            print(e)
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
