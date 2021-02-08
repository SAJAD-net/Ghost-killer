import requests
import time
from colorama import Fore, init
init()
from src.Banner import headers

while True:

    @headers
    def robots():
        try:
            print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To Robots Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
            url = input(f"\n{Fore.GREEN}[!]- {Fore.LIGHTBLUE_EX}┌─[Enter Domain ...\n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)
            if url == "quit":
                exit()
            elif 'https://' not  in url and 'http://' not in url:
                url = 'http://'+url
            with open("lib/Robots.txt", "r") as robot:
                    for line in robot.readlines():
                        ur = (url+"/"+i)
                        reqs = requests.get(ur)
                        if reqs.status_code == 200 or reqs.status_code == 405:
                            print(Fore.GREEN+"["+Fore.LIGHTRED_EX+"+"+Fore.GREEN+"]- "+Fore.LIGHTBLUE_EX+ur)
                        else:
                            print(Fore.LIGHTRED_EX+"["+Fore.LIGHTBLUE_EX+"+"+Fore.LIGHTRED_EX+"]- "+Fore.LIGHTBLUE_EX+ur)
            input(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)  
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)