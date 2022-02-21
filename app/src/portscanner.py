import sys,os
import requests, readline
from colorama import Fore,init
init()
import sys
from src.Banner import headers
while True:
    @headers
    def portscanner():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to port-scanner part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        datas=input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[enter [ip /domain]\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)

        if datas == "":
            exit()
        if datas == "0":
            import src.chdir

        try:
            resualtss=requests.get('https://api.hackertarget.com/nmap/?q='+datas).text
            print(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}{resualtss}')
            input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

        except Exception:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[error, press Enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
