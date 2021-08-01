import sys
import requests, readline
from colorama import Fore, init
init()
from src.Banner import headers
while True:

    @headers
    def traceroute():
        try:
            print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To Trace-Route Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
            inp = input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[Enter Domain ...\n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)
            if inp == "quit":
                exit()
            if inp == "0":
                import src.chdir
            result = requests.get('https://api.hackertarget.com/mtr/?q=' + inp).text
            print(Fore.YELLOW+"["+Fore.LIGHTRED_EX+"+"+Fore.YELLOW+"]- "+Fore.LIGHTBLUE_EX+result)
            input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
                
        
