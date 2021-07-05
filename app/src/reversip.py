import requests, readline
from colorama import Fore,init
init()
import json
from src.Banner import headers
while True:
    @headers
    def reversip():
        print(Fore.LIGHTBLUE_EX+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To Port-Scanner Part `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")
        try:
            Website=input(f"\n{Fore.GREEN}[!]- {Fore.LIGHTBLUE_EX}┌─[Enter Domain ...\n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗  "+Fore.LIGHTBLUE_EX)
            if Website == 'quit':
                exit()
            if Website == "0":
                import src.chdir
            else:
                Reverss={'remoteAddress': Website}
                link=requests.post('http://domains.yougetsignal.com/domains.php',Reverss)
                jsons=json.loads(link.content)
                file=open('out/reversip.txt','w')
                for rev in jsons['domainArray']:
                    print(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}{rev[0]}\n')
                    file.writelines[rev[0]]
                    print(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[The output of operation is saved as reversip.txt\n')
                input(f'{Fore.GREEN}[{Fore.LIGHTRED_EX}+{Fore.GREEN}]- {Fore.LIGHTBLUE_EX}┌─[Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
        except:
            input(f'{Fore.LIGHTRED_EX}[{Fore.LIGHTBLUE_EX}+{Fore.LIGHTRED_EX}]- {Fore.LIGHTBLUE_EX}┌─[Error, Press Enter to back ... \n{Fore.LIGHTBLUE_EX}     └──╼ {Fore.GREEN}GHOST-K {Fore.RED}✗ '+Fore.LIGHTBLUE_EX)
      
