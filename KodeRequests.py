import requests
import time
import pyfiglet
import colorama
import os
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

error = pyfiglet.figlet_format("Error")

re = 3

pas = pyfiglet.figlet_format("PassKode")
txt = pyfiglet.figlet_format("KodeRequests")

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

	print(Fore.CYAN + txt)

	name = input("\x1b[94m│ \x1b[36mWhat is the name of the streamer? " + Fore.BLUE)

	os.system('cls' if os.name == 'nt' else 'clear')

	discord = pyfiglet.figlet_format("DiscordRequests")


	print(Fore.RED + discord)
	print(Fore.RED + "┍━━━━━━━━━━━━━━━━━━━━━━┑")
	print("\x1b[31m│    [1] \x1b[91mFollowsBot    \x1b[31m│")
	print("\x1b[31m│    [2] \x1b[91mSpamsBot      \x1b[31m│")
	print("\x1b[31m│    [3] \x1b[91mTrollsBot     \x1b[31m│")
	print("\x1b[31m│    [4] \x1b[91mRaidsBot      \x1b[31m│")
	print(Fore.RED + "┕━━━━━━━━━━━━━━━━━━━━━━┙")
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

		print("\x1b[32m┍━━━━━━━━━━━━━━━━━┑")

		while True:
			count1 += 1
			print(f"\x1b[32m┝ \x1b[92m{count1} requests send \x1b[32m┥")
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

		print("\x1b[35m┍━━━━━━━━━━━━━━━━━┑")

		while True:
			count2 += 1
			print(f"\x1b[35m┝ \x1b[95m{count2} requests send \x1b[35m┥")
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

		print("\x1b[33m┍━━━━━━━━━━━━━━━━━┑")

		while True:
			count2 += 1
			print(f"\x1b[33m┝ \x1b[93m{count3} requests send \x1b[33m┥")
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

		count2 = 0

		print("\x1b[34m┍━━━━━━━━━━━━━━━━━┑")

		while True:
			count4 += 1
			print(f"\x1b[34m┝ \x1b[94m{count4} requests send \x1b[34m┥")
			r = requests.post("https://discord.com/api/v9/channels/1041756912431153278/messages", data=payload, headers=header)
			time.sleep(15)

	else:
		print(Fore.Red + error)

else:

	pas = pyfiglet.figlet_format("Wrong Password")
	pls = pyfiglet.figlet_format("Please try again")

	re -= 1

	print(Fore.RED + pas)
	print("\x1b[91m" + pls)
	print(f"\x1b[31mYou have {re} tries left")
	print(" ")

	moh = input("\x1b[31m│ \x1b[91mDo you want to try again (y or N)? \x1b[31m")
