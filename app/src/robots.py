import requests, readline
import time
from colorama import Fore, init
init()
from src.Banner import headers

while True:

    @headers
    def robots():
        try:
            print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To Robots Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
            url = input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[Enter Domain ...\n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)
            if url == "quit":
                exit()
            if url == "0":
                import src.chdir
            elif 'https://' not  in url and 'http://' not in url:
                url = 'http://'+url
            with open("src/lib/robots.txt", "r") as robot:
                    for line in robot.readlines():
                        ur = (url+"/"line)
                        reqs = requests.get(ur)
                        if reqs.status_code == 200:
                            print(Fore.YELLOW+"["+Fore.LIGHTRED_EX+"+"+Fore.YELLOW+"]- "+Fore.LIGHTBLUE_EX+ur)
                        else:
                            print(Fore.LIGHTRED_EX+"["+Fore.LIGHTBLUE_EX+"+"+Fore.LIGHTRED_EX+"]- "+Fore.LIGHTBLUE_EX+ur)
            input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)  
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
