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
	os.system("xdg-open https://t.me/zed_cracker_1")
	try:
		import telethon
	except:
		os.system("pip install telethon")
		import telethon
		pass
	try:
		import requests
	except:
		os.system("pip install requests")
		import requests
		pass
	import os, sys, socket, random, requests
	from telethon import TelegramClient, sync, utils
	#awshtanay ka pewistn bo tools aka
	#############################################
	#pshan darakaman
	telegramspam_banner = '''

  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓   ▄▄▄█████▓▓█████  ██▓    ▓█████   ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒   ▓  ██▒ ▓▒▓█   ▀ ▓██▒    ▓█   ▀  ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░   ▒ ▓██░ ▒░▒███   ▒██░    ▒███   ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██    ░ ▓██▓ ░ ▒▓█  ▄ ▒██░    ▒▓█  ▄ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ 
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒     ▒██▒ ░ ░▒████▒░██████▒░▒████▒░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░     ▒ ░░   ░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░       ░     ░ ░  ░░ ░ ▒  ░ ░ ░  ░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░
░  ░  ░  ░░         ░   ▒   ░      ░        ░         ░     ░ ░      ░   ░ ░   ░   ░░   ░   ░   ▒   ░      ░   
      ░                 ░  ░       ░                  ░  ░    ░  ░   ░  ░      ░    ░           ░  ░       ░   
                                                                                                               

    Auther: Zed Coder
	'''

	def clearscreen():
		os.system("clear")

	def restart_program():
		# bo restart krdn
		python = sys.executable
		os.execl(python, python, * sys.argv)
		curdir = os.getcwd()

	def backtomenu_option():
		#bo garanawa bo sarata
		print()
		backtomenu = "4553635646776"
		
		if backtomenu == "4553635646776":
			restart_program()
		elif backtomenu == "8748576832783755682":
			sys.exit()
		else:
			print()
			restart_program()
	clearscreen()
	#while true wata dwbara bwnaway be kota
	while True:
		try:
			santet = "54753689735964872569834765983762983465872349875624987596438"
			if santet == "54753689735964872569834765983762983465872349875624987596438":
				os.system("claer")
				print(telegramspam_banner)
				api_id = 1148490
				api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
				client = TelegramClient('client',api_id,api_hash).start()
				#usr ean id aw kasa dana  ka atawet attack bkay sary
				target = input(" ZED > Attack USERNAME/ID ")
				#dwatr bri nardnakay
				try: count = input(" Bry Nrdn : ")
				except(ValueError): count = 999
				#dwatr aw msg ay ka atawe brwa chi bet
				urmsg = input(" ZED >  MESSAGE Akat ! : ")
				for x in range(count):
					client.send_message(target, urmsg)
					sys.stdout.write(u" \u001b[1000D[*] Sent {} messages to {}...".format(x+1, target))
					sys.stdout.flush()
				print("\n  Done ... !!\n")
				backtomenu_option()
			else:
				pass
		except(telethon.errors.rpcerrorlist.PhoneNumberInvalidError):
			print("The phone number is invalid (caused by SendCodeRequest)")
			print("You need to register your phone number first into Telegram\n")
		except(KeyboardInterrupt):
			print("\n[!] Close the program...")
		except(EOFError):
			print("\n[!] Close the program...")
		except Exception as e:
			print("\n[!] Error: "+e)
	else:
		##################################
		pass
