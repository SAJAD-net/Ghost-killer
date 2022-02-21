def headers(fun):
    import os
    def wrapper():
        os.system("clear") if os.name == "posix" else os.system('cls')
        from colorama import Fore,init
        init()
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
