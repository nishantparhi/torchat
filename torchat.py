#!/usr/bin/env python
#Author: Nishant Parhi
#Coded and Developed by: @nishantparhi

import socket
import threading
import time
import os
import platform
import sys
import Crypto
from Crypto.Cipher import AES
import socket
try:
	import socks
except:
	import pip
	pip.main(['install', 'pysocks'])
import subprocess
try:
	import dns
except:
	import pip
	pip.main(['install', 'pydns'])
user_name_peer = ''
username = ''
key_value = ''
socket_val = ''
sock0 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
class c:
	r = '\033[0;31m'
	g = '\033[0;31m'
	o = '\033[0;33m'
	b = '\033[0;94m'
	p = '\033[0;35m'
	w = '\033[0;97m'
        rb = '\033[01;31m'
        gb = '\033[01;31m'
        ob = '\033[01;33m'
        bb = '\033[01;94m'
        pb = '\033[01;35m'
        wb = '\033[01;97m'
	d = '\033[0;00m'
logo1 = ("""
_________ _______  _______  _______           _______ _________
\__   __/(  ___  )(  ____ )(  ____ \|\     /|(  ___  )\__   __/
   ) (   | (   ) || (    )|| (    \/| )   ( || (   ) |   ) (   
   | |   | |   | || (____)|| |      | (___) || (___) |   | |   
   | |   | |   | ||     __)| |      |  ___  ||  ___  |   | |   
   | |   | |   | || (\ (   | |      | (   ) || (   ) |   | |   
   | |   | (___) || ) \ \__| (____/\| )   ( || )   ( |   | |   
   )_(   (_______)|/   \__/(_______/|/     \||/     \|   )_(   
                                                                                                                                 
""")
logo2 = ("""
                                                                                            
 _________ _______  _______  _______           _______ _________
\__   __/(  ___  )(  ____ )(  ____ \|\     /|(  ___  )\__   __/
   ) (   | (   ) || (    )|| (    \/| )   ( || (   ) |   ) (   
   | |   | |   | || (____)|| |      | (___) || (___) |   | |   
   | |   | |   | ||     __)| |      |  ___  ||  ___  |   | |   
   | |   | |   | || (\ (   | |      | (   ) || (   ) |   | |   
   | |   | (___) || ) \ \__| (____/\| )   ( || )   ( |   | |   
   )_(   (_______)|/   \__/(_______/|/     \||/     \|   )_(   
                                                                                    
                    Coded and Developed by: NISHANT PARHI
""")
print(c.b+'                  Uses AES-256 bit encryption & Tor Proxies!'+c.d)
print(c.r+logo2+c.d)
class os_type:
	os_type1 = platform.system()
class sockets:
	sock1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def init_proxy():
	subprocess.call('service tor restart', shell=True)
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1",9050, True)
	socket.socket = socks.socksocket
	try:
		import requests
	except:
		import pip
		pip.main(['install', 'requests'])
	r = requests.get('http://ipinfo.io/ip').content
	print("Tor IP Address: {}").format(r.strip())
def enc_msg(message,key):
	iv = 'Yu_920_v^:[}=+%$'
	enc = AES.new(key, AES.MODE_CFB, iv)
	msg = enc.encrypt(str(message))
	return(msg)
def dec_msg(message,key):
	iv = 'Yu_920_v^:[}=+%$'
	dec = AES.new(key, AES.MODE_CFB,iv)
	msg = dec.decrypt(str(message))
	return(msg)
def start_server(host,port):
	global user_name_peer
	global username
	global client
	global sock0
	sock0.bind((host,port))
	sock0.listen(1)
	(client, (ip,port)) = sock0.accept()
	client.send(str(username))
	if(os_type.os_type1 == 'Linux'):
		user_name_peer = client.recv(1024)
		print(c.w+'['+c.g+"info"+c.w+"]: "+c.b+"{} "+c.w+"has joined your channel..."+c.d).format(user_name_peer)
	elif(os_type.os_type1 == 'Windows'):
		user_name_peer = client.recv(1024)
		print('[info]: {} has joined your channel...').format(user_name_peer)
def recieve_data():
	global client
	global user_name_peer
	global key_value
	while True:
		data = client.recv(10240)
		if(os_type.os_type1 == 'Linux'):
			print(c.g+"\n{}:"+c.w+" {}"+c.d).format(user_name_peer,dec_msg(data,key_value))
		elif(os_type == 'Windows'):
			print("\n{}: {}").format(user_name_peer,dec_msg(data,key_value))
def allow_connections():
        global user_name_peer
        global username
        global client
        global sock0
        while True:
                (client, (ip,port)) = sock0.accept()
                client.send(str(username))
                if(os_type.os_type1 == 'Linux'):
                        user_name_peer = client.recv(1024)
                        print(c.w+'['+c.g+"info"+c.w+"]: "+c.b+"{} "+c.w+"has joined your channel..."+c.d).format(user_name_peer)
                elif(os_type.os_type1 == 'Windows'):
                        user_name_peer = client.recv(1024)
                        print('[info]: {} has joined your channel...').format(user_name_peer)
def chat(host,port):
	start_server(host,port)
#	t1 = threading.Thread(target=allow_connections)
#	t1.setDaemon(True)
#	t1.start()
	global key_value
	chat_thread = []
	t = threading.Thread(target=recieve_data)
	t.setDaemon(True)
	t.start()
	while True:
		if(os_type.os_type1 == 'Linux'):
			try:
				s_msg = raw_input(c.b+'Send Message: '+c.w)
				client.send(enc_msg(s_msg,key_value))
			except KeyboardInterrupt:
				ex_ = raw_input("Are you sure you would like to exit (y/n): ")
                	        if(ex_ == 'y'):
                	                print('\n')
                	                client.send(enc_msg(str(username+' has left the chat!'),key_value))
                	                client.close()
                	                try:
                	                        exit(0)
                	                except:
                	                        sys.exit(0)
                	except Exception as e:
                	        print('Socket Connection Error.')
                	        try:
                	                exit(0)
                	        except:
                	                sys.exit(1)
		elif(os_type.os_type1 == 'Windows'):
			try:
				s_msg = raw_input('Send Message: ')
				client.send(enc_msg(s_msg,key_value))
	                except KeyboardInterrupt:
	                        ex_ = raw_input("Are you sure you would like to exit (y/n): ")
	                        if(ex_ == 'y'):
	                                print('\n')
	                                client.send(enc_msg(str(username+' has left the chat!'),key_value))
	                                client.close()
	                                try:
	                                        exit(0)
	                                except:
	                                        sys.exit(0)
	                except Exception as e:
	                        print('Socket Connection Error.')
	                        try:
	                                exit(0)
	                        except:
	                                sys.exit(1)
def exec_server():
	global key_value
	global username
	host = raw_input("Server to host channel on: ")
	port = input("Port to run server on: ")
	key = raw_input("Encryption Key: ")
	username = raw_input("Username: ")
        cc_val = 1
        while (cc_val == 1):
                if(len(username) > 20):
                        print("Username should not exceed 20 characters.")
                        username = raw_input("Set your username: ")
                else:
                        cc_val = 0
        if(len(key) > 32):
                for i in range(10000):
                        if(len(key) == 32):
                                break;
                        key = key[:1]
                key_value = key
        elif(len(key) < 32):
                for i in range(10000):
                        if(len(key) == 32):
                                break;
                        key = key+"}"
                key_value = key
	chat(host,port)
def recieve_data1():
        global user_name_peer
        global key_value
	global sock0
	while True:
		try:
			data = sock0.recv(10240)
			if(os_type.os_type1 == 'Linux'):
			        print(c.g+"\n{}:"+c.w+" {}"+c.d).format(user_name_peer,dec_msg(data,key_value))
			elif(os_type.os_type1 == 'Windows'):
				print('\n{}: {}').format(user_name_peer,dec_msg(data,key_value))
		except Exception as e:
			print("\nChannel has been closed")
			try:
				exit(0)
			except:
				sys.exit(1)
def join_server():
	global key_value
	global user_name_peer
	global socket_val
	global sock0
	server_addr = raw_input("Server Address: ")
	server_port = input("Server Port: ")
	key = raw_input("Encryption Key: ")
	username = raw_input("Set your username: ")
	cc_val = 1
	while (cc_val == 1):
		if(len(username) > 20):
			print("Username should not exceed 20 characters.")
			username = raw_input("Set your username: ")
		else:
			cc_val = 0
	if(len(key) > 32):
		for i in range(10000):
			if(len(key) == 32):
				break;
			key = key[:1]
		key_value = key
	elif(len(key) < 32):
		for i in range(10000):
			if(len(key) == 32):
				break;
			key = key+"}"
		key_value = key
	sock0.connect((server_addr,server_port))
	user_name_peer = sock0.recv(10240)
	print(user_name_peer)
	sock0.send(str(username))
	t = threading.Thread(target=recieve_data1)
	t.setDaemon(True)
	t.start()
	while True:
		try:
			s_msg = raw_input("Send Message: ")
			sock0.send(enc_msg(str(s_msg),key_value))
		except KeyboardInterrupt:
			ex_ = raw_input("Are you sure you would like to exit (y/n): ")
			if(ex_ == 'y'):
				print('\n')
				sock0.send(enc_msg(str(username+' has left the chat!'),key_value))
				sock0.close()
				try:
					exit(0)
				except:
					sys.exit(0)
		except Exception as e:
			print('Socket Connection Error.')
			try:
				exit(0)
			except:
				sys.exit(1)
init_proxy()
print("""
1 = Create a Channel
2 = Join a Channel
""")
opt = raw_input("Option: ")
if(opt == '1'):
	exec_server()
elif(opt == '2'):
	join_server()
