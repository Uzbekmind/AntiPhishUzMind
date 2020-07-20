FG = Fore.GREEN
FC = Fore.CYAN
FW = Fore.WHITE
FY = Fore.YELLOW
FM = Fore.MAGENTA
FB = Fore.BLUE
FR = Fore.RED


import requests
import urllib.request, urllib.parse, urllib.error
import os
from colorama import Fore, Back, Style
import time

def cls():
    os.system('clear')
def banner():

    print(FG + '''
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
    print(FC + 'Created: #THE UZBEKMIND & @Uzbekmind_Public (telegram) & @Umchats (telegram Chat')
    print('--------------------------------------------------------')
    print('\n')             
cls()

banner()
print(FM + ' Misol uchun: ' + FW + 'http://saytnomi.com/\n\n')
                                
file = open('files.txt', 'r')

a = input(FY + "Saytni kiriting: " + FW)
          
if a[:-1] != '/':
    a = (a + '/')
else:
    pass

ok = '0'
for line in file:
    print(line[:-1])
                 
    try:
        urllib.request.urlretrieve(a + line[:-1] + '.txt', 'core/' + 'cracked.txt')

        ok = '1'
    except:
        print(FR + ' Hujjat ' + str(line) + ' topilmadi!')
                                              
    try:

        urllib.request.urlretrieve(a + line[:-1] + '.log', 'core/' + 'cracked.txt')
        ok = '1'
    except:                                
        print(FR + 'Log ' + str(line) + ' topilmadi!')

    try:
        urllib.request.urlretrieve(a + line[:-1]+ '.lst', 'core/' + 'cracked.txt')
        ok = '1'
    except:
        print(FR + ' Ro`yhat ' + str(line) + ' topilmadi!')
    try:
        urllib.request.urlretrieve(a + line[:-1] + '.db', 'core/' + 'cracked.db')
        ok = '2'
    except:
        print(FR + '[!] Ma`lumotlar bazasi ' + str(line) + ' topilmadi!')
        if int(ok) >= 1:
            print(FG + '[!] Tabriklaymiz! Siz fishing saytni egallab oldingiz!!!! Fayl: ' + line)
            print('')
            print(FM + '[!]Fayldagi malumotlar yuklanmoqda...' + FW + '\n\n')
            os.system('cat core/cracked.txt')
            print(FM + '[!] 15 sekund davomida yuqoridagi natijani korishingiz mumkin, undan keyin davom etamiz!')
            time.sleep(15)
            ok = 0
            if ok == '1':

                print(FC + '[!] core/cracked.txt nomli faylga saqlandi!')
            elif ok == '2':
                print(FC + '[!] core/cracked.db nomli faylga saqlandi!')
            print('\n')
            print(FB + '[!]Qidiruvimiz davom etamoqda... \n')
            time.sleep(2)
            a = '1'
if a == '1':
    cls()
    banner()

    print(FG + '[!]Fayldagi ma`lumotlar yuklanmoqda: \n\n' + FW)
    print(FY + '----------------------------------------------------------------\n\n')
    print(FW + '')
    os.system('cat core/cracked.txt')
    print(FY + '\n\n----------------------------------------------------------------')
    q = input(FG + '\nHimoyalangan ma`lumot ^^^')
 
elif a == '2':
    cls()
    banner()
    print(FG + '[!]"core/cracked.db" nomli faylga saqlandi!')
else:
    print(FB + '[!]Voy! Hech nima topilmadi!' + FW)
