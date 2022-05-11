import requests, readline
from src.banner import headers
from colorama import Fore,init
init()


while True:
    @headers
    def httpheaders():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to http-Header's part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        http1=input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[enter the domain\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)

        if http1 == "":
            exit()
        elif http1 == "0":
            import src.chdir

        try:
            result=requests.get("http://www."+http1)
            for k,v in result.headers.items():
                print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTRED_EX}+{Fore.LIGHTBLUE_EX}]- {k} : {v} ")
            input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

        except Exception:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[error, press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
