

import requests
import urllib.request, urllib.parse, urllib.error
import os
from colorama import Fore, Back, Style
import time

def cls():
    os.system('clear')
def banner():

    print(Fore.GREEN + '''
       ___          _    _ ______  _       _       __   __ ________
      / _ \        | |  (_)|  ___|(_)     | |     | |  | | \_____  \
     / /_\ \ _ __  | |_  _ | |_    _  ___ | |__   | |  | |       / /
     |  _  || '_ \ | __|| ||  _|  | |/ __|| '_ \  | |  | |      / /
     | | | || | | || |_ | || |    | |\__ \| | | | | |__| |     / /___
     \_| |_/|_| |_| \__||_|\_|    |_||___/|_| |_| \_____/ ... |_______\
                                             
                                             

      _____     _____ 
     / __  \   |  _  |
     `' / /'   | |/' |
       / /     |  /| |
     ./ /___ _ \ |_/ /
     \_____/(_) \___/ 
                  
    ''')
    print(Fore.CYAN + 'Created by THE UZBEKMIND & Uzbekmind_Public (telegram) & Umchats (telegram Chat')
    print('--------------------------------------------------------')
    print('\n')             
cls()

banner()
print(Fore.MAGENTA + ' Misol uchun: ' + Fore.WHITE + 'http://saytnomi.com/\n\n')
                                
file = open('files.txt', 'r')

a = input(Fore.YELLOW + "Saytni kiriting: " + Fore.WHITE)
          
if a[:-1] != '/':
    a = (a + '/')
else:
    pass

ok = '0'
for line in file:
    print(line[:-1])
                 
    try:
        urllib.request.urlretrieve(a + line[:-1] + '.txt',  + 'cracked.txt')

        ok = '1'
    except:
        print(Fore.RED + ' Hujjat ' + str(line) + ' topilmadi!')
                                              
    try:

        urllib.request.urlretrieve(a + line[:-1] + '.log',  + 'cracked.txt')
        ok = '1'
    except:                                
        print(Fore.RED + 'Log ' + str(line) + ' topilmadi!')

    try:
        urllib.request.urlretrieve(a + line[:-1]+ '.lst',  + 'cracked.txt')
        ok = '1'
    except:
        print(Fore.RED + ' Ro`yhat ' + str(line) + ' topilmadi!')
    try:
        urllib.request.urlretrieve(a + line[:-1] + '.db',  + 'cracked.db')
        ok = '2'
    except:
        print(Fore.RED + '[!] Ma`lumotlar bazasi ' + str(line) + ' topilmadi!')
        if int(ok) >= 1:
            print(Fore.GREEN + '[!] Tabriklaymiz! Siz fishing saytni egallab oldingiz!!!! Fayl: ' + line)
            print('')
            print(Fore.MAGENTA + '[!]Fayldagi malumotlar yuklanmoqda...' + Fore.WHITE + '\n\n')
            os.system('cat core/cracked.txt')
            print(Fore.MAGENTA + '[!] 15 sekund davomida yuqoridagi natijani korishingiz mumkin, undan keyin davom etamiz!')
            time.sleep(15)
            ok = 0
            if ok == '1':

                print(Fore.CYAN + '[!] cracked.txt nomli faylga saqlandi!')
            elif ok == '2':
                print(Fore.CYAN + '[!] cracked.db nomli faylga saqlandi!')
            print('\n')
            print(Fore.BLUE + '[!]Qidiruvimiz davom etamoqda... \n')
            time.sleep(2)
            a = '1'
if a == '1':
    cls()
    banner()

    print(Fore.GREEN + '[!]Fayldagi ma`lumotlar yuklanmoqda: \n\n' + Fore.WHITE)
    print(Fore.YELLOW + '----------------------------------------------------------------\n\n')
    print(Fore.WHITE + '')
    os.system('cat cracked.txt')
    print(Fore.YELLOW + '\n\n----------------------------------------------------------------')
    q = input(Fore.GREEN + '\nHimoyalangan ma`lumot ^^^')
 
elif a == '2':
    cls()
    banner()
    print(Fore.GREEN + '[!]"cracked.db" nomli faylga saqlandi!')
else:
    print(Fore.BLUE + '[!]Voy! Hech nima topilmadi!' + Fore.WHITE)
