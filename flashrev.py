#!/usr/bin/env python3

import requests
import os
import threading
import json
from socket import gethostbyname
from colorama import Fore, Back, Style
import requests,re,time,random ,os, sys, socket
from multiprocessing.dummy import Pool
from colorama import Fore


linux = 'clear'
windows = 'cls'
os.system([linux,windows][os.name == 'nt'])

hijau = Fore.GREEN
merah = Fore.RED
cyan = Fore.CYAN
tai = Fore.YELLOW
biru = Fore.BLUE
batas = Style.RESET_ALL

def Banner():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	print('''
  _____   _                 _       ____                 
 |  ___| | |   __ _   ___  | |__   |  _ \    ___  __   __
 | |_    | |  / _` | / __| | '_ \  | |_) |  / _ \ \ \ / /
 |  _|   | | | (_| | \__ \ | | | | |  _ <  |  __/  \ V / 
 |_|     |_|  \__,_| |___/ |_| |_| |_| \_\  \___|   \_/  
                   
       Unlimited Reverse IP & Delete Duplicate Domain                  
                   Betetx & Shin403
               Recode From Shin403 Rev IP
''')
Banner()


def filter(o):
	block = ['ico', 'png' , 'jpg', 'gif', 'displ','css','dataL','push', 'getEl','display','getElementById','dataLayer','getElementsByTagName']
	domen = ['cdnjs.cloudflare.com','db-ip.com', 'twitter.com','facebook.com',  'cdnjs.cloudflare.com']
	neko = set()
	for i in o:
		ext = i.split('.')[-1]
		if ext not in block and i not in domen:
			neko.add(i)
	return neko

def SHINREV(url):
	try:
		SHINGET = requests.get('http://sharingmyip.com/?site='+url,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
		if 'at this IP address' in SHINGET:
			REGEX = re.findall("(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}",SHINGET)
			SHINFIL = filter(REGEX)
			for SHIN in SHINFIL:
				SHINREP  = SHIN.replace('www.','').replace('ftp.','').replace('images.','').replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','')
				print(Fore.GREEN + '[$] REVERSE ->>' + Fore.WHITE + SHINREP)
				open('result.txt','a').write('http://'+SHINREP+'\n')
			else:
				print(Fore.RED + '[x] BAD CANT REVERSE :(' + Fore.WHITE)
	except:
				pass

def DELETE_DUPLICATE():
	with open('result.txt', 'r') as SHINXX:
		SHINXXX = list(dict.fromkeys(SHINXX.read().splitlines()))
		with open('result.txt.tmp','a') as new:
			new.write('\n'.join(SHINXXX))
			new.close()
		SHINXX.close()
	os.remove('result.txt')
	os.rename('result.txt.tmp','result.txt')


def Main():
	try:
		list = input("\n\033[91mDomain List\033[97m:~# \033[97m").replace('http://', '').replace('https://', '')
		che = open(list, 'r').read().splitlines()
		pp = Pool(50)
		pr = pp.map(SHINREV, che)
	except:
		pass

if __name__ == '__main__':
	Main()
	DELETE_DUPLICATE()