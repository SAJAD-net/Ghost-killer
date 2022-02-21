import sys
import requests, readline
from src.Banner import headers
from colorama import Fore, init
init()

while True:
    @headers
    def finder():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to url-finder part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        try:
            #Gets url from user input
            url = input(f"\n{Fore.YELLOW}[!]-{Fore.LIGHTBLUE_EX}┌─[enter the website address ...\n{Fore.LIGHTBLUE_EX}    └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)

            #Checks the url
            if url == "":
                sys.exit()
            elif url == "0":#if url equal to 0, return to the main window
                import src.chdir
            elif 'https://' and 'http://' not in url:
                url = 'http://'+url

            #Reads the finder.txt file and then sends the requests to sub pages
            with open("src/lib/finder.txt") as subpages:
                for subpage in subpages.readlines():
                    r = requests.get(url+"/"+subpage)#sends the get request to url/<sub_page>
                    if r.status_code == 200: #If page exists print <page> [ok]
                        print(f'{Fore.LIGHTBLUE_EX}[{Fore.LIGHTRED_EX}+{Fore.LIGHTBLUE_EX}]- {Fore.LIGHTBLUE_EX}{url}"/"{subpage} {Fore.LIGHTYELLOW_EX} [ok] ')

                    else:
                        print(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}{url}/{subpage} {Fore.LIGHTRED_EX} [no] ')
                subpage.close()

                input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

        except Exception:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[error, press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
