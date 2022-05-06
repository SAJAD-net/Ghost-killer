import os, sys, readline
from colorama import Fore,init
from src.Banner import headers
init()


@headers
def main():
    while True:
        print(Fore.YELLOW+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+\
        Fore.LIGHTBLUE_EX+"` Welcome To GHOST-KILLER (H4CK3R) V1.6 `"+\
              Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`")

        rednum = Fore.LIGHTRED_EX
        bluene = Fore.LIGHTBLUE_EX
        print(f"""
        {rednum}[01]- {bluene}cloudeFlare 		{rednum}[02]- {bluene}httpHeaders
        {rednum}[03]- {bluene}IPlocation 		{rednum}[04]- {bluene}reversIP
        {rednum}[05]- {bluene}dnsLookup 		{rednum}[06]- {bluene}portScanner
        {rednum}[07]- {bluene}cmsDetect 		{rednum}[08]- {bluene}robotsScanner
        {rednum}[09]- {bluene}traceRoute 		{rednum}[10]- {bluene}sharedDns
        {rednum}[11]- {bluene}whois             \t{rednum}[12]- {bluene}adminPages""")

        self=input(Fore.YELLOW+'\n[!]-'+Fore.LIGHTBLUE_EX+\
                   ' ┌─[choose the tool number ((:\n'+Fore.LIGHTBLUE_EX+\
                   '     └──> '+Fore.YELLOW+'GHOST-K '+Fore.RED+'✗ '+Fore.LIGHTBLUE_EX)

        if self == '1':
            import src.cloudflare.cloudeflare
        elif self == '2':
            import src.httpheaders.httpheaders
        elif self == '3':
            import src.iplocation.iplocation
        elif self == '4':
            import src.reversip.reversip
        elif self == '5':
            import src.dnslookup.dnslookup
        elif self == '6':
            import src.portscanner.portscanner
        elif self == '7':
            import src.cms.cms
        elif self == '8' :
            import src.robots.robots
        elif self == '9' :
            import src.traceroute.traceroute
        elif self == '10':
            import src.findsharedns.fsd
        elif self == '11':
            import src.whois.whois
        elif self == '12':
            import src.finder.finder
        else:
            sys.exit()
