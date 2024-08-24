import os
import subprocess
import random
import sys
import time 
import locale
import logging
import ctypes
import random
import msvcrt

from colorama import Fore, init, Style
from admin_error import show_admin_error

init()
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

logging.basicConfig(filename='Logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def title():
   ctypes.windll.kernel32.SetConsoleTitleW("Calcolatrice | Developed by Alessandro")
   print()

def print_ascii_art():
    print(f"""{Fore.LIGHTBLACK_EX}
          
               $$$$$$\            $$\                     $$\            $$\                         
               $$  __$$\           $$ |                    $$ |           $$ |                        
               $$ /  \__| $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
               $$ |       \____$$\ $$ |$$  _____|$$  __$$\ $$ | \____$$\\_$$  _|  $$  __$$\ $$  __$$\ 
               $$ |       $$$$$$$ |$$ |$$ /      $$ /  $$ |$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|
               $$ |  $$\ $$  __$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      
               \$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      
                \______/  \_______|\__| \_______| \______/ \__| \_______|  \____/  \______/ \__|      
          
                                                                                   {Style.RESET_ALL}""")
def print_menù():
    print(f"""{Fore.LIGHTRED_EX}                                            1.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Somma{Style.RESET_ALL} | {Fore.LIGHTRED_EX}2.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Sottrazione{Style.RESET_ALL}\n
                                  {Fore.LIGHTRED_EX}3.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Moltiplicazione{Style.RESET_ALL} | {Fore.LIGHTRED_EX}4.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Divsione{Style.RESET_ALL}\n
                                      {Fore.LIGHTRED_EX}5.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Uguaglianza{Style.RESET_ALL} | {Fore.LIGHTRED_EX}6.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Info{Style.RESET_ALL}\n
                                             {Fore.LIGHTRED_EX}7.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Help{Style.RESET_ALL} | {Fore.LIGHTRED_EX}8.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Exit{Style.RESET_ALL}""")


def main():
    title()

    print_ascii_art()
    print_menù()
    while True:

       key = msvcrt.getch()
       if key == b'1':
          os.system('cls')
          print_ascii_art()
          print_somma()
       elif key == b'2':
           os.system('cls')
           print_ascii_art()
           print_sottrazione()
       elif key == b'3':
           os.system('cls')
           print_ascii_art
           print_moltiplicazione()
       elif key == b'4':
           os.system('cls')
           print_ascii_art()
           print_divisione()
       elif key == b'5':
           os.system('cls')
           print_ascii_art()
           print_uguaglianza()
       elif key == b'6':
           os.system('cls')
           print_ascii_art()
           print_info()
       elif key == b'7':
           os.system('cls')
           print_ascii_art()
           print_help()
       elif key == b'8':
           sys.close(0)
       else:
           input(f"         {Fore.LIGHTBLACK_EX}Invalid choice. Please try again. {Style.RESET_ALL}{Fore.RED}(Press Enter){Style.RESET_ALL}")
           os.system('cls')
           print_ascii_art()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def print_somma():
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    print(f"Risultato: {a + b}")


def print_sottrazione(a, b):
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    print(f"Risultato: {a - b}")

def print_moltiplicazione(a, b):
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    print(f"Risultato: {a * b}")

def print_divisione(a, b):
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    if b == 0:
        print(f"Errore: Divisione per zero")
    else:
        print(f"Risultato: {a / b}")

def print_uguaglianza():
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    if a == b:
        print("I numeri sono uguali.")
    elif a < b:
        print(f"{a} è minore di {b}.")
    else:
        print(f"{a} è maggiore di {b}.")

def print_info():
    
if __name__ == '__main__':
    main()