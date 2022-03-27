import socket
import colorama
from colorama import Fore, Style
print(Fore.MAGENTA + Style.BRIGHT)
print("""

     8888   8888 8888888 88 8888888
      8888 8888  88   88 88 88
       8888888   88   88 88 88
      8888 8888  88   88 88 88
     8888   8888 8888888 88 8888888
               alpha v0.1

""")

print(Fore.BLUE + Style.BRIGHT)
ip = " "

ip = input("Enter Host: " + Fore.MAGENTA)

x = socket.gethostbyname(ip)
print("ip: " + Fore.BLUE, x)
