import requests, builtwith
from colorama import Fore, init
init()
from src.Banner import headers

while True:

    @headers
    def cms():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To CMS Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        target = input(f"\n{Fore.GREEN}[!]-{Fore.LIGHTBLUE_EX}┌─[Enter The Domain\n{Fore.LIGHTBLUE_EX}    └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
        if target == "quit":
            exit()
        elif 'https://' not in target and 'http://' not in target:
            target = 'http://'+target
        info = builtwith.parse(target)
        for name in info:
            value = ''
            for val in info[str(name)]:
                name = name.replace('-',' ')
                name = name.title()
                value += str(val) 
            print(Fore.GREEN+"["+Fore.LIGHTRED_EX+"+"+Fore.GREEN+"]- "+Fore.LIGHTBLUE_EX+"\n"+name+': '+value)

        input(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
