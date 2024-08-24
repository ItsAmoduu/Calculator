import os
import sys
import time
import ctypes
import colorama
from colorama import Fore, Style

# Inizializza colorama
colorama.init()

def center_text(text, width):
    """Centra il testo in una larghezza specificata."""
    lines = text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def show_admin_error():
    """Mostra un messaggio di errore e termina il programma se non si è amministratori."""
    # Definisci l'ASCII art in rosso
    ascii_art = f"""
{Fore.RED}
███████╗██████╗ ██████╗  ██████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
{Style.RESET_ALL}
"""

    # Messaggio di errore con colore rosso
    error_message = f"""
{Fore.RED}
==============================
[♯] Error, please open the Tool as Administrator. (!) ({{}})
==============================
{Style.RESET_ALL}
"""

    # Calcola la larghezza del terminale
    try:
        terminal_width = os.get_terminal_size().columns
    except AttributeError:
        terminal_width = 80  # Imposta una larghezza predefinita se non riesce a ottenere la larghezza del terminale

    # Centra l'ASCII art e il messaggio di errore
    centered_art = center_text(ascii_art, terminal_width)

    for i in range(5, 0, -1):
        # Pulizia del terminale e stampa dell'ASCII art e del messaggio di errore aggiornato
        os.system('cls' if os.name == 'nt' else 'clear')
        print(centered_art)
        print(center_text(error_message.format(i), terminal_width))  # Aggiorna il countdown
        time.sleep(1)

    # Esci direttamente senza ulteriori messaggi
    sys.exit(1)

def is_admin():
    """Verifica se il programma è eseguito con privilegi di amministratore."""
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

# Esegui la funzione di controllo amministrativo
if not is_admin():
    show_admin_error()