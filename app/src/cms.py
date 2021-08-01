import requests, builtwith, readline
from colorama import Fore, init
init()
from src.Banner import headers

while True:

    @headers
    def cms():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To CMS Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        target = input(f"\n{Fore.YELLOW}[!]-{Fore.LIGHTBLUE_EX}┌─[Enter The Domain\n{Fore.LIGHTBLUE_EX}    └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
        if target == "quit":
            exit()
        elif target == "0":
            import src.chdir
        elif 'https://' not in target and 'http://' not in target:
            target = 'http://'+target
        info = builtwith.parse(target)
        for name in info:
            value = ''
            for val in info[str(name)]:
                name = name.replace('-',' ')
                name = name.title()
                value += str(val) 
            print(Fore.YELLOW+"["+Fore.LIGHTRED_EX+"+"+Fore.YELLOW+"]- "+Fore.LIGHTBLUE_EX+name+' : '+value)

        input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
