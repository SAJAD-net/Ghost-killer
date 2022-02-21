import requests, readline
from colorama import Fore, init
init()
from src.Banner import headers
while True:
    @headers
    def fsd():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to find-shared-dns part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        try:
            inp = input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[enter the domain\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)

            if inp == "":
                exit()
            if inp == "0":
                import src.chdir

            result = requests.get('https://api.hackertarget.com/findshareddns/?q=' + inp).text
            print(f'{Fore.LIGHTBLUE_EX}[{Fore.LIGHTRED_EX}+{Fore.LIGHTBLUE_EX}]- {result}')
            input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

        except Exception:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[error, press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
