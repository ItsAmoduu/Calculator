import os
import sys
import locale
import platform
from colorama import Fore, init, Style

# Initialize colorama and locale settings
init()
locale.setlocale(locale.LC_ALL, '')

# Constants
TITLE = "Calculator | Developed by Alessandro"

def set_console_title():
    """Set the console title for Windows."""
    if platform.system() == 'Windows':
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(TITLE)

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_ascii_art():
    print(f"""{Fore.LIGHTBLACK_EX}
          
           $$$$$$\            $$\                     $$\            $$\                         
           $$  __$$\           $$ |                    $$ |           $$ |                        
           $$ /  \__| $$$$$$\  $$ | $$$$$$$\ $$\   $$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
           $$ |       \____$$\ $$ |$$  _____|$$ |  $$ |$$ | \____$$\\_$$  _|  $$  __$$\ $$  __$$\ 
           $$ |       $$$$$$$ |$$ |$$ /      $$ |  $$ |$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|
           $$ |  $$\ $$  __$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      
           \$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      
            \______/  \_______|\__| \_______| \______/ \__| \_______|  \____/  \______/ \__|      
                                                                                   {Style.RESET_ALL}""")

def print_menu():
    print(f"""{Fore.LIGHTRED_EX}
                                1.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Addition{Style.RESET_ALL} | {Fore.LIGHTRED_EX}2.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Subtraction{Style.RESET_ALL}
                          {Fore.LIGHTRED_EX}3.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Multiplication{Style.RESET_ALL} | {Fore.LIGHTRED_EX}4.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Division{Style.RESET_ALL}
                                {Fore.LIGHTRED_EX}5.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Equality{Style.RESET_ALL} | {Fore.LIGHTRED_EX}6.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Info{Style.RESET_ALL}
                                    {Fore.LIGHTRED_EX}7.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Help{Style.RESET_ALL} | {Fore.LIGHTRED_EX}8.{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}Exit{Style.RESET_ALL}""")

def perform_operation(operation):
    try:
        a = float(input(f"{Fore.LIGHTBLACK_EX}Enter the first number: {Style.RESET_ALL}"))
        b = float(input(f"{Fore.LIGHTBLACK_EX}Enter the second number: {Style.RESET_ALL}"))
        
        if operation == 'addition':
            result = a + b
        elif operation == 'subtraction':
            result = a - b
        elif operation == 'multiplication':
            result = a * b
        elif operation == 'division':
            if b == 0:
                print(f"{Fore.RED}Error: Division by zero{Style.RESET_ALL}")
                return
            result = a / b
        elif operation == 'equality':
            if a == b:
                print(f"{Fore.LIGHTBLACK_EX}The numbers are equal.{Style.RESET_ALL}")
            elif a < b:
                print(f"{Fore.LIGHTBLACK_EX}{a} is less than {b}.{Style.RESET_ALL}")
            else:
                print(f"{Fore.LIGHTBLACK_EX}{a} is greater than {b}.{Style.RESET_ALL}")
            return
        else:
            print(f"{Fore.RED}Invalid operation.{Style.RESET_ALL}")
            return
        
        print(f"{Fore.LIGHTBLACK_EX}Result:{Style.RESET_ALL} {result}")
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter numeric values.{Style.RESET_ALL}")

def print_info():
    print(f"{Fore.LIGHTBLACK_EX}This is a simple command-line calculator developed by Alessandro. For more details, visit the GitHub repository{Style.RESET_ALL} {Fore.CYAN}(https://github.com/ItsAmoduu/Calcolator/tree/main){Style.RESET_ALL}.{Style.RESET_ALL}")

def print_help():
    print(f"{Fore.LIGHTBLACK_EX}Use the menu to select an option by entering the corresponding number. Follow the prompts to input numbers and get results.{Style.RESET_ALL}")

def main():
    set_console_title()
    
    while True:
        clear_console()
        print_ascii_art()
        print_menu()
        
        choice = input(f"\n{Fore.LIGHTBLACK_EX}Select an option: {Style.RESET_ALL}").strip()
        
        if choice == '1':
            clear_console()
            print_ascii_art()
            perform_operation('addition')
            input(f"{Fore.LIGHTBLACK_EX}Press Enter to return to the menu.{Style.RESET_ALL}")
        elif choice == '2':
            clear_console()
            print_ascii_art()
            perform_operation('subtraction')
            input(f"{Fore.LIGHTBLACK_EX}Press Enter to return to the menu.{Style.RESET_ALL}")
        elif choice == '3':
            clear_console()
            print_ascii_art()
            perform_operation('multiplication')
            input(f"{Fore.LIGHTBLACK_EX}Press Enter to return to the menu.{Style.RESET_ALL}")
        elif choice == '4':
            clear_console()
            print_ascii_art()
            perform_operation('division')
            input(f"{Fore.LIGHTBLACK_EX}Press Enter to return to the menu.{Style.RESET_ALL}")
        elif choice == '5':
            clear_console()
            print_ascii_art()
            perform_operation('equality')
            input(f"{Fore.LIGHTBLACK_EX}Press Enter to return to the menu.{Style.RESET_ALL}")
        elif choice == '6':
            clear_console()
            print_ascii_art()
            print_info()
            input(f"{Fore.LIGHTBLACK_EX}Press Enter to return to the menu.{Style.RESET_ALL}")
        elif choice == '7':
            clear_console()
            print_ascii_art()
            print_help()
            input(f"{Fore.LIGHTBLACK_EX}Press Enter to return to the menu.{Style.RESET_ALL}")
        elif choice == '8':
            print(f"{Fore.LIGHTBLACK_EX}Exiting the calculator. Goodbye!{Style.RESET_ALL}")
            sys.exit(0)
        else:
            input(f"{Fore.LIGHTBLACK_EX}Invalid choice. Please try again. {Style.RESET_ALL}{Fore.RED}(Press Enter to continue){Style.RESET_ALL}")
            clear_console()

if __name__ == '__main__':
    main()
