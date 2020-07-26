def WEB():
    from colorama import Fore
    from Banner import headers
    from CloudFlare import CloudFlare
    from HttpHeaders import HttpHeaders
    from IPLocation import IpLocation
    from PortScanner import PortScanner
    from ReversIP import ReversIP
    from Whois  import Whois
    import os
    import sys
    from colorama import init
    init()
    from colorama import Fore
    os.system('cls')
    headers()
    print(Fore.GREEN+'Welcome To Section Server')
    Tools=["CloudeFlare",
"HttpHeaders",
"IPLocation",
"PortScanner",
"ReversIP",
"Whois",
]
    for i in range(1000):
        count = 1
        for i in Tools:
            print(Fore.RED+'[{}]'.format(count),Fore.BLUE+i+'\n')
            count+=1
        Self=input(Fore.GREEN+'[!]'+Fore.BLUE+'Enter Number To Go The Tools ((:\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
        if Self == '1':
            CloudFlare()
        elif Self == '2':
            HttpHeaders()
        elif Self == '3':
            IpLocation()
        elif Self == '4':
            PortScanner()
        elif Self == '5':
            ReversIP()
        elif Self == '6':
            Whois()
        else:
            input('Field,It Is Not Found, Press Enter To Back The Section Server\n'+Fore.BLUE+'   └──╼ '+Fore.GREEN+'SCH '+Fore.RED+'卐')
            WEB()
#WEB()