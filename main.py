import os
import sys
import logging
import locale
import platform

from colorama import Fore, init, Style

# Initialize colorama
init()
locale.setlocale(locale.LC_ALL, '')

# Path configurations
TITLE = "Calculator | Developed by Alessandro"

def title():
    if platform.system() == 'Windows':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(TITLE)
    print()

def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

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

def print_menu():
    print(f"""{Fore.LIGHTRED_EX}                                        1.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Addition{Style.RESET_ALL} | {Fore.LIGHTRED_EX}2.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Subtraction{Style.RESET_ALL}\n
                                  {Fore.LIGHTRED_EX}3.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Multiplication{Style.RESET_ALL} | {Fore.LIGHTRED_EX}4.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Division{Style.RESET_ALL}\n
                                        {Fore.LIGHTRED_EX}5.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Equality{Style.RESET_ALL} | {Fore.LIGHTRED_EX}6.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Info{Style.RESET_ALL}\n
                                            {Fore.LIGHTRED_EX}7.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Help{Style.RESET_ALL} | {Fore.LIGHTRED_EX}8.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Exit{Style.RESET_ALL}""")

def main():
    title()

    print_ascii_art()
    print_menu()
    while True:
        key = input(f"{Fore.LIGHTBLACK_EX}Select an option: {Style.RESET_ALL}").strip()
        if key == '1':
            clear_console()
            print_ascii_art()
            print_addition()
        elif key == '2':
            clear_console()
            print_ascii_art()
            print_subtraction()
        elif key == '3':
            clear_console()
            print_ascii_art()
            print_multiplication()
        elif key == '4':
            clear_console()
            print_ascii_art()
            print_division()
        elif key == '5':
            clear_console()
            print_ascii_art()
            print_equality()
        elif key == '6':
            clear_console()
            print_ascii_art()
            print_info()
        elif key == '7':
            clear_console()
            print_ascii_art()
            print_help()
        elif key == '8':
            sys.exit(0)
        else:
            input(f"         {Fore.LIGHTBLACK_EX}Invalid choice. Please try again. {Style.RESET_ALL}{Fore.RED}(Press Enter){Style.RESET_ALL}")
            clear_console()
            print_ascii_art()

def print_addition():
    a = float(input(f"{Fore.LIGHTBLACK_EX}Enter the first number: {Style.RESET_ALL}"))
    b = float(input(f"{Fore.LIGHTBLACK_EX}Enter the second number: {Style.RESET_ALL}"))
    print(f"{Fore.LIGHTBLACK_EX}Result:{Style.RESET_ALL} {a + b}")

def print_subtraction():
    a = float(input(f"{Fore.LIGHTBLACK_EX}Enter the first number: {Style.RESET_ALL}"))
    b = float(input(f"{Fore.LIGHTBLACK_EX}Enter the second number: {Style.RESET_ALL}"))
    print(f"{Fore.LIGHTBLACK_EX}Result:{Style.RESET_ALL} {a - b}")

def print_multiplication():
    a = float(input(f"{Fore.LIGHTBLACK_EX}Enter the first number: {Style.RESET_ALL}"))
    b = float(input(f"{Fore.LIGHTBLACK_EX}Enter the second number: {Style.RESET_ALL}"))
    print(f"{Fore.LIGHTBLACK_EX}Result:{Style.RESET_ALL} {a * b}")

def print_division():
    a = float(input(f"{Fore.LIGHTBLACK_EX}Enter the first number: {Style.RESET_ALL}"))
    b = float(input(f"{Fore.LIGHTBLACK_EX}Enter the second number: {Style.RESET_ALL}"))
    if b == 0:
        print(f"{Fore.RED}Error: Division by zero{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTBLACK_EX}Result:{Style.RESET_ALL} {a / b}")

def print_equality():
    a = float(input(f"{Fore.LIGHTBLACK_EX}Enter the first number: {Style.RESET_ALL}"))
    b = float(input(f"{Fore.LIGHTBLACK_EX}Enter the second number: {Style.RESET_ALL}"))
    if a == b:
        print(f"{Fore.LIGHTBLACK_EX}The numbers are equal.{Style.RESET_ALL}")
    elif a < b:
        print(f"{Fore.LIGHTBLACK_EX}{a} is less than {b}.{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTBLACK_EX}{a} is greater than {b}.{Style.RESET_ALL}")

def print_info():
    print(f"{Fore.LIGHTBLACK_EX}This is a simple command-line calculator developed by Alessandro. For more details, visit the GitHub repository.{Style.RESET_ALL}")

def print_help():
    print(f"{Fore.LIGHTBLACK_EX}Use the menu to select an option by entering the corresponding number. Follow the prompts to input numbers and get results.{Style.RESET_ALL}")

if __name__ == '__main__':
    main()
