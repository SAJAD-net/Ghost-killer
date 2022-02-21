import requests, builtwith, readline
from colorama import Fore, init
init()
from src.Banner import headers

while True:

    @headers
    def cms():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to cms part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        target = input(f"\n{Fore.YELLOW}[!]-{Fore.LIGHTBLUE_EX}┌─[enter the domain\n{Fore.LIGHTBLUE_EX}    └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)

        if target == "":
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

        input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
