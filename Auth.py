from colorama import Fore, init, Style
import requests
import ctypes
import os

def Auth():
    IP = requests.get('http://api.ipify.org/').text
    r = requests.get('https://pastebin.com/raw/...').text #Raw Pastebin URL where the IP addresses will be stored
    if IP in r:
        pass
    else:
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW('Unauthorized')
        print(Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'IP address unauthorized!')
        print(Style.RESET_ALL + Fore.RED + ' -- ' + Fore.WHITE + Style.BRIGHT + 'Your IP: ' + IP)
        input()
        quit()

Auth()
