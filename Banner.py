def headers():
    import os
    os.system('cls')
    from colorama import init
    init()
    from colorama import Fore
    from pyfiglet import figlet_format
    header=('GHOST KILLER')
    print(Fore.RED,(figlet_format(header)))
    header=(Fore.RED+"""
####################################################################            
**           .::Name is apps :: .:GHOST KILLER:.                  ** **                                                         	  **
**                *Producer* || *SAJAD.CH*                        **
**          .::Programmer::. :: .::SAJAD.CH::.                    **
**              *Works is*   || *By offensive Security Pen Test*  **
**          .::Tools::.      :: .::[port scan \ ip finder         **
**                           || cmd \ se.. dir,file and more...]  ** **                        ::                                      **                 
####################################################################
""")
    print(header)
#headers()
  
