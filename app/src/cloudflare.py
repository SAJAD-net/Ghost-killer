import readline
from colorama import Fore,init
init()
from src.Banner import headers
from socket import gethostbyname

while True:
    @headers
    def cloudflare():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To CloudFlare Bypass Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        subdomain=['ftp','localhost','host','webmail','local','mysql','vb','blog']
        Addrss=input(f"\n{Fore.YELLOW}[!]-{Fore.LIGHTBLUE_EX}┌─[Please Enter The Target Website Address\n{Fore.LIGHTBLUE_EX}    └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
        if Addrss == "0":
            import src.chdir
        elif Addrss == "quit":
            exit()   
        for sub in subdomain:
            try:
                Hosts=str(sub) + '.' + str(Addrss)
                Bypass = gethostbyname(str(Hosts))
                print(Fore.LIGHTBLUE_EX+'[!]-',Fore.LIGHTBLUE_EX+'CloudFlare Bypass --> ' + str(Bypass) + '::' + str(Hosts))
            except:
                input(f"\n{Fore.LIGHTRED_EX}[!]-{Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back \n{Fore.LIGHTBLUE_EX}    └──╼ {Fore.YELLOW}GHOST-K {Fore.RED}✗ "+Fore.LIGHTBLUE_EX)
                break
