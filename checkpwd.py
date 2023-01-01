import os
import hashlib
import requests
import pyinputplus as pyip
import fade
import shutil
import msvcrt


def cls():
    os.system("cls" if os.name == "nt" else "clear")

CLEAR_SCREEN = "\033[2J"
RED = "\033[41m"
GREEN = "\033[32m"
RESET = "\033[0m"
GREENB = "\033[42m"

banner = fade.fire(
    """
                            ██████╗ ██╗    ██╗███╗   ██╗███████╗██████╗ ██████╗ 
                            ██╔══██╗██║    ██║████╗  ██║██╔════╝██╔══██╗╚════██╗
                            ██████╔╝██║ █╗ ██║██╔██╗ ██║█████╗  ██║  ██║  ▄███╔╝
                            ██╔═══╝ ██║███╗██║██║╚██╗██║██╔══╝  ██║  ██║  ▀▀══╝ 
                            ██║     ╚███╔███╔╝██║ ╚████║███████╗██████╔╝  ██╗   
                            ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═════╝   ╚═╝   
════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                Check if your password has been compromised
════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                             by cthulhu#5008
════════════════════════════════════════════════════════════════════════════════════════════════════════════"""
)
columns, rows = shutil.get_terminal_size()
bannerlength = "                                                                                                            "
padding = (columns - len(bannerlength)) // 2
cls()
print(" " * padding + banner + " " * padding)

def check_password_safety(password):

    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    api_url = f"https://api.pwnedpasswords.com/range/{hashed_password[:5]}"
    response = requests.get(api_url)

    if hashed_password[5:] in response.text:
        cls()

        padding = (columns - len(bannerlength)) // 2
        result1 = (
            "Your password has been compromised! Please change it as soon as possible."
        )
        padding = (columns - len(result1)) // 2
        print(" " * padding + banner + " " * padding)
        print(RED + result1 + RESET)
        print("\nPress ANY key to exit")
        msvcrt.getch()
        exit()

    else:
        cls()
        padding = (columns - len(bannerlength)) // 2
        result2 = "Your password has not been leaked and it's safe to use."
        padding = (columns - len(result2)) // 2
        print(" " * padding + banner + " " * padding)
        print(GREENB + result2 + RESET)
        print("\nPress ANY key to exit")
        msvcrt.getch()
        exit()


password = pyip.inputPassword(prompt="Enter password: ")
check_password_safety(password)