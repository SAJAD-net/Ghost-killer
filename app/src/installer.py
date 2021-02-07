import os, shutil
from colorama import Fore, init
init()
from src.Banner import headers



@headers
def installer():
    
    print(Fore.LIGHTRED_EX+"[i]- "+Fore.LIGHTBLUE_EX+"Intalling ...")
    home=pathlib.Path.home()
    nhome=re.findall(r"\w*",str(home))
    home="/"+nhome[1]+"/"+nhome[3]
    pwd=os.getcwd()
    os.chdir(home)
    os.mkdir(".GhostKiller")
    os.chdir(pwd)
    gh = home+".GhostKiller"
    os.chdir(gh)
    os.mkdir("app")
    os.chdir("app")
    os.mkdir("src")
    ap, sr = gh+"app", gh+"src"
    os.chdir(pwd)
    for i in os.listdir("."):
        if os.isfile(i):
            shutil.copy(i,gh)
        elif i == "app":
            os.chdir("app")
            for x in os.listdir("."):
                if os.isfile
                    shutil.copy(x, ap)
                elif x == "src"
                    chdir("src")
                    for y  in os.listdir("."):
                        if os.isfile
                            shutil.copy(y, sr)
    cm = "alias ghost=python3.9"+ap+"/GhostKiller.py"    
    os.chdir(pwd)
    for i in os.listdir("."):
        if i == ".zshrc":
            os.system("echo alias ghost=python3.9 $HOME/.GhostKiller/app/GhostKiller.py >> .zshrc")
        elif i == ".bashrc":
            os.system("echo alias ghost=python3.9 $HOME/.GhostKiller/app/GhostKiller.py >> ..bashrc")
        else:
            print(Fore.LIGHTRED_EX+"[!]- Error --> Your shell is not defind !")
            exit()
    print(Fore.LIGHTRED_EX+"[i]- "+Fore.LIGHTBLUE_EX+"Copide all file to $HOME/.GhostKiller !")
    print(Fore.LIGHTBLUE_EX+"[n]- You can type ghost to running aGhostKiller app !")
    os.chdir(pwd)

