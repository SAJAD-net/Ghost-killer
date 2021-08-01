import requests, readline
from colorama import Fore, init
init()
from src.Banner import headers

while True:

    @headers
    def finder():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to url-finder part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        try:
            url = input(f"\n{Fore.YELLOW}[!]-{Fore.LIGHTBLUE_EX}┌─[enter the website address ...\n{Fore.LIGHTBLUE_EX}    └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
            if url == "quit":
                exit()
            if url == "0":
                import src.chdir
            elif 'https://' not in url and 'http://' not in url:
                url = 'http://'+url
            with open("src/lib/finder.txt") as find:
                for i in find.readlines():
                    r = requests.get(url+"/"+i)
                    if r.status_code == 200:
                        print(f'{Fore.LIGHTBLUE_EX}[{Fore.LIGHTRED_EX}+{Fore.LIGHTBLUE_EX}]-  {Fore.LIGHTBLUE_EX}{url}"/"{i} {Fore.LIGHTYELLOW_EX} [ok] ')
                    else:
                        print(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]-  {Fore.LIGHTBLUE_EX}{url}{i} {Fore.LIGHTRED_EX} [no] ')
               
                find.close()
                input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except:
            
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[error, press enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

