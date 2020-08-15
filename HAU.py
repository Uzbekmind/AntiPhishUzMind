#Real author: Wannadeuth
#Translated and changed by: UzbekMind
#Banner build by: UzbekMind
#Suport author~~~UzbekMind

import requests
import urllib.request, urllib.parse, urllib.error
import os
from colorama import Fore, Back, Style
import time

FG = Fore.GREEN
FC = Fore.CYAN
FW = Fore.WHITE
FY = Fore.YELLOW
FM = Fore.MAGENTA
FB = Fore.BLUE
FR = Fore.RED

def cls():
    os.system('clear')
def banner():

    print(FG + '''
                   /)   (\  
      (/\)   (/\) ((_____)) (/\)   (/\)
      |  |   |  |  / ___ \  |  |   |  |
      |  |   |  | | /   \ | |  |   |  |
      |  |___|  | | |\_/| | |  |   |  |
      |  \___/  | | |/ \| | |  |   |  |
      |  |   |  | | |   | | |  |   |  |
      |  |   |  | | |   | | |   \_/   |
      |  |   |  | | /   \ |  \  ___  /
       \/     \/  |/     \|   \/   \/
      
      Crack attacker easily...
    ''')
    print(FC + "Author: #THE UZBEKMIND & @Uzbekmind_Public (telegram) & @Umchats (telegram Chat)")
    print('--------------------------------------------------------')
    print('\n')             
cls()

banner()
print(FM + 'For example | Misol uchun: ' + FW + 'http://example.com | http://saytnomi.com/\n\n')
                                
file = open('files.txt', 'r')

a = input(FY + "Enter phishing site | Fishing saytni kiriting: " + FW)
          
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
        print(FR + 'File' + str(line) + 'Not found' + FG + ' | ' + FR + 'Hujjat' + str(line) + ' topilmadi!')
                                              
    try:

        urllib.request.urlretrieve(a + line[:-1] + '.log', 'core/' + 'cracked.txt')
        ok = '1'
    except:                                
        print(FR + 'Log' + str(line) + 'Not found' + FG + ' | ' + FR + 'Log' + str(line) + 'topilmadi!')

    try:
        urllib.request.urlretrieve(a + line[:-1]+ '.lst', 'core/' + 'cracked.txt')
        ok = '1'
    except:
        print(FR + 'List' + str(line) + 'Not found' + FG ' | ' + FR + 'Ro`yhat' + str(line) + 'topilmadi!')
    try:
        urllib.request.urlretrieve(a + line[:-1] + '.db', 'core/' + 'cracked.db')
        ok = '2'
    except:
        print(FR + 'Data base' + str(line) + 'Not found!' + FG ' | ' + FR 'Ma`lumotlar bazasi' + str(line) + 'topilmadi!')
        if int(ok) >= 1:
            print(FG + 'Great hack my kiddie! Cracked file:' + line + FR + ' | ' + FG + 'Qoyilmaqom ish! Siz fishing saytni egallab oldingiz! Fayl nomi: ' + line)
            print('')
            print(FM + ' Loading files...' + FG + ' | ' + FM + 'Fayldagi malumotlar yuklanmoqda...' + FW + '\n\n')
            os.system('cat core/cracked.txt')
            print(FM + 'See results, after 7 sec we`ll continue' + FG + ' | ' + FM '7 sekund davomida yuqoridagi natijani ko`rishingiz mumkin, undan keyin davom etamiz!')
            time.sleep(7)
            ok = 0
            if ok == '1':

                print(FC + 'Saved: core/cracked.txt' + FG + ' | ' + FC 'core/cracked.txt nomli faylga saqlandi!')
            elif ok == '2':
                print(FC + 'Saved: core/cracked.db' + FG ' | ' + FC 'core/cracked.db nomli faylga saqlandi!')
            print('\n')
            print(FB + 'Cracking again...' + FG + ' | ' + FB + 'Qidiruvimiz davom etamoqda... \n')
            time.sleep(2)
            a = '1'
if a == '1':
    cls()
    banner()

    print(FG + 'Loading file data...' + FR ' | ' + FG + 'Fayldagi ma`lumotlar yuklanmoqda: \n\n' + FW)
    print(FY + '----------------------------------------------------------------\n\n')
    print(FW + '')
    os.system('cat core/cracked.txt')
    print(FY + '\n\n----------------------------------------------------------------')
    q = input(FG + 'Secured data' + FR + ' | ' + FG '\nHimoyalangan ma`lumot!')
 
elif a == '2':
    cls()
    banner()
    print(FG + 'Saved: core/cracked.db' + FR ' | ' + FG + 'core/cracked.db nomli faylga saqlandi!')
else:
    print(FB + 'Oops! Nothing found!' + FG + ' | ' + FB 'Voy! Hech nima topilmadi!' + FW)
