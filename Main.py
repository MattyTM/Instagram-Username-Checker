#Instagram Username Checker
#Made by: Matty#8952
#Github: MattyTM
#Discord server: https://discord.gg/CJWW7DW
#Version 1.0
import requests
import string
import urllib
import pathlib
import colorama
import os, sys
import time
import selenium
from pathlib import Path
from selenium import webdriver
from colorama import *

os.system("title [Instagram] Username Checker by - Matty#8952")
current_path = os.path.dirname(os.path.realpath(__file__))
open(current_path +"/"+str("Available")+str("")+".txt","a") #Create the Available.txt
open(current_path +"/"+str("Usernames")+str("")+".txt","a") #Create the Usernames.txt
browser = webdriver.Chrome(current_path+'/chromedriver')
names = open('Usernames.txt', 'r')
available = open('Available.txt', 'w')
mypath = Path('Usernames.txt')
os.system("cls")

def check(string):
    os.system("cls")
    print(Fore.LIGHTBLACK_EX+"["+Fore.CYAN+"+"+Fore.LIGHTBLACK_EX+"]"+"------------      Instagram Username Checker by "+Fore.RESET+"Matty#8952 "+Fore.LIGHTBLACK_EX+"Made for fair use, dont sell it      ------------["+Fore.CYAN+"+"+Fore.LIGHTBLACK_EX+"]")

    if mypath.stat().st_size == 0:
        print(Fore.WHITE+"\nPlease put your NickNames in Usernames.txt"+ Fore.RED +"\nClosing in 5 seconds")
        time.sleep(5)
        browser.close()
        sys.exit()
    else:
           pass   
    print(Fore.LIGHTGREEN_EX+"\nStarting Checker...\n")
    with open('Usernames.txt', 'r') as f:
        for line in f:
            nick = line.rstrip("\n")
            browser.get('https://instagram.com/' + nick)
            if ("Esta página no está disponible." in browser.page_source) :
                print(Fore.GREEN+"[ + ] Available username "+Fore.RESET+ nick)
                available.write(nick+"\n")

            if not ("Esta página no está disponible." in browser.page_source) :
                print(Fore.RED+"[ - ] Taken username "+Fore.RESET+ nick)

check(string)

print(Fore.CYAN+"\nChecker finished.")
print("Available usernames saved!")
print(Fore.RED +"Closing in 5 seconds")
time.sleep(5)
sys.exit()