import os
from colorama import Fore,init
init()

def headers(fun):
    def wrapper():
        os.system("clear") if os.name == "posix" else os.system('cls')
        print(Fore.RED+"""
      ██████╗██╗  ██╗ ██████╗ ███████╗████████╗   ██╗  ██╗
    ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝   ██║ ██╔
    ██║  ███╗███████║██║   ██║███████╗   ██║█████╗█████╔╝
    ██║   ██║██╔══██║██║   ██║╚════██║   ██║╚════╝██╔═██╗
    ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║      ██║  ██╗
     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝  ╚═╝""")
        print(Fore.BLUE+"\t"*3,f"programmer {Fore.RED}: "+Fore.BLUE+"SAJAD-CHEHRAZI\n")
        fun()
    return wrapper()
