import os
import sys
from colorama import init
init()
from colorama import Fore
from Banner import headers
file = []
directory=[]
def searchs_directory():
    count=0
    try:   
            print(Fore.GREEN+'------> It apps run to ',os.getcwd(),'<------')
            for item in os.listdir('.'):
                if os.path.isdir(item):
                    print(Fore.GREEN+'[!]',Fore.BLUE+" in to is %s a directory"%(item))
                    directory.append(item)
                    count+=1
                    ##os.system('cd..')
                    num=input(Fore.GREEN+'Do You See Your Numbers The Directory (Enter [Y/n])\t')
                    num=num.upper()
                    if num == 'Y':
                        print(count) 
                    else:
                        return 
                    
                    input(Fore.BLUE+'Press Enter The Back To SectionClient\n'+Fore.RED+'└──╼ ~ 卐')
                    os.system('cls')
                    Client()
    except:             
        print('Field to searchs directory')
        input(Fore.BLUE+'Press Enter The Back To SectionClient\n'+Fore.RED+'└──╼ ~ 卐')
    
        os.system('cls')
        Client() 
#*************************************************************************       
def searchs_file(): 
    count1=0
    print(os.getcwd())
    for item in os.listdir('.'):                  
        if os.path.isfile(item):
                print(Fore.GREEN+ '[!]',Fore.BLUE+" in to is a",'%s file'%(item))
                file.append(item) 
                count1+=1
    num1=input('Do You See your numbers The File (Enter [Y/n])\t')
    num1=num1.upper()
    if num1 == 'Y':
        print(count1)
    else:
        return
        
    input('Press Enter The Back To SectionClient')
    os.system('cls')
    Client()
#************************************************************************* 
def searchs_dirfile():
    print(os.getcwd())
    searchs_directory()
    searchs_file()
    input(Fore.BLUE+'Press Enter The Back To SectionClient\n'+Fore.RED+'└──╼ ~ 卐')
    os.system('cls')
    Client()
#*************************************************************************
def Helps():
    helps=["Enter searchs file to searchs a file",
 
'Enter searchs directory to searchs a directory',

"Enter searchs difile to searchs a directory and file",

"Enter cmd to open cmd",

"Enter ip to select a ip you computer",

"Enter quit to exit a apps",
]
    for i in helps:
        print(Fore.RED+'[$]',Fore.BLUE+i,'\n')
def Client():
    directory = []
    headers()
    section=(Fore.RED+':))'+Fore.GREEN+'\ttWelcome To Sections Client\t '+Fore.RED+'((:\n')
    print(section.center(65))
    Helps()
    for i in range(1000):    
        start=input(Fore.RED+'└──╼ ~ 卐')  
        if start == 'searchs directory':
            try:
                os.system('cls')
                searchs_directory()
                input(Fore.GREEN+'Press Enter to back a apps └──╼ ~ 卐')
                headers()
                Helps()
            except:
                r=input(Fore.GREEN+'field to searchs directory\nEnter Tryagain to again a searchs directory\n and Enter back to back a apps\n└──╼ ~ 卐 ')
                if r == 'tryagain':
                    searchs_directory() 
        elif start == 'searchs file':
            try:  
                searchs_file()
                end=input(Fore.GREEN+'Press Enter to back a apps └──╼ ~ 卐') 
                os.system('cls')
                headers()
                Helps()     
            except:
                r=input(Fore.GREEN+'field to searchs file\nEnter Tryagain to again a searchs file\n and Enter back to back a apps\n└──╼ ~ 卐 ')
                searchs_file()
        elif start == 'searchs dirfile':                        
            try:    
                searchs_file()
                end=input(Fore.GREEN+'Press Enter to back a apps └──╼ ~ 卐') 
                headers()
                Helps()     
            except:
                r=input(Fore.GREEN+'field to searchs dirfile\nEnter Tryagain to again a searchs dirfile\n and Enter back to back a apps\n└──╼ ~ 卐 ')
                searchs_dirfile()
        elif start == 'show directory':
            try:   
                os.system('cls')
                print(directory)
                end=input(Fore.BLUE+'Press Enter to back a apps └──╼ ~ 卐')
                headers()
                Helps()
            except:
                r=input(Fore.GREEN+'field to show directory,Press Enter to back a apps\n└──╼ ~ 卐')
                headers() 
                Helps()
        elif start == 'show file':
            try:
                os.system('cls')
                print(file)
                end=input(Fore.BLUE+'Press Enter to back a apps └──╼ ~ 卐')
                headers()
                Helps()
            except:
                r=input(Fore.GREEN+'field to show file,Press Enter to back a apps\n└──╼ ~ 卐')
        elif start == 'cmd':
            os.system('cls')
            os.system('cmd')
            r=input(Fore.BLUE+'Press Enter to back a apps\n└──╼ ~ 卐')
            os.system('cls')
            headers()
            Helps()
        elif start == 'ip':
            os.system('cls')
            os.system('ipconfig')
            end=input(Fore.BLUE+'Press Enter to back a apps └──╼ ~ 卐')
            os.system('cls')
            headers()
            Helps()
        elif start == 'quit':
            sys.exit()
        else:
            os.system('cls')
            input(Fore.RED+'[!] field to {} \n└──╼ ~ 卐'.format(start))
            os.system('cls')
            headers()
            Helps()
#Client()
if __name__ == "__main__":headers()