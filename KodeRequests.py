import requests
import time
import pyfiglet
import colorama
import os
from colorama import Back, Fore, Style

error = pyfiglet.figlet_format("Error")

re = 3

pas = pyfiglet.figlet_format("PassKode")
txt = pyfiglet.figlet_format("KodeRequests")

os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.MAGENTA + pas)

password = input("\x1b[35m│ \x1b[95mWhat is the password? " + Fore.MAGENTA)

os.system('cls' if os.name == 'nt' else 'clear')

tk = pyfiglet.figlet_format("YourToken")
print(Fore.RED + tk)
print(Fore.RED + "┍ You need to join this server! ┑")
print(Fore.RED + "│   discord.gg/tw1tchfollower   │")
print(Fore.RED + "┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
print(" ")

token = input("\x1b[31m│ \x1b[91mPlease enter your token? \x1b[31m")

os.system('cls' if os.name == 'nt' else 'clear')

if password == "KodeBg":

	os.system('cls' if os.name == 'nt' else 'clear')

	chc = pyfiglet.figlet_format("BestChoice")

	print(Fore.RED + chc)
	print(Fore.RED + "┍━━━━━━━━━━━━━━━━━━┑")
	print("\x1b[31m│    [1] \x1b[91mTwitch    \x1b[31m│")
	print("\x1b[31m│    [2] \x1b[91mKahoot    \x1b[31m│")
	print(Fore.RED + "┕━━━━━━━━━━━━━━━━━━┙")
	print(" ")

	bet = input(Fore.RED + "│ Choose from these choices? " + "\x1b[91m")

	os.system('cls' if os.name == 'nt' else 'clear')

	if bet == "1":

		print(Fore.CYAN + txt)

		name = input("\x1b[94m│ \x1b[36mWhat is the name of the streamer? " + Fore.BLUE)

		os.system('cls' if os.name == 'nt' else 'clear')

		discord = pyfiglet.figlet_format("DiscordRequests")

		print(Fore.RED + discord)
		print(Fore.RED + "┍━━━━━━━━━━━━━━━━━━━━━━━┑")
		print("\x1b[31m│     [1] \x1b[91mFollowsBot    \x1b[31m│")
		print("\x1b[31m│     [2] \x1b[91mSpamsBot*     \x1b[31m│")
		print("\x1b[31m│     [3] \x1b[91mTrollsBot*    \x1b[31m│")
		print("\x1b[31m│     [4] \x1b[91mRaidsBot*     \x1b[31m│")
		print("\x1b[31m│     [5] \x1b[91mViewsBot*     \x1b[31m│")
		print("\x1b[31m│ \x1b[91m* = Must have premium \x1b[31m│")
		print(Fore.RED + "┕━━━━━━━━━━━━━━━━━━━━━━━┙")
		print(" ")

		fod = input(Fore.RED + "│ Choose from these choices? " + "\x1b[91m")

		if fod == "1":
			os.system('cls' if os.name == 'nt' else 'clear')

			req = pyfiglet.figlet_format("OnFollows")

			print(Fore.GREEN + req)
			print("\x1b[32m│ One request = 200 Follows")
			print("\x1b[92m─────────────────────────────")
			print(f"\x1b[32m│ You are following {name}")
			print(" ")

			payload = {
			'content': "/tfollow " + name
			}

			header = {
			'authorization': token
			}

			count1 = 0

			while True:
				count1 += 1
				print(f"\x1b[32mSent \x1b[92m{count1} \x1b[32mrequests to {name}")
				r = requests.post("https://discord.com/api/v9/channels/1041756912431153278/messages", data=payload, headers=header)
				time.sleep(15)
		else:
			print(Fore.RED + error)

		if fod == "2":

			os.system('cls' if os.name == 'nt' else 'clear')

			req = pyfiglet.figlet_format("OnMessages")

			print(Fore.MAGENTA + req)

			print("\x1b[35mOne request = 15 Messages")
			print(" ")

			message = input("\x1b[95m│ Which message do you want to spam? \x1b[35m")

			os.system('cls' if os.name == 'nt' else 'clear')

			print(Fore.MAGENTA + req)
			print("\x1b[35m│ One request = 15 Messages")
			print("\x1b[95m─────────────────────────────")
			print(f"\x1b[35m│ You are spamming {name}")
			print(" ")

			payload = {
			'content': "/tspam " + name + " " + message
			}

			header = {
			'authorization': token
			}

			count2 = 0

			while True:
				count2 += 1
				print(f"\x1b[35mSent \x1b[95m{count2} \x1b[35mrequests to {name}")
				r = requests.post("https://discord.com/api/v9/channels/1041756912431153278/messages", data=payload, headers=header)
				time.sleep(15)

		else:
			print(Fore.RED + error)

		if fod == "3":

			os.system('cls' if os.name == 'nt' else 'clear')

			troll = pyfiglet.figlet_format("OnTroll")

			print(Fore.YELLOW + troll)
			print("\x1b[33m│ One request = 15 Messages")
			print("\x1b[93m─────────────────────────────")
			print(f"\x1b[33m│ You are trolling {name}")
			print(" ")

			payload = {
			'content': "/ttroll " + name
			}

			header = {
			'authorization': token
			}

			count3 = 0

			while True:
				count3 += 1
				print(f"\x1b[33mSent \x1b[93m{count1} \x1b[33mrequests to {name}")
				r = requests.post("https://discord.com/api/v9/channels/1041756912431153278/messages", data=payload, headers=header)
				time.sleep(15)

		else:
			print(Fore.RED + "error")

		if fod == "4":
			os.system('cls' if os.name == 'nt' else 'clear')

			troll = pyfiglet.figlet_format("OnRaid")

			print(Fore.BLUE + troll)
			print("\x1b[34m│ One request = 15 Raids")
			print("\x1b[94m─────────────────────────────")
			print(f"\x1b[34m│ You are raiding {name}")
			print(" ")

			payload = {
			'content': "/traid " + name
			}

			header = {
			'authorization': token
			}

			count4 = 0

			while True:
				count4 += 1
				print(f"\x1b[34mSent \x1b[94m{count4} \x1b[34mrequests to {name}")
				r = requests.post("https://discord.com/api/v9/channels/1041756912431153278/messages", data=payload, headers=header)
				time.sleep(15)

		else:
			print(Fore.RED + error)

		if fod == "5":
			os.system('cls' if os.name == 'nt' else 'clear')

			view = pyfiglet.figlet_format("OnViews")

			print(Fore.CYAN + view)
			print("\x1b[36m│ One request = 100 - 500 Viewers")
			print("\x1b[96m─────────────────────────────────")
			print(f"\x1b[36m│ You are raiding {name}")
			print(" ")

			payload = {
			'content': "!view " + name
			}

			header = {
			'authorization': token
			}

			count5 = 0

			while True:
				count5 += 1
				print(f"\x1b[36mSent \x1b[96m{count5} \x1b[36mrequests to {name}")
				r = requests.post("https://discord.com/api/v9/channels/1048661590817394808/messages", data=payload, headers=header)
				time.sleep(10)

		else:
			print(Fore.RED + "Error")

	else:
		print(Fore.RED + "Error")

	if bet == "2":

		os.system('cls' if os.name == 'nt' else 'clear')

		kah = pyfiglet.figlet_format("MyKahoot")

		print(Fore.CYAN + kah)

		room = input("\x1b[36m│ \x1b[96mPlease enter RoomId? \x1b[36m")

		os.system('cls' if os.name == 'nt' else 'clear')

		print(Fore.CYAN + kah)
		print("\x1b[36m│ One request = 25 Joins")
		print("\x1b[96m─────────────────────────────")
		print(f"\x1b[36m│ You are the room {room}")
		print(" ")

		payload = {
		'content': "/kraid " + room
		}

		header = {
		'authorization': token
		}

		count5 = 0

		while True:
			count6 += 1
			print(f"\x1b[36mSent \x1b[96m{count6} \x1b[36mrequests to {room}")
			r = requests.post("https://discord.com/api/v9/channels/1046183217755074580/messages", data=payload, headers=header)
			time.sleep(120)

	else:
		print(Fore.RED + "Error")

else:
	pas = pyfiglet.figlet_format("Wrong Password")
	pls = pyfiglet.figlet_format("Please try again")

	re -= 1

	print(Fore.RED + pas)
	print("\x1b[91m" + pls)
	print(f"\x1b[31mYou have {re} tries left")
	print(" ")

	moh = input("\x1b[31m│ \x1b[91mDo you want to try again (y or N)? \x1b[31m")
