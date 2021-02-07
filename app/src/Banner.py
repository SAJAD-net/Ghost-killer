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
     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝  ╚═╝
     """)
        print(Fore.LIGHTBLUE_EX+"\t"*4,"GHOST-KILLER V1.0\n"\
        ,"\t"*4,"Programmer :: "+Fore.RED+"SAJAD-CHEHRAZI\n")
        fun()
    return wrapper()

