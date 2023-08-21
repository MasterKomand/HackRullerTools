import os
import re

try:
    import requests
except:
    os.system("pip install requests")
    import requests

import time

import sys

from os import system

try:
    from platform import platform
except:
    os.system("pip install platform")

from time import sleep

try:
    from art import *
except:
    os.system("pip install art")
    from art import *


def printtext(text):
    os.system(delet)
    art1 = text2art(text)
    print(art1)
    time.sleep(1)


def printair(i):
    for l in range(i):
        time.sleep(0.6)
        print()


puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'

printtext('H..')
printtext('Ha..')
printtext('Hac..')
printtext('Hack..')
printtext('Hacki..')
printtext('Hackin..')
printtext('Hacking..')
printtext('HackingC..')
printtext('HackingCa..')
printtext('HackingCam')

menu_ev = """1: Взлом камер Российской Федерациии!
2: Об утилите!"""
menu_number = 0


def menu():
    os.system(delet)
    printtext('HackingCam')
    print(menu_ev)
    while True:
        try:
            menu_number = int(input('Выберите число: '))
            if menu_number == 1:
                print("\n")
                os.system(delet)
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
                    for page in range(0, 82):

                        url = ("http://www.insecam.org/en/bycountry/RU/?page=" + str(page))

                        res = requests.get(url, headers=headers)
                        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                        count = 0

                        for _ in findip:
                            hasil = findip[count]
                            print("URL - камера: \033[1;37m", hasil)
                            f = open('logs.txt', 'a')
                            f.write(f'{findip}' + '\n')
                            f.close()

                            count += 1
                except:
                    print("Error")
            if menu_number == 2:
                print(
                    'Утилита создано командой: HackerRullerTools\nТелеграмм создателей:\n@MasterKomand - создатель утилиты\n@TRAILEKS - помощник по коду в termux')
        except:
            print('Введите правильное число!')
            time.sleep(3)
            menu()
            break


menu()  
