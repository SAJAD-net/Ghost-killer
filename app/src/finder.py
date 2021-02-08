import requests
from colorama import Fore, init
init()
from src.Banner import headers

while True:

    @headers
    def finder():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To Url-Finder Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        try:
            url = input(f"\n{Fore.GREEN}[!]-{Fore.LIGHTBLUE_EX}┌─[Enter The Website Address ...\n{Fore.LIGHTBLUE_EX}    └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
            if url == "quit":
                exit()
            elif 'https://' not in url and 'http://' not in url:
                url = 'http://'+url
            with open("lib/finder.txt") as find:
                for i in find.readlines():
                    r = requests.get(url+i)
                    if r.status_code == 200:
                        print(f'{Fore.LIGHTBLUE_EX}[{Fore.LIGHTRED_EX}+{Fore.LIGHTBLUE_EX}]-  {Fore.LIGHTBLUE_EX}{url}{i} {Fore.LIGHTGREEN_EX}  Found ')
                    else:
                        print(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]-  {Fore.LIGHTBLUE_EX}{url}{i} {Fore.LIGHTRED_EX} Not Found ')
               
                find.close()
                input(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

