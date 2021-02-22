import requests
from colorama import Fore,init
init()
from src.Banner import headers

while True:
    @headers
    def httpheaders():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To Http-Header's Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        http1=input(f"\n{Fore.GREEN}[!]-{Fore.LIGHTBLUE_EX}┌─[Enter The Domain ...\n{Fore.LIGHTBLUE_EX}    └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
        if http1 == 'quit':
            exit()
        if http1 == "0":
            import src.chdir
        try:
            gets=requests.get('https://api.hackertarget.com/httpheaders/?q='+http1)
            print(print(f'{Fore.LIGHTBLUE_EX}[{Fore.LIGHTRED_EX}+{Fore.LIGHTBLUE_EX}]- {gets}'))
            input(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
