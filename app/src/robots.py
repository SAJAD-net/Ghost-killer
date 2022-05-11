import requests, readline
import time
from colorama import Fore, init
init()
from src.banner import headers

while True:

    @headers
    def robots():
        try:
            print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to robots-finder part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
            url = input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[enter domain\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)

            if url == "":
                exit()
            if url == "0":
                import src.chdir
            elif 'https://' not  in url and 'http://' not in url:
                url = 'http://'+url

            with open("src/lib/robots.txt", "r") as robot:
                    for line in robot.readlines():
                        ur = (url+"/"+line)
                        reqs = requests.get(ur)
                        if reqs.status_code == 200:
                            print(Fore.LIGHTBLUE_EX+"["+Fore.LIGHTGREEN_EX+"ok"+Fore.LIGHTBLUE_EX+"]- "+Fore.LIGHTBLUE_EX+ur.strip())
                        else:
                            print(Fore.LIGHTYELLOW_EX+"["+Fore.LIGHTRED_EX+"no"+Fore.LIGHTYELLOW_EX+"]- "+Fore.LIGHTBLUE_EX+ur.strip())
            input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

        except Exception:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[error, press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
