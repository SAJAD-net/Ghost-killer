from colorama import Fore,init
init()
import requests, readline
from src.Banner import headers
while True:

    @headers
    def whois():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To Whois Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        Addr=input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[Enter Domain ...\n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)
        if Addr == 'quit':
           exit()
        if Addr == "0":
            import src.chdir
        try:
            data=requests.get('http://api.hackertarget.com/whois/?q='+Addr).text
            print(Fore.YELLOW+"["+Fore.LIGHTRED_EX+"+"+Fore.YELLOW+"]- "+Fore.LIGHTBLUE_EX+data)
            input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.
            }GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
