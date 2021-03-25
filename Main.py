#Instagram Username Checker by Fall
#Made by: fall#6087
#Github: Falzqq
#Discord name; fall#6087
#Version 1.1
import requests
import string
import pathlib
import colorama
import os, sys
import time
from pathlib import Path
from colorama import *

os.system("title [Instagram] Username Checker by - Matty#8952")
current_path = os.path.dirname(os.path.realpath(__file__))
open(current_path +"/"+str("Available")+str("")+".txt","a") #Create the Available.txt
open(current_path +"/"+str("Usernames")+str("")+".txt","a") #Create the Usernames.txt
names = open('Usernames.txt', 'r')
available = open('Available.txt', 'w')
mypath = Path('Usernames.txt')
badtoken=0

def check():
    os.system("cls")
    print(Fore.LIGHTBLACK_EX+"["+Fore.CYAN+"+"+Fore.LIGHTBLACK_EX+"]"+"------------      Instagram Username Checker by "+Fore.RESET+"Matty#8952 "+Fore.LIGHTBLACK_EX+"Made for fair use, dont sell it      ------------["+Fore.CYAN+"+"+Fore.LIGHTBLACK_EX+"]")

    if mypath.stat().st_size == 0:
        print(Fore.WHITE+"\nPlease put your NickNames in Usernames.txt"+ Fore.RED +"\nClosing in 5 seconds")
        time.sleep(5)
        sys.exit()
    else:
           pass   
    with open('Usernames.txt', 'r') as f:
            for line in f:
                time.sleep(0)
                nick = line.rstrip("\n")
                src = requests.get('https://instagram.com/'+nick)

                try:
                    if src.status_code == 200:
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"Taken"+Fore.WHITE+"] "+Fore.RESET + nick)
                    else:
                        print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"Not Taken"+Fore.WHITE+"] "+Fore.RESET+ nick)
                except Exception:
                    badtoken=99999999999999
check()

print(Fore.CYAN+"\nChecker finished.")
print("Available usernames saved!")
print(Fore.RED +"Closing in 5 seconds")
time.sleep(5)
sys.exit()
