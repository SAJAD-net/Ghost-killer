import requests
from colorama import Fore,init
init()
from src.Banner import headers

while True:
    @headers
    def dnslookup():
        try:
            print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To DnsLookup Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
            inp = input(f"\n{Fore.GREEN}[!]-{Fore.LIGHTBLUE_EX}┌─[Enter The Domain\n{Fore.LIGHTBLUE_EX}    └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
            if inp == "quit":
                exit()
            elif inp == "0":
                import src.chdir
            result = requests.get('http://api.hackertarget.com/dnslookup/?q=' + inp).text
            print(Fore.GREEN+"["+Fore.LIGHTRED_EX+"+"+Fore.GREEN+"]- "+Fore.LIGHTBLUE_EX+result)
            input(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

