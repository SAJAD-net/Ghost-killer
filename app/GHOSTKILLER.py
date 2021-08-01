import os, sys, readline
from colorama import Fore,init
init()
from src.Banner import headers

@headers
def GHOSTKILLER(): 
    while True:
        print(Fore.YELLOW+'[*]-',Fore.LIGHTBLUE_EX+"`"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"` Welcome To GHOST-KILLER (H4CK3R) V1.0 `"+Fore.RED+"*"+Fore.LIGHTBLUE_EX+"`\n")
        Tools=["cloudeflare",
        "httpHeaders",
        "iplocation",
        "reversip",
        "dnsLookup",
        "portScanner",
        "cmsDetect",
        "robotsScanner",
        "traceRoute",
        "sharedDnss",
        "whois",
        "adminPages"]
        while True:
            count = 1
            c=0
            for i in range(len(Tools)):
                if len(str(count)) == 1:
                    if count % 3 == 0 or count == 5 or count == 7:
                        if count != 6:
                            print("")
                    print(Fore.LIGHTRED_EX+f'\t[0{count}]-',Fore.LIGHTBLUE_EX+Tools[c],"\t",end="")
                    count+=1
                    c+=1
                elif count == 11:
                    print(Fore.LIGHTRED_EX+f'\n\t[{count}]-',Fore.LIGHTBLUE_EX+Tools[c],"\t",end="")
                    count+=1
                    c+=1
                elif count == 12:
                    print(Fore.LIGHTRED_EX+f'\t\t[{count}]-',Fore.LIGHTBLUE_EX+Tools[c],"\t",end="\n") 
                    break
                elif c == 5:
                    print("\t",end="")
                else:
                    print(Fore.LIGHTRED_EX+f'\t[{count}]-',Fore.LIGHTBLUE_EX+Tools[c],"\t",end="") 
                    count+=1
                    c+=1
            Self=input(Fore.YELLOW+'\n[!]-'+Fore.LIGHTBLUE_EX+' ┌─[enter number to chose tool ((:\n'+Fore.LIGHTBLUE_EX+'     └──╼ '+Fore.YELLOW+'GHOST-K '+Fore.RED+'✗ '+Fore.LIGHTBLUE_EX)
            if Self == '1' or Self == '01':
                import src.cloudflare.cloudeflare
            elif Self == '2' or Self == '02':
                import src.httpheaders.httpheaders
            elif Self == '3' or Self == '03':
                import src.iplocation.iplocation
            elif Self == '4' or Self == '04':
                import src.reversip.reversip
            elif Self == '5' or Self == '05':
                import src.dnslookup.dnslookup
                
            elif Self == '6' or Self == "06":
                import src.portscanner.portscanner
            elif Self == '7' or Self == "07":
                import src.cms.cms
            elif Self == '8' or Self == "08":
                import src.robots.robots
            elif Self == '9' or Self == "09":
                import src.traceroute.traceroute
            elif Self == '10' or Self == "10":
                import src.findsharedns.fsd
            elif Self == '11' or Self == "11":
                import src.whois.whois
            elif Self == '12' or Self == "12":
                import src.finder.finder
            elif Self == "quit":
                exit()
            else:
                input(Fore.LIGHTRED_EX+'[!]- '+Fore.LIGHTBLUE_EX+'┌─[field, press enter to exit :( \n'+Fore.LIGHTBLUE_EX+'     └──╼ '+Fore.YELLOW+'GHOST-K '+Fore.RED+'✗ '+Fore.LIGHTBLUE_EX)
                exit()
