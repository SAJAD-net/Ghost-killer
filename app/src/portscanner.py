import sys,os
import requests
from colorama import Fore,init
init()
import sys
from src.Banner import headers
while True:
    @headers
    def portscanner():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To Port-Scanner Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        datas=input(f"\n{Fore.GREEN}[!]- {Fore.LIGHTBLUE_EX}┌─[Enter [IP / Domain] ...\n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)
        if datas == 'quit':
            exit()
        if datas == "0":
            import src.chdir
        try:
            resualtss=requests.get('https://api.hackertarget.com/nmap/?q='+datas).text
            print(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}{resualtss}')
            input(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
    