#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import base64
from termcolor import colored

my_name = colored("Cor3min3r","red",attrs=['concealed','blink','bold'])

print (colored("""
                                                                                        
   _ __  _    __  _    _____ _ __ ___  ___   _   _  __
  /// /.' \ ,'_/ / //7/_  _//// // _/ / o.),' \ | |/,'
 / ` // o // /_ /  ,'  / / / ` // _/ / o \/ o | /  /  
/_n_//_n_/ |__//_/\\  /_/ /_n_//___//___,'|_,','_n_\  
                                                       
		[+] Invite Generator by """+my_name+"""

""","green"))


#proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
user_agent = {
	'User-agent': 'Mozilla/5.0',
}

req = requests.post("https://www.hackthebox.eu//api/invite/generate",headers = user_agent)

split = req.text.split('"')

c0de = base64.b64decode(split[7])

c0de = colored(c0de,"yellow") 

print "Your invitation Code is :" + c0de 

print (colored("h@I()e h4ck^ng","red"))


