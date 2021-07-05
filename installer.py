import os, shutil, readline
from colorama import Fore, init
init()
from app.src.Banner import headers
import pathlib
import re



def modules():
    lis = ["requests", "ipapi", "colorama", "bs4"]
    print(Fore.LIGHTRED_EX+"[i]- "+Fore.LIGHTBLUE_EX+"Intalling ...")
    for l in lis:
        try:
            os.system(f"python3.9 -m pip install {l}")
        except:
            print(f"{Fore.LIGHTRED_EX}[!]- {Fore.LIGHTBLUE_EX}Check your conncetion !")
            break

@headers
def installer():
    
    ins = input(f"{Fore.LIGHTRED_EX}[!]- {Fore.LIGHTBLUE_EX}Are want to install require modules [Y/N] ? ") 
    if ins.upper() == "Y":
        modules()
    else:
        print(Fore.LIGHTRED_EX+"[i]- "+Fore.LIGHTBLUE_EX+"Installing ...")
        try:
            home=pathlib.Path.home()
            nhome=re.findall(r"\w*",str(home))
            home="/"+nhome[1]+"/"+nhome[3]
            pwd=os.getcwd()
            os.chdir(home)
            os.mkdir(".GhostKiller")
            os.chdir(pwd)
            gh = home+"/.GhostKiller/"
            os.chdir(gh)
            os.mkdir("app")
            os.chdir("app")
            os.mkdir("src")
            os.chdir("src")
            os.mkdir("lib")
            os.mkdir("out")
            ap, sr, lib= gh+"app/", gh+"app/"+"src/", gh+"app/src/lib"
            os.chdir(pwd)
            for i in os.listdir("."):
                if os.path.isfile(i):
                    shutil.copy(i,gh)
                elif i == "app":
                    shutil.copy("LICENSE",gh)
                    os.chdir("app")
                    for x in os.listdir("."):
                        if os.path.isfile(x):
                            shutil.copy(x, ap)
                        elif x == "src":
                            os.chdir("src")
                            for y  in os.listdir("."):
                                if os.path.isfile(y):
                                    shutil.copy(y, sr)
                                elif y == "lib":
                                    os.chdir("lib")
                                    for z  in os.listdir("."):
                                        shutil.copy(z, lib)
                                    os.chdir("../")
                            os.chdir(pwd+"/app")    
            os.chdir(home)
            for i in os.listdir(home+"/"):
                if i == ".zshrc":
                    with open(".zshrc", "a") as file:
                        file.write("alias ghost=\"python3 $HOME/.GhostKiller/app/GHOSTKILLER.py\"")
                elif i == ".bashrc":
                    with open(".bashrc", "a") as file:
                        file.write("alias ghost=\"python3 $HOME/.GhostKiller/app/GHOSTKILLER.py\"")
   
            
            print(Fore.LIGHTRED_EX+f"[!]- {Fore.LIGHTBLUE_EX}Copide all file to {home}/.GhostKiller !")
            print(Fore.LIGHTRED_EX+f"[!]- {Fore.LIGHTBLUE_EX}your computer should be restart !")
            print(Fore.LIGHTRED_EX+f"[!]- {Fore.LIGHTBLUE_EX}You can type ghost to running a GhostKiller app !")
            os.chdir(pwd)
        except FileExistsError:
            print(Fore.LIGHTRED_EX+"[+]- "+Fore.LIGHTBLUE_EX+"This are also installed")
