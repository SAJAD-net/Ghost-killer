from colorama import Fore,init
init()
from src.Banner import headers
import requests, readline
import ipapi
while True:
    @headers
    def ipLocation():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to IP-location-finder part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        site = input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[enter ip address\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)

        if site == "":
            exit()
        if site.strip() == "0":
            import src.chdir

        try:
            Source=requests.get(f"https://ipapi.co/{site}/json/")
            print(Source.text)
            input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

        except Exception:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[error, press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
