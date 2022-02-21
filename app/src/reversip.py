import requests, readline
from colorama import Fore,init
init()
import json
from src.Banner import headers
while True:
    @headers
    def reversip():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` welcome to reverse-ip part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        try:
            url=input(f"\n{Fore.YELLOW}[!]- {Fore.LIGHTBLUE_EX}┌─[enter domain\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)

            if url == "":
                exit()
            if url == "0":
                import src.chdir
            else:
                reverss={'remoteAddress': url}
                link=requests.post('http://domains.yougetsignal.com/domains.php',reverss)
                jsons=json.loads(link.content)
                file=open('out/reversip.txt','w')

                for rev in jsons['domainArray']:
                    print(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}{rev[0]}\n')
                    file.writelines[rev[0]]
                    print(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[the output of operation saved as reversip.txt\n')
                input(f'{Fore.YELLOW}[{Fore.LIGHTRED_EX}+{Fore.YELLOW}]- {Fore.LIGHTBLUE_EX}┌─[press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)

        except Exception:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[error, press enter to return\n{Fore.LIGHTBLUE_EX}     └──> {Fore.YELLOW}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
