import readline
from colorama import Fore,init
init()
from src.banner import headers
from socket import gethostbyname

while True:
    @headers
    def cloudflare():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to cloudFlare bypass part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        subdomain=['ftp','localhost','host','webmail','local','mysql','vb','blog']
        addrss=input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[enter the address\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)

        if addrss == "0":
            import src.chdir
        elif addrss == "":
            exit()

        for sub in subdomain:
            try:
                hosts=str(sub) + '.' + str(addrss)
                bypass = gethostbyname(str(hosts))
                print(Fore.LIGHTBLUE_EX+'[!]-',Fore.LIGHTBLUE_EX+'cloudFlare bypass --> ' + str(bypass) + ':' + str(hosts))

            except Exception:
                input(f"\n{Fore.LIGHTRED_EX}[!]- {Fore.LIGHTBLUE_EX}┌─[error, press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
                break
