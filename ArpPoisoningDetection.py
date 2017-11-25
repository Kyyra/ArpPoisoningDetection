#Python 3

import socket
from requests import get
import os
import time


hostname = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = get('https://api.ipify.org').text



print ("Bonjour",hostname)
print (" ")
print ("Votre IP INTERNE est :",(s.getsockname()[0]))
s.close()
print ('Votre IP EXTERNE est :', ip)

os.system('route | grep default | grep eth0  | sed \'s/\t/ /g\' | sed \'s/\ \ */ /g\' | cut -d " " -f2 > tmp.txt')

with open('tmp.txt','r') as b:
		gateway = b.readline()
		print('Votre GATEWAY est :', gateway)

os.remove('tmp.txt')



while True :

	os.system('arp -a | grep eth0 | cut -d \' \' -f2 | sed \'s/(/ /g\' | sed \'s/)/ /g\' | sed \'s/ //g\' > tmpArp.txt')
	with open('tmpArp.txt','r') as a:
		arp = a.readline()

	os.remove('tmpArp.txt')
	
	if arp != gateway :
		os.system("arp -d " +arp)
		print ("bye bye",arp)
		os.system("curl -X POST -d \"Attaque ARP sur votre pc depuis "+arp+"\" https://trafficrobot.tk/YourConnecter")

		
	time.sleep(1)