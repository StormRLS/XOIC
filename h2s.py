import colorama
from colorama import Fore, Style

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
print(Fore.BLUE + Style.BRIGHT)
hours = float(input("[+]  Enter hours:"))
seconds = hours * 60 * 60
print(Fore.MAGENTA)
print("[+]  Seconds:", seconds)
print("")
print(Fore.BLUE + "[+]  Bye!")